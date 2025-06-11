from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..database.db import (create_challenge, get_user_challenges, get_challenge_quota, reset_quota_if_needed, create_challenge_quota)
from ..utils import authenticate_and_get_user_details
from ..database.models import get_db
import json
from datetime import datetime
from ..ai_generator import generate_challenge

router = APIRouter()

class ChallengeRequest(BaseModel):
    difficulty: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "difficulty": "easy"
            }
        }

@router.post("/generate-challenge")
async def generate_challenge_endpoint(request: ChallengeRequest, request_obj: Request, db: Session = Depends(get_db)):
    try:
        user_details = authenticate_and_get_user_details(request_obj)
        user_id = user_details.get("user_id")
        quota = get_challenge_quota(db, user_id)
        
        # Create quota if it doesn't exist
        if not quota:
            quota = create_challenge_quota(db, user_id)
        
        # Reset quota if needed and check remaining
        quota = reset_quota_if_needed(db, quota)
        if quota.quota_remaining <= 0:
            raise HTTPException(status_code=429, detail="Quota Exceeded")
        
        challenge_data = generate_challenge(request.difficulty)
        
        # Convert options list to JSON string
        challenge_data['options'] = json.dumps(challenge_data['options'])
        
        new_challenge = create_challenge(
            db=db, 
            difficulty=request.difficulty, 
            created_by=user_id,
            **challenge_data)

        quota.quota_remaining -= 1
        db.commit()

        return {
        "id": new_challenge.id,
        "difficulty": request.difficulty,
        "title": new_challenge.title,
        "options": json.loads(new_challenge.options),
        "correct_answer_id": new_challenge.correct_answer_id,
        "explanation": new_challenge.explanation,
        "timestamp": new_challenge.date_created.isoformat()
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/my-history")
async def get_my_history(request: Request, db: Session = Depends(get_db)):
    user_details = authenticate_and_get_user_details(request)
    user_id = user_details.get("user_id")
    challenges = get_user_challenges(db, user_id)
    return {"challenges": challenges}
    
    
    
@router.get("/quota")
async def get_quota(request: Request, db: Session = Depends(get_db)):
    user_details = authenticate_and_get_user_details(request)
    user_id = user_details.get("user_id")
    
    # Get or create quota
    quota = get_challenge_quota(db, user_id)
    if not quota:
        quota = create_challenge_quota(db, user_id)
    
    # Reset quota if needed
    quota = reset_quota_if_needed(db, quota)
    return {
        "user_id": quota.user_id,
        "quota_remaining": quota.quota_remaining,
        "last_reset_at": quota.last_reset_at.isoformat()
    }

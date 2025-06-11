from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


engine = create_engine("sqlite:///ai_code_challenger.db", echo=True)
Base = declarative_base()

class Challenge(Base):
    __tablename__ = "challenges"
    id = Column(Integer, primary_key=True)
    difficulty = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.now())
    created_by = Column(String, nullable=False)
    title = Column(String, nullable=False)
    options = Column(String, nullable=False)
    correct_answer_id = Column(Integer, nullable=False)
    explanation = Column(String, nullable=False)

class ChallengeQuota(Base):
    __tablename__ = "challenge_quota"
    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False, unique=True)
    quota_remaining = Column(Integer, nullable=False, default=10)
    last_reset_at = Column(DateTime, nullable=False, default=datetime.now())
    
    

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
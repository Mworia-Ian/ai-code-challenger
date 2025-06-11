# CodeQuest AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A web application that generates coding challenges using AI, tracks user progress, and enforces daily quotas. Built with a modern tech stack including FastAPI, React, and Clerk for authentication.

## Features

- 🚀 AI-generated coding challenges with multiple difficulty levels (easy, medium, hard)
- 🔒 Secure user authentication and management with Clerk
- 📊 Daily challenge quota system to manage API usage
- 💅 Sleek, responsive, and modern UI with a dark theme
- 📝 Challenge history tracking to review past attempts
- ⚡ Real-time quota updates without needing to refresh the page

## Tech Stack

### Backend

- **Framework**: FastAPI
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Clerk Backend API
- **AI**: Deepseek API for dynamic content generation
- **API Documentation**: OpenAPI/Swagger UI

### Frontend

- **Framework**: React (with Vite)
- **Styling**: Custom CSS with a modern, responsive design
- **Routing**: React Router
- **API Communication**: `fetch` API with `useApi` hook for authenticated requests

## Prerequisites

- Python 3.10+
- Node.js 18+
- `npm` or `yarn`
- A Deepseek API Key
- A Clerk Account with API Keys

## Getting Started

### Backend Setup

1.  **Navigate to the backend directory**:
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables**:
    Create a `.env` file in the `backend/src` directory and add your secret keys:
    ```
    CLERK_SECRET_KEY=your_clerk_secret_key
    DEEPSEEK_API_KEY=your_deepseek_api_key
    ```

5.  **Run the development server**:
    ```bash
    uvicorn src.app:app --reload
    ```
    The backend will be available at `http://localhost:8000`.

### Frontend Setup

1.  **Navigate to the frontend directory**:
    ```bash
    cd frontend
    ```

2.  **Install dependencies**:
    ```bash
    npm install
    ```

3.  **Configure environment variables**:
    Create a `.env` file in the `frontend` directory and add your Clerk publishable key:
    ```
    VITE_CLERK_PUBLISHABLE_KEY=your_clerk_publishable_key
    ```

4.  **Run the development server**:
    ```bash
    npm run dev
    ```
    The frontend will be available at `http://localhost:5173`.

## Deployment

This project can be easily deployed to Vercel.

1.  **Push your code to a GitHub repository**.
2.  **Import the repository on Vercel**.
3.  **Configure the project**:
    -   Set the **Framework Preset** to `Vite`.
    -   Set the **Root Directory** to `frontend`.
4.  **Add Environment Variables**:
    In the Vercel project settings, add your `DEEPSEEK_API_KEY`, `CLERK_SECRET_KEY`, and `VITE_CLERK_PUBLISHABLE_KEY`.
5.  **Deploy**! Vercel will handle the rest.

## Project Structure

```
ai-code-challenger/
├── backend/                    # Backend server
│   ├── src/
│   │   ├── database/          # Database models and operations
│   │   ├── routes/             # API routes
│   │   ├── utils/              # Utility functions
│   │   ├── app.py              # FastAPI application
│   │   └── config.py           # Configuration settings
│   └── pyproject.toml          # Python dependencies
├── frontend/                   # Frontend React application
│   ├── public/
│   ├── src/
│   │   ├── components/        # Reusable components
│   │   ├── context/           # React context providers
│   │   ├── hooks/             # Custom React hooks
│   │   └── utils/             # Utility functions
│   └── package.json
└── README.md                   # This file
```

## API Endpoints

### Authentication

- `POST /api/authenticate` - Authenticate user

### Challenges

- `POST /api/generate-challenge` - Generate a new coding challenge
- `GET /api/my-history` - Get user's challenge history
- `GET /api/quota` - Get user's current quota information

## Environment Variables

### Backend

- `OPENAI_API_KEY`: Your OpenAI API key
- `CLERK_SECRET_KEY`: Clerk secret key for backend authentication
- `JWT_KEY`: Secret key for JWT token signing
- `CLERK_WEBHOOK_SECRET`: Secret for verifying Clerk webhook signatures

### Frontend

- `VITE_CLERK_PUBLISHABLE_KEY`: Your Clerk publishable key
- `VITE_API_URL`: Base URL for API requests

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Ian Mworia - ianmworia156@gmail.com / ianmworia.dev

Project Link: [https://github.com/Mworia-Ian/ai-code-challenger](https://github.com/Mworia-Ian/ai-code-challenger)

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://reactjs.org/)
- [Clerk](https://clerk.dev/)
- [OpenAI](https://openai.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

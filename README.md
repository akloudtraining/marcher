# Marcher - Freelance Marketplace Platform

Marcher is a modern freelance marketplace platform that connects talented professionals with businesses and individuals seeking their services.

## Features

- User authentication (Freelancers and Clients)
- Project posting and bidding system
- Advanced search and filtering
- Secure messaging system
- Payment integration
- Rating and review system
- Profile management
- Project milestone tracking

## Tech Stack

- Frontend: React.js with TypeScript
- Backend: Python FastAPI
- Database: PostgreSQL
- Authentication: JWT
- Real-time messaging: WebSocket
- File Storage: AWS S3
- Payment Processing: Stripe

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Python (3.9 or higher)
- PostgreSQL
- Docker (optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/marcher.git
cd marcher
```

2. Set up the backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up the frontend:
```bash
cd frontend
npm install
```

4. Start the development servers:

Backend:
```bash
cd backend
uvicorn main:app --reload
```

Frontend:
```bash
cd frontend
npm run dev
```

5. Visit http://localhost:3000 to see the application

## Environment Variables

Create a `.env` file in both frontend and backend directories with the following variables:

Backend:
```
DATABASE_URL=postgresql://user:password@localhost:5432/marcher
JWT_SECRET=your_jwt_secret
STRIPE_SECRET_KEY=your_stripe_secret_key
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_BUCKET_NAME=your_bucket_name
```

Frontend:
```
VITE_API_URL=http://localhost:8000
VITE_STRIPE_PUBLIC_KEY=your_stripe_public_key
```

## License

MIT License

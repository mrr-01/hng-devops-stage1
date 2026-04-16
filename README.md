# hng-devops-stage1
Personal API Deployment
# Personal API

A simple REST API built with FastAPI for DevOps training. This API provides three endpoints for testing and personal information.

## Local Development

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/personal-api.git
cd personal-api
```
2. Create virtual environment:

bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

    Install dependencies:

bash

pip install -r requirements.txt

    Run the application:

bash

python app.py

The API will be available at http://localhost:8000
API Endpoints
GET /

Returns a simple status message.

Response:
json

{
  "message": "API is running"
}

Status Code: 200
Content-Type: application/json
GET /health

Health check endpoint.

Response:
json

{
  "message": "healthy"
}

Status Code: 200
Content-Type: application/json
GET /me

Returns personal information.

Response:
json

{
  "name": "Your Full Name",
  "email": "you@example.com",
  "github": "https://github.com/yourusername"
}

Status Code: 200
Content-Type: application/json

#Deployment URL
https://mrrhng.mooo.com

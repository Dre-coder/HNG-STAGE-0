# HNG-STAGE-0

## Description
This project is a simple FastAPI application that provides a single endpoint to return user information along with the current date and time in ISO 8601 format (UTC).

## Setup Instructions
To run this project locally, follow the following steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/Dre-coder/HNG-STAGE-0.git
    cd HNG-STAGE-0
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    source .venv\Scripts\activate  
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the FastAPI application:
    ```sh
    uvicorn main:app --reload
    ```

## API Documentation

### Endpoint URL
- `GET /`


### Request/Response Format

    ```json
    {
        "email": "oshoayomide03@gmail.com",
        "current_datetime": "2023-10-05T14:48:00Z",
        "github_url": "https://github.com/Dre-coder/HNG-STAGE-0"
    }
    ```
## backlink
[https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

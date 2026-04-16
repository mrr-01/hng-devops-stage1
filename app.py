from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Personal API", description="My DevOps Stage 1 API")


@app.get("/")
async def root():
    "Root Endpoints"
    return JSONResponse(status_code=200, content={"Message": "API is running"})


@app.get("/health")
async def health_check():
    """Health End Point Check"""
    return JSONResponse(status_code=200, content={"Message": "Healthy"})


@app.get("/me")
async def get_me():
    """Personal Information Endpoint"""
    return JSONResponse(
        status_code=200,
        content={
            "Name": "Victor Joseph",
            "Email": "joevictor025@gmail.com",
            "github": "https://github.com/mrr-01",
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

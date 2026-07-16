from fastapi import FastAPI
import os

app = FastAPI(title="Morning API for Render")

@app.get("/")
def read_root():
    return {"message": "Morning"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/info")
def get_info():
    return {
        "app_name": "Morning API",
        "version": "1.0.0",
        "description": "A simple FastAPI application deployed on Render",
        "environment": "production" if os.environ.get("RENDER") == "true" else "local"
    }

if __name__ == "__main__":
    import uvicorn
    # Render sets the PORT environment variable
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

import uvicorn
from Main.config import settings

if __name__ == "__main__":
    uvicorn.run(settings.APP_NAME, reload=True, port=9000)
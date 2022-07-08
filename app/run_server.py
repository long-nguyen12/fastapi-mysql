from controller import accelerometer_controller
from fastapi import FastAPI
import uvicorn
from database.database import engine, SessionLocal
from database import models
models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Accelerometer for Ha"
    }


app.include_router(accelerometer_controller.control_accelerometer)

if __name__ == "__main__":
    uvicorn.run("run_server:app", host="0.0.0.0", port=8000, reload=True)

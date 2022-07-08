from decimal import Decimal
import os
from ossaudiodev import control_labels
from fastapi import Request, Response, Body, APIRouter, File, UploadFile, Depends
from database.models import *
import time
from typing import Union
from tempfile import NamedTemporaryFile
from datetime import date, datetime
from sqlalchemy.orm import Session
from database.database import SessionLocal
control_accelerometer = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@control_accelerometer.post("/data")
async def post_file(file: Union[UploadFile, None] = None, sess: Session = Depends(get_db)):
    if not file:
        return {"message": "No upload file sent"}
    else:
        contents = await file.read()

        file_copy = NamedTemporaryFile(delete=False)
        try:
            file_copy.write(contents)
            file_copy.seek(0)
            with open(file_copy.name) as f:
                data = f.readlines()
                for line in data:
                    arr = line.split(" ")
                    x = Decimal(arr[0])
                    y = Decimal(arr[1])
                    z = Decimal(arr[2])
                    timestamp = datetime.strptime(arr[3].strip(), "%Y-%m-%d")
                    accelerometer = Accelerometer(
                        x=x, y=y, z=z, timestamp=timestamp)
                    sess.add(accelerometer)
                    sess.commit()
                    sess.refresh(accelerometer)

        finally:
            file_copy.close()
            os.unlink(file_copy.name)

        return {"filename": file.filename}


@control_accelerometer.get("/data")
async def get_file():
    return {"msg": "Success"}

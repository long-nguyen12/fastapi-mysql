from sqlalchemy import Column, Integer, DECIMAL, Date
from database.database import Base


class Accelerometer(Base):
    __tablename__ = "accelerometers"

    id = Column(Integer, primary_key=True, index=True)
    x = Column(DECIMAL)
    y = Column(DECIMAL)
    z = Column(DECIMAL)
    timestamp = Column(Date)

from datetime import date, datetime
from decimal import Decimal
import time
from pydantic import BaseModel, Optional, validator


class Accelerometer(BaseModel):
    id = Optional[int]
    x = Optional[Decimal]
    y = Optional[Decimal]
    z = Optional[Decimal]
    timestamp = Optional[datetime]

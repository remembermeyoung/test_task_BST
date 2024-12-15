from typing import Annotated
from pydantic import Field, BaseModel
from datetime import datetime as date


model_or_version = Annotated[str, Field(pattern=r'^[A-Z]{1}[0-9]{1}$')]


class RobotJSON(BaseModel):
    model: model_or_version
    version: model_or_version
    created: date

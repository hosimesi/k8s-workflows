from pydantic import BaseModel, Field


class Args(BaseModel):
    file_id: str = Field(alias="id")
    file_path: str = Field(alias="path")
    file_type: str = Field(alias="type")

from pydantic import BaseModel

class GoogleToken(BaseModel):
    token_id: str

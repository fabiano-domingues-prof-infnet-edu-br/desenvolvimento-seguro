import html
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, validator

app = FastAPI()

class UserInput(BaseModel):
    first_name: str = Field(..., regex=r"^[a-zA-Z ]*$")
    last_name: str = Field(..., regex=r"^[a-zA-Z ]*$")
    email: EmailStr
    phone: str = Field(..., regex=r"^[0-9\-\(\)]*$")
    address: str = Field(..., min_length=6)

    class Config:
        anystr_strip_whitespace = True
    @validator("*", pre=True)
    def sanitize_html_and_slashes(cls, v):
        if isinstance(v, str):
            v = v.replace("\\", "")
            v = html.escape(v)
        return v

@app.post("/process")
async def process_form(user: UserInput):
    return {
        "message": "Input is valid. Processing...",
        "data": user
    }
import html
from fastapi import FastAPI
from pydantic import BaseModel, Field, validator

app = FastAPI()

class ReviewInput(BaseModel):
    review_content: str = Field(..., min_length=10)

    class Config:
        anystr_strip_whitespace = True

    @validator("*", pre=True)
    def sanitize_html_and_slashes(cls, v):
        if isinstance(v, str):
            v = v.replace("\\", "")
            v = html.escape(v)
        return v

@app.post("/submit-review")
async def process_review(review: ReviewInput):
    return {
        "message": "Review is valid. Processing...",
        "data": review
    }
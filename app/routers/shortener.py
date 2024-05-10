from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
import random
import string
from fastapi.responses import RedirectResponse

from app.db.urls import get_db
from app.models.url import URL

router = APIRouter()


def get_random_string(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@router.post("/shorten/")
def shorten_url(request: Request, original_url: str, db: Session = Depends(get_db)):
    short_url = get_random_string()
    while db.query(URL).filter(URL.short_url == short_url).first():
        short_url = get_random_string()
    db.add(URL(short_url=short_url, original_url=original_url))
    db.commit()
    return {"short_url": f"{request.url.scheme}://{request.url.netloc}/{short_url}"}


@router.get("/{short_url}")
def redirect_short_url(short_url: str, db: Session = Depends(get_db)):
    url = db.query(URL.original_url).filter(URL.short_url == short_url).first()
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url.original_url)
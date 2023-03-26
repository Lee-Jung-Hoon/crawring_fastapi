from typing import Optional
from fastapi import FastAPI
from crawring_util import start_crawring

app = FastAPI()

@app.get("/items")
def read_item(
        txtTrlNo01: Optional[int] = None,
        txtTrlNo02: Optional[int] = None,
        txtTrlNo03: Optional[int] = None,
        txtTrlNo04: Optional[str] = None):
    
    result = start_crawring()
    return {result}
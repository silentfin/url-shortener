from fastapi import FastAPI
from pydantic import BaseModel
import random
import string

LOWER_ASCII_CHARACTERS = string.ascii_lowercase
UPPER_ASCII_CHARACTERS = string.ascii_uppercase
DIGITS = string.digits

app=FastAPI()

def generate_short_code():
    short_code=""
    for _ in range(5):
        short_code+=random.choice(LOWER_ASCII_CHARACTERS+UPPER_ASCII_CHARACTERS+DIGITS)
    return short_code


all_urls={"test":"hero"}

class Link(BaseModel):
    url: str

@app.get("/")
def read_root():
    return all_urls

@app.get("/url/{short_code}")
async def print_url(short_code: str):
    return all_urls[short_code]

@app.post("/url/")
async def post_url(long_url: Link):
    print(f"{long_url.url} is recieved!!!")
    short_code=generate_short_code()
    all_urls[short_code]=long_url.url
    return long_url
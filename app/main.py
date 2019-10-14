#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title="FastAPI Mangum Example", version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app)


@app.get('/', name='Hello World', tags=['Hello'])
def hello_world():
    return {"Hello": "Python"}


if __name__ == '__main__':
    uvicorn.run(app)

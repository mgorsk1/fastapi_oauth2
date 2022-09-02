import jwt
from fastapi import FastAPI, Request, Response, status, HTTPException

from app.models.user import User

app = FastAPI()


def parse_token(token):
    return jwt.decode(token, options={"verify_signature": False}, algorithms=['RS256'])


@app.get("/")
async def root(response: Response):
    response.status_code = status.HTTP_200_OK

    return {"message": "Hello World, I am a stranger."}


@app.get("/me", response_model=User)
async def me(request: Request, response: Response):
    try:
        token = request.headers['x-forwarded-access-token']

        data = parse_token(token)

        response.status_code = status.HTTP_200_OK
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing access token.")

    return User(**data)

from fastapi import FastAPI
from jwt_util import JwtUtil
import httpx
import asyncio
import config

app = FastAPI()

@app.post("/hook/")
async def test_hook(status: int, uuid):
  if status >= config.confirmations:
    async with httpx.AsyncClient() as client:
      token = JwtUtil.gen_jwt()
      headers = {
        'Authorization': 'Ghost {}'.format(token),
        'Accept-Version': 'v5.0',
        'Content-Type': 'application/json'
      }
      data = {"members": [{"email": "test1@ghost.org"}]}
      r = await client.post("{}/ghost/api/admin/members/".format(config.api_url), json=data, headers=headers)
      return r.json()
  return {}
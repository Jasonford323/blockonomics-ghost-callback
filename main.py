from fastapi import FastAPI
from jwt_util import JwtUtil
import httpx
import asyncio
import config

app = FastAPI()

async def fetch_merchant_order(client, uuid):
  headers = {
    'Authorization': 'Bearer {}'.format(config.blockonomics_api_key),
    'Content-Type': 'application/json'
  }
  r = await client.get('{}{}'.format(config.BLOCKONOMICS_MERCHANT_ORDER_URL, uuid), headers=headers)
  merchant_data = r.json().get('data')
  return merchant_data.get('emailid'), merchant_data.get('Custom Field1')

@app.get("/hook/")
async def hook(status: int, uuid):
  if status >= config.confirmations:
    async with httpx.AsyncClient() as client:
      customer_email, ghost_url = await fetch_merchant_order(client, uuid)
      token = JwtUtil.gen_jwt()
      headers = {
        'Authorization': 'Ghost {}'.format(token),
        'Accept-Version': 'v5.0',
        'Content-Type': 'application/json'
      }
      data = {"members": [{"email": customer_email}]}
      r = await client.post("{}/ghost/api/admin/members/".format(ghost_url), json=data, headers=headers)
      return r.json()
  return {}
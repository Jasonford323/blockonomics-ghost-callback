import jwt
import config
from datetime import datetime as date

class JwtUtil():

  @staticmethod
  def gen_jwt(ghost_admin_api_key):
    # Create JWT token from Ghost Admin API key
    kid, secret = ghost_admin_api_key.split(':')

    iat = int(date.now().timestamp())
    header = {'alg': 'HS256', 'typ': 'JWT', 'kid': kid}
    payload = {
        'iat': iat,
        'exp': iat + 5 * 60,
        'aud': '/admin/'
    }

    token = jwt.encode(payload, bytes.fromhex(secret), algorithm='HS256', headers=header)
    return token.decode('UTF-8')
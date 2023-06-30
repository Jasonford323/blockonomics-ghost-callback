# Blockonomics Ghost callback

A small callback server to receive webhooks from Blockonomics and to send Admin API calls to Ghost blogs.

## Tech Stack

* Python 3.7+
* FastAPI as async web framework, will handle incoming webhook calls
* HTTPX will handle sending out callbacks asynchronously
* PyJWT for generating JWT tokens needed to call Ghost Admin API
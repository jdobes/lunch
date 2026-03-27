import logging
import os
import time

import httpx
from fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LUNCH_API = os.getenv("LUNCH_API", "http://lunch:8000")
OPENAPI_SPEC = f"{LUNCH_API}/api/openapi.json"

# Wait for the API to be ready and load OpenAPI spec
logger.info(f"Connecting to Lunch API at {LUNCH_API}")
while True:
    try:
        response = httpx.get(OPENAPI_SPEC)
        response.raise_for_status()
        openapi_spec = response.json()
        break
    except (httpx.HTTPError, httpx.ConnectError) as e:
        logger.info(f"Waiting for Lunch API to be ready at {OPENAPI_SPEC}...")
        time.sleep(1)

# Create an HTTP client for your API
client = httpx.AsyncClient(base_url=LUNCH_API)

# Create the MCP server
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="Lunch API"
)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=9000)

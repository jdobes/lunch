import json
import logging
import os
import re

import requests

FACEBOOK_COOKIE = os.getenv("FACEBOOK_COOKIE", "")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_access_token(session: requests.Session) -> str:
    response = session.get('https://business.facebook.com/business_locations', headers={'cookie': FACEBOOK_COOKIE})
    if response.status_code == 200:
        search_token = re.search(r"(EAAG\w+)", response.text)
        if search_token and search_token.group(1): 
            return search_token.group(1)
        else:
            logger.warning(f"Access token not found!")
    else:
        logger.warning(f"Invalid HTTP return code: {response.status_code}")
    return ""


def get_endpoint(session: requests.Session, page_id: str) -> str:
    access_token = get_access_token(session)
    fields = "id,created_time,full_picture,message"
    if access_token:
        endpoint = f"https://graph.facebook.com/v25.0/{page_id}/feed?limit=10&fields={fields}&access_token={access_token}"
    else:
        endpoint = ""
    return endpoint


def get_page_posts(page_id: str) -> list:
    with requests.Session() as session:
        endpoint = get_endpoint(session, page_id)
        if not endpoint:
            return []
        response = session.get(endpoint, headers={'cookie': FACEBOOK_COOKIE})
        if response.status_code == 200:
            response = json.loads(response.text)
            return response.get("data", [])
        logger.warning(f"Invalid HTTP return code: {response.status_code}")
        return []

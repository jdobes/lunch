# Lunch

## Components

- **API** - Python app running on port 8000
- **Web** - React app, served by the Python webserver

## Build and run

```bash
# Build React app assets first
./build_web.sh
podman build -t localhost/jdobes/lunch:latest .
podman run --rm -p 8000:8000 localhost/jdobes/lunch:latest
```

## Using

- **Main page** - http://localhost:8000/
- **Swagger UI for API** - http://localhost:8000/api/

## Frontend Development

```bash
# Re-install dependencies and re-generate lock file
rm -rf node_modules package-lock.json
npm install
# Run the API
podman run --rm -p 8000:8000 localhost/jdobes/lunch:latest
# Start node devel server
npm start
```

## Adding a restaurant

1. Add `<new_restaurant_name>.py` with the following contents into `api/restaurants`

```py
# -*- coding: utf-8 -*-
from .utils import fetch_menicka, parse_menicka

NAME = "<Restaurant Name>"
URL = "<url>" # will be linked to by "Menu link"
RESTAURANT_ID = "1337"
GPS = (49.23081293334384, 16.577047939793758)


def parse_menu():
  menicka_html = fetch_menicka(RESTAURANT_ID)
  return parse_menicka(menicka_html)
```

2. Enable your restaurant in `Containerfile` by adding `<new_restaurant_name>` to ENV

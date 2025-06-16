# Lunch

## Components
- **API** - Python app running on port 8000
- **Web** - React app, served by the Python webserver

## Build and run

    # Build React app assets first
    ./build_web.sh
    podman build -t localhost/jdobes/lunch:latest .
    podman run --rm -p 8000:8000 localhost/jdobes/lunch:latest

## Using

- **Main page** - http://localhost:8000/
- **Swagger UI for API** - http://localhost:8000/api/

## Frontend Development

    podman run --rm -p 8000:8000 localhost/jdobes/lunch:latest
    npm start

# Lunch

## Components
- **API** - Python app running on port 8001
- **Web** - React app running on port 8000, contains a proxy to re-direct /api requests to **API** container

## Build and run

    # Build React app assets first
    ./build_web.sh
    docker-compose up --build

## Using

- **Main page** - http://localhost:8000/
- **Swagger UI for API** - http://localhost:8000/api/

## Frontend Development

    docker-compose up -d lunch-api
    npm start

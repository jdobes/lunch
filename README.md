# Lunch

## Components
- **API** - Python app running on port 8000
- **Web** - React app, served by the Python webserver

## Build and run

    # Build React app assets first
    ./build_web.sh
    docker-compose up --build

## Using

- **Main page** - http://localhost:8000/
- **Swagger UI for API** - http://localhost:8000/api/

## Frontend Development

    docker-compose up -d
    npm start

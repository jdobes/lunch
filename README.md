    Components:
    - API - Python app running on port 8001
    - Web - React app running on port 8002
    - Proxy - Nginx proxy running on port 8000 (Not needed in prod-like envs)

    Build and run:
    docker-compose up --build

    Test:
    Main page: http://localhost:8000/
    Swagger UI: http://localhost:8000/api/

    Frontend Development:
    docker-compose start lunch-api
    npm start

    Release:
    docker buildx build -f ./api/Dockerfile --platform linux/amd64,linux/arm64 --push -t jdobes/lunch_api:latest -t jdobes/lunch_api:0.1 .
    docker buildx build -f ./web/Dockerfile --platform linux/amd64,linux/arm64 --push -t jdobes/lunch_web:latest -t jdobes/lunch_web:0.1 .

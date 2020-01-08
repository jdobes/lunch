    Build:
    podman build -t lunch_api -f api/Dockerfile .
    podman build -t lunch_web -f web/Dockerfile .

    Run:
    podman run --rm -p 8001:8000 -e ZOMATO_API_KEY= --name lunch_api lunch_api
    podman run -it --rm -p 8002:8000 --name lunch_web lunch_web

    Test:
    Main page: http://localhost:8002/
    Swagger UI: http://localhost:8001/api/

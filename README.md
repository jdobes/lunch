    Build:
    podman build -t lunch_api -f api/Dockerfile .
    podman build -t lunch_web -f web/Dockerfile .
    podman build -t lunch_proxy -f proxy/Dockerfile .

    Run:
    podman pod create -n lunch -p 8000:8000
    podman run --pod lunch --rm -e ZOMATO_API_KEY= --name lunch_api lunch_api
    podman run --pod lunch -it --rm --name lunch_web lunch_web
    podman run --pod lunch -it --rm --name lunch_proxy lunch_proxy
    podman pod stop lunch
    podman pod rm lunch

    Release:
    podman build -t registry.owny.cz/lunch/lunch_api -f api/Dockerfile .
    podman build -t registry.owny.cz/lunch/lunch_web -f web/Dockerfile .
    podman push registry.owny.cz/lunch/lunch_api
    podman push registry.owny.cz/lunch/lunch_web

    Test:
    Main page: http://localhost:8000/
    Swagger UI: http://localhost:8000/api/

podman build -t lunch .

podman run --rm -p 8000:8000 -e ZOMATO_API_KEY= --name lunch lunch

Main page: http://localhost:8000/
Swagger UI: http://localhost:8000/api/

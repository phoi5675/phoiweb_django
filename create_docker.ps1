# Stop docker container.
docker stop django
docker rm django
# Recreate image.
docker build --rm -f dockerfiles/Dockerfile --tag django .
# Run dockeer container.
docker run -d -p 8000:8000 --restart=always --name django django
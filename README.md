# phoiweb_django

django for phoiweb

# how to run

- create image
  
  ```shell
  docker build --rm -f dockerfiles/Dockerfile --tag django .
  ```
- run docker container

  ```shell
  docker run -d -p 8000:8000 --restart=always --name django django
  ```

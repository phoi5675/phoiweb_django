# phoiweb_django

django for phoiweb

# how to run

- create image
  
  ```shell
  docker build --rm -f dockerfiles/Dockerfile --tag django .
  ```
- run docker container(windows)

  ```shell
  docker run -d -p 8000:8000 --restart=always -v "$((Get-Item -Path '.\' -Verbose).FullName)\django:/django" --name django django
  ```

- If you run dockerfile first time, uncomment
  ```
  # RUN python3 manage.py collectstatic
  ```
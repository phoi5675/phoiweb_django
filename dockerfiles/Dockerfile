FROM python

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
            postgresql-client \
	        && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
	&& apt-get install -y \
	 vim

COPY requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR /django
COPY ./django .

# RUN python3 manage.py collectstatic

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
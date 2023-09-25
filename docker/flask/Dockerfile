# Author: Sakthi Santhosh
# Created on: 25/09/2023
FROM python:3.11-alpine AS build

COPY ./requirements.txt ./

RUN pip3 install -q -r ./requirements.txt

FROM python:3.11-alpine AS final

WORKDIR /app/

COPY ./ ./
COPY --from=build /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=build /usr/local/bin/ /usr/local/bin/

EXPOSE 8000/tcp

ENTRYPOINT gunicorn --bind 0.0.0.0:8000 --workers 4 "app:app_handle"

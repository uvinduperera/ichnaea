FROM python:2.7
WORKDIR /app
RUN groupadd -g 10001 app && useradd -d /app -g 10001 -G app -M  -s /bin/sh -u 10001 app
COPY . ./
RUN apt-get update && apt-get -y install libspatialindex-dev libgeos-dev
RUN virtualenv --no-site-packages .
RUN make release && chown -R app:app /app

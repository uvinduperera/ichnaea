FROM python:2.7
WORKDIR /app
COPY . ./
RUN apt-get update && apt-get -y install libspatialindex-dev libgeos-dev
RUN virtualenv --no-site-packages .
RUN make release

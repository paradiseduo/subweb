FROM alpine:latest
COPY . /subweb
WORKDIR /subweb
RUN apk add --no-cache python3-dev  \
    && pip3 install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt
EXPOSE 10086 10010
CMD [ "/subweb/docker.sh"]
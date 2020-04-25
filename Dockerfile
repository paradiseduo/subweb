FROM alpine:latest
COPY . /subweb
WORKDIR /subweb
RUN apk add --no-cache python3-dev  \
    && pip3 install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt\
    && chmod 777 /subweb/config/subconverter \
    && chmod 777 /subweb/docker.sh
EXPOSE 10086 10010
CMD [ "/subweb/docker.sh"]
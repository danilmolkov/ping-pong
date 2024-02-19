FROM ubuntu:latest

LABEL version="1.0"
LABEL maintaner="Daniel Molkov"
LABEL promoted="true"

RUN apt update && apt install net-tools -y && apt install curl -y

RUN echo 'ping localhost &' > /bootstrap.sh
RUN echo 'sleep infinity' >> /bootstrap.sh
RUN chmod +x /bootstrap.sh

ENTRYPOINT [ "/bin/sh", "-c", "while :; do sleep 5; done" ]
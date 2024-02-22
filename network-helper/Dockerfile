FROM ubuntu:latest

LABEL version="1.0"
LABEL maintaner="Daniel Molkov"
LABEL promoted="true"

RUN TOOLS="net-tools curl python3 pip dnsutils iputils-ping" && \
    apt update && apt install $TOOLS -y

RUN --mount=type=bind,source=test/requirements.txt,target=requirements.txt \
    pip install -r requirements.txt

RUN echo 'ping localhost &' > /bootstrap.sh
RUN echo 'sleep infinity' >> /bootstrap.sh
RUN chmod +x /bootstrap.sh

COPY test/test.py test.py

ENTRYPOINT [ "/bin/sh", "-c", "while :; do sleep 5; done" ]
FROM golang as builder
WORKDIR /app

COPY server.go .
RUN go build -o server server.go

FROM debian

RUN apt update && \
    apt install -y xvfb libgtk-3-dev libwebkit2gtk-4.0-dev libwebkit2gtk-4.1-dev dbus-x11 curl wget && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*

COPY --from=builder /app/server /server

COPY app /
RUN echo 'PUCTF24{fake_flag}' > /flag.txt
RUN chmod 555 /server /app /flag.txt
RUN rm -rf /tmp/*

RUN useradd bot --create-home && chown -R bot:bot /tmp
USER bot

WORKDIR /tmp
ENV DISPLAY :333
CMD ["sh","-c","Xvfb :333 -screen 0 640x400x8 -nolisten tcp & /server"]

FROM alpine
RUN apk add sed bash curl coreutils busybox-extras
COPY index.cgi /www/cgi-bin/index.cgi
RUN chmod 700 /www/cgi-bin/index.cgi
CMD httpd -h/www -p$PORT -f

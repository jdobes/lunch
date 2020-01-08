FROM registry.access.redhat.com/ubi8/ubi-minimal

RUN microdnf install nginx && microdnf clean all && \
    sed -i -e 's/80 default_server;/8000 default_server;/g' \
           -e 's/pid \/run\/nginx.pid;/pid \/tmp\/nginx.pid;/' \
           -e 's/user nginx;/#user nginx;/' \
           -e 's/error_log \/var\/log\/nginx\/error.log;/error_log \/dev\/stderr;/' \
           -e 's/access_log  \/var\/log\/nginx\/access.log  main;/access_log  \/dev\/stdout main;/' \
    /etc/nginx/nginx.conf

ADD web/*.json /web-build/
ADD web/public/ /web-build/public/
ADD web/src/ /web-build/src/

RUN microdnf install npm && \
    cd /web-build && npm ci && npm run build && \
    mv build/* /usr/share/nginx/html/ && cd / && rm -rf web-build && rm -rf /root/.npm && \
    microdnf remove nodejs npm && microdnf clean all

USER nginx

EXPOSE 8000

CMD ["nginx", "-g", "daemon off;"]

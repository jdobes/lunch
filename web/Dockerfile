FROM centos:8

RUN dnf -y install nginx && dnf clean all && \
    sed -i -e 's/80 default_server;/8000 default_server;/g' -e 's/pid \/run\/nginx.pid;/pid \/tmp\/nginx.pid;/' \
           -e 's/user nginx;/#user nginx;/' -e 's/error_log \/var\/log\/nginx\/error.log;/error_log \/dev\/stdout;/' \
           -e 's/access_log  \/var\/log\/nginx\/access.log  main;/access_log  \/dev\/stdout main;/' /etc/nginx/nginx.conf

ADD web/*.json /web-build/
ADD web/public/ /web-build/public/
ADD web/src/ /web-build/src/

RUN dnf -y install npm && \
    cd /web-build && npm install && npm run build && \
    mv build/* /usr/share/nginx/html/ && cd / && rm -rf web-build && rm -rf /root/.npm && \
    dnf -y remove npm && dnf clean all

USER nginx

EXPOSE 8000

CMD ["nginx", "-g", "daemon off;"]

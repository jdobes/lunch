FROM registry.access.redhat.com/ubi8/ubi-minimal

RUN microdnf install nginx && microdnf clean all && \
    sed -i -e 's/80 default_server;/8002 default_server;/g' \
           -e 's/pid \/run\/nginx.pid;/pid \/tmp\/nginx.pid;/' \
           -e 's/user nginx;/#user nginx;/' \
           -e 's/error_log \/var\/log\/nginx\/error.log;/error_log \/dev\/stderr;/' \
           -e 's/access_log  \/var\/log\/nginx\/access.log  main;/access_log  \/dev\/stdout main;/' \
    /etc/nginx/nginx.conf

ADD web/*.json /web-build/
ADD web/public/ /web-build/public/
ADD web/src/ /web-build/src/

RUN microdnf module enable nodejs:18 && \
    microdnf install npm python2 make gcc-c++ && \
    cd /web-build && npm ci && npm run build && \
    mv build/* /usr/share/nginx/html/ && cd / && rm -rf web-build && rm -rf /root/.npm && rm -rf /root/.node-gyp && \
    microdnf remove binutils cpp gcc gcc-c++ gdbm glibc-devel glibc-headers isl kernel-headers libgomp libmpc libpkgconf \
                    libstdc++-devel libxcrypt-devel make nodejs npm pkgconf pkgconf-m4 pkgconf-pkg-config \
                    python2 python2-libs python2-pip python2-pip-wheel python2-setuptools python2-setuptools-wheel \
                    nodejs-full-i18n && \
    microdnf clean all

USER nginx

EXPOSE 8002

CMD ["nginx", "-g", "daemon off;"]

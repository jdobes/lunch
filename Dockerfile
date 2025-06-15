FROM registry.access.redhat.com/ubi10/ubi-minimal

ADD api/*.txt /lunch/

RUN microdnf -y install python3 nginx \
        libxml2-devel libxslt-devel \
        python3-devel poppler-utils && \
    microdnf clean all && \
    pip3 install --no-cache-dir -r /lunch/requirements.txt

ENV TZ="Europe/Prague"
ENV API_HOST="localhost"

# apscheduler fix
RUN echo "Europe/Prague" > /etc/timezone

ADD entrypoint.sh         /

ADD api/*.py              /lunch/
ADD api/*.yml             /lunch/
ADD api/restaurants/*.py  /lunch/restaurants/

# Web must be built first using build_web.sh
ADD web/build/*           /usr/share/nginx/html/
ADD web/build/static/js/* /usr/share/nginx/html/static/js/
ADD web/nginx.conf        /etc/nginx/nginx.conf

RUN chown -R nginx:nginx /usr/share/nginx/html

ENV ENABLED_RESTAURANTS=asport,bistro22,cookpoint,kancl,qwerty,alvin,moravia,portoriko,kanas_restaurant,kanas_jidelna,nepal,royalnepal,purkynka,velorex,kotelna,padthai,3opice,sesamo,jeanpauls,rubin,poupe,charlies_square,u_3_certu_starobrnenska,padowetz,statl,tusto,sportpub

FROM registry.access.redhat.com/ubi8/ubi-minimal

ADD api/*.txt /lunch/

RUN microdnf module enable nginx:1.22 && \
    microdnf install sqlite python39 shadow-utils \
                     libxml2-devel libxslt-devel gcc \
                     python39-devel nginx poppler-utils \
                     gtk3 alsa-lib libX11-xcb && \
    microdnf clean all && \
    pip3 install --no-cache-dir -r /lunch/requirements.txt && \
    playwright install firefox

ENV PLAYWRIGHT_PROXY=""
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

ENV ENABLED_RESTAURANTS=asport,bistro22,cookpoint,kancl,qwerty,alvin,moravia,portoriko,kanas_restaurant,kanas_jidelna,vitalite,nepal,royalnepal,purkynka,velorex,kotelna,padthai,3opice,spravnemisto,sesamo,jeanpauls,rubin

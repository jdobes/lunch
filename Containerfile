FROM registry.access.redhat.com/ubi10/ubi-minimal:10.2-1786323476@sha256:e6c7c01447dc8eadf2a673e65fb6c607f16e168fe29a776fb937004f33c81cc0

ADD api/*.txt /lunch/

RUN microdnf -y install python3 python3-devel libxml2-devel libxslt-devel poppler-utils && \
    microdnf clean all && \
    pip3 install --no-cache-dir -r /lunch/requirements.txt

ENV TZ="Europe/Prague"

# apscheduler fix
RUN echo "Europe/Prague" > /etc/timezone

ADD api/*.py              /lunch/
ADD api/*.yml             /lunch/
ADD api/restaurants/*.py  /lunch/restaurants/

# Web must be built first using build_web.sh
ADD web/build/*           /lunch/html/
ADD web/build/static/js/* /lunch/html/static/js/

ENV ENABLED_RESTAURANTS=asport,bistro22,cookpoint,kancl,qwerty,alvin,moravia,portoriko,charlies_park,jidelna_sto_chuti,nepal,royalnepal,purkynka,primesteak,k2,kotelna,padthai,3opice,sesamo,jeanpauls,rubin,poupe,charlies_square,u_3_certu_starobrnenska,padowetz,sindelar,statl,tusto,sportpub

ENTRYPOINT ["python3", "-m", "lunch.lunch"]

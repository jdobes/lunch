FROM registry.access.redhat.com/ubi10/ubi-minimal:10.2-1786398535@sha256:1e429ea364534f7baf494bac5cc54996b9b9d300f1da90e7b1dfa0ce455bfe39

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

FROM centos:8

ADD api/* /lunch/
ADD api/restaurants/* /lunch/restaurants/

RUN dnf -y install sqlite python3 && dnf clean all && \
    pip3 install -r /lunch/requirements.txt && \
    rm -rf /root/.cache

RUN adduser --gid 0 -d /lunch --no-create-home -c 'Lunch user' lunch
USER lunch

EXPOSE 8000

ENV ENABLED_RESTAURANTS=asport,portoriko,nepal,purkynka,liquidbread,tasteofindia,kotelna,padthai,velorex,3opice

CMD python3 -m lunch.lunch

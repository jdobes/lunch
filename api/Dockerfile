FROM registry.access.redhat.com/ubi8/ubi-minimal

ADD api/*.txt /lunch/

RUN microdnf install sqlite python3 shadow-utils && microdnf clean all && \
    pip3 install -r /lunch/requirements.txt && \
    rm -rf /root/.cache

# apscheduler fix
RUN echo "UTC" > /etc/timezone

RUN adduser --gid 0 -d /lunch --no-create-home -c 'Lunch user' lunch

ADD api/*.py /lunch/
ADD api/*.yml /lunch/
ADD api/restaurants/*.py /lunch/restaurants/

USER lunch

EXPOSE 8001

ENV ENABLED_RESTAURANTS=asport,portoriko,nepal,purkynka,liquidbread,tasteofindia,kotelna,padthai,velorex,3opice

CMD python3 -m lunch.lunch

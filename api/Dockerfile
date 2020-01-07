FROM registry.access.redhat.com/ubi8/ubi-minimal

ADD api/* /lunch/
ADD api/restaurants/* /lunch/restaurants/

RUN microdnf install sqlite python3 shadow-utils && microdnf clean all && \
    pip3 install -r /lunch/requirements.txt && \
    rm -rf /root/.cache

# apscheduler fix
RUN echo "UTC" > /etc/timezone

RUN adduser --gid 0 -d /lunch --no-create-home -c 'Lunch user' lunch
USER lunch

EXPOSE 8000

ENV ENABLED_RESTAURANTS=asport,portoriko,nepal,purkynka,liquidbread,tasteofindia,kotelna,padthai,velorex,3opice

CMD python3 -m lunch.lunch

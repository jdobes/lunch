FROM centos:8

ADD web/*.json /web-build/
ADD web/public/ /web-build/public/
ADD web/src/ /web-build/src/

ADD api/* /lunch/
ADD api/restaurants/* /lunch/restaurants/

RUN dnf -y install sqlite npm python3-pip && \
    cd /web-build && npm install && npm run build && \
    mv build /lunch/web && cd / && rm -rf web-build && rm -rf /root/.npm && \
    pip3 install -r /lunch/requirements.txt && \
    rm -rf /root/.cache && \
    dnf -y remove npm python3-pip && dnf clean all

RUN adduser --gid 0 -d /lunch --no-create-home -c 'Lunch user' lunch
USER lunch

EXPOSE 8000

ENV ENABLED_RESTAURANTS=asport,portoriko,nepal,purkynka,liquidbread,tasteofindia,kotelna,padthai,velorex,3opice

CMD python3 -m lunch.lunch

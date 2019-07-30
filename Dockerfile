FROM fedora

RUN dnf -y update && dnf -y install sqlite npm && dnf clean all

ADD web/*.json /web-build/
ADD web/public/ /web-build/public/
ADD web/src/ /web-build/src/
RUN cd /web-build && npm install && npm run build && mkdir /lunch && \
    mv build /lunch/web && cd / && rm -rf web-build

ADD api/requirements.txt /lunch/

RUN pip3 install --upgrade pip
RUN pip3 install -r /lunch/requirements.txt

RUN adduser --gid 0 -d /lunch --no-create-home -c 'Lunch user' lunch
USER lunch

EXPOSE 8000

ENV ENABLED_RESTAURANTS=asport,portoriko,nepal,purkynka,liquidbread,tasteofindia,kotelna,padthai,velorex,3opice

ADD api/* /lunch/
ADD api/restaurants/* /lunch/restaurants/


CMD python3 -m lunch.lunch

FROM fedora

RUN dnf -y update && dnf -y install sqlite npm && dnf clean all

ADD lunch-web/*.json /lunch-web-build/
ADD lunch-web/public/ /lunch-web-build/public/
ADD lunch-web/src/ /lunch-web-build/src/
RUN cd /lunch-web-build && npm install && npm run build && mkdir /lunch && \
    mv build /lunch/web && cd / && rm -rf lunch-web-build

ADD requirements.txt /

RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

RUN adduser --gid 0 -d /lunch --no-create-home -c 'Lunch user' lunch
USER lunch

EXPOSE 8000

ENV ENABLED_RESTAURANTS=asport,portoriko,nepal,purkynka,liquidbread,tasteofindia,kotelna,padthai,velorex,3opice

ADD lunch-api/* /lunch/
ADD lunch-api/restaurants/* /lunch/restaurants/


CMD python3 -m lunch.lunch

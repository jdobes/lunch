FROM fedora

RUN dnf -y update && dnf -y install sqlite && dnf clean all

ADD requirements.txt /

RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

RUN adduser --gid 0 -d /lunch --no-create-home -c 'Lunch user' lunch
USER lunch

EXPOSE 8000

ENV ENABLED_RESTAURANTS=asport,portoriko,nepal,purkynka,liquidbread,tasteofindia,kotelna,padthai,velorex,3opice

ADD lunch-api/* /lunch/
ADD lunch-api/restaurants/* /lunch/restaurants/
ADD lunch-api/static/* /lunch/static/

CMD python3 -m lunch.lunch

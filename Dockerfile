FROM fedora

RUN dnf -y update && dnf clean all

ADD requirements.txt /lunch/

RUN pip3 install --upgrade pip
RUN pip3 install -r /lunch/requirements.txt

RUN adduser --gid 0 -d /lunch --no-create-home -c 'Lunch user' lunch
USER lunch

EXPOSE 8000

ADD config.yml /lunch/
ADD openapi.spec.yml /lunch/
ADD index.html /lunch/
ADD static/* /lunch/static/
ADD restaurants/*.py /lunch/restaurants/
ADD lunch.py /lunch/

CMD python3 /lunch/lunch.py

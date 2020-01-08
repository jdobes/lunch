FROM registry.access.redhat.com/ubi8/ubi-minimal

RUN microdnf install nginx && microdnf clean all

ADD proxy/nginx.conf /etc/nginx/nginx.conf

USER nginx

EXPOSE 8000

CMD ["nginx", "-g", "daemon off;"]

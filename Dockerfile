FROM arm64v8/python:3.9-alpine3.16
USER root

RUN ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

RUN adduser -D app

ADD run.sh /sbin/run.sh
RUN chmod ugo+xr /sbin/run.sh

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./static /code/static
COPY ./templates /code/templates
COPY ./app /code/app
RUN chgrp -R 0 /code && \
    chmod -R g=u /code

USER app

ENV FILES_BASEPATH=/tmp

EXPOSE 8080
ENTRYPOINT ["/sbin/run.sh"]
CMD ["app.main:app", "--host", "0.0.0.0", "--port", "8080"]

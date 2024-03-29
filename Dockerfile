FROM python:3.11-alpine3.17
ENV PYTHONUNBUFFERED=1

COPY ./pitblog /pitblog

COPY commands.sh /commands.sh

WORKDIR /pitblog
EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /pitblog/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod +x /commands.sh

ENV PATH="/scripts:/venv/bin:$PATH"

USER duser

CMD ["/commands.sh"]
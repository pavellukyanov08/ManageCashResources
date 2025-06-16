FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=flowcash_app.settings
ENV PATH="/venv/bin:$PATH"

WORKDIR /cashflowmanage

RUN python -m venv /venv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod 755 /cashflowmanage && \
    mkdir -p /var/log/gunicorn

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

RUN pip install gunicorn

ENTRYPOINT ["./entrypoint.sh"]
#CMD ["gunicorn", "manage.py", "runserver", "0.0.0.0:8000", "--workers", "3"]


FROM python:latest

LABEL environment=Production
LABEL author="Ramkumar JD"
LABEL company=SISL

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]

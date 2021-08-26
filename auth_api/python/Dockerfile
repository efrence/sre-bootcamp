FROM python:3.9.1
ADD . ./src
WORKDIR /src
EXPOSE 8000
RUN pip install -r requirements.txt
CMD ["python", "api.py"]

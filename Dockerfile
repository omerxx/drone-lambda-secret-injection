FROM python:2.7-alpine

RUN apk -Uuv add ca-certificates

RUN pip install boto3

ADD lambda-update-env.py /bin/

RUN chmod +x /bin/ecs-deploy.py 

ENTRYPOINT ["python", "/bin/lambda-update-env.py"]

FROM public.ecr.aws/lambda/python:3.12


COPY app/* ${LAMBDA_TASK_ROOT}/
COPY requirements.txt .

RUN pip install -r requirements.txt -t ${LAMBDA_TASK_ROOT}/app

CMD ["entry.handler"]

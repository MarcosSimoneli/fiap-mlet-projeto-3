FROM public.ecr.aws/lambda/python:3.11

RUN pip install --no-cache-dir scikit-learn pandas boto3

COPY lambda_handler.py ./
COPY Services ./Services
COPY Data ./Data
COPY modelo_bestseller.pkl ./

CMD ["lambda_handler.lambda_handler"]
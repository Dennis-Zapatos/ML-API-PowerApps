# 
#FROM python:3.9

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# 
# WORKDIR /app

# 
COPY ./requirements.txt /ML-API-POWERAPPS/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /ML-API-POWERAPPS/requirements.txt

# 
COPY ./app /main/app

# 
# CMD ["fastapi", "run", "app/main.py", "--port", "80"]
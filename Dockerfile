FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY . .
RUN python3 -m pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#COPY . .
#CMD ["python", "main.py"]

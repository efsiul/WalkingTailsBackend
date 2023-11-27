FROM python:3.11.6

WORKDIR /app                                                                
COPY    . /app
RUN     pip install --no-cache-dir -r requirements.txt
EXPOSE  3000
CMD     ["uvicorn", "app.main.main:app", "--host", "0.0.0.0", "--port", "3000"]
FROM python:3.12-rc-bullseye

COPY [".", "."]

# RUN pip install --upgrade -r requirements.txt

CMD [ "python", "./src/main.py"]


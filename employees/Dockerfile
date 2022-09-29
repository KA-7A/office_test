FROM python:3.10

RUN git clone https://github.com/KA-7A/office_test /drf_src
WORKDIR /drf_src
ENV PYTHONUNBUFFERED 1

RUN pip3 install poetry

WORKDIR /drf_src/office_test/employees
RUN poetry install


EXPOSE 8000

RUN poetry run python3 manage.py makemigrations employees_app && poetry run python3 manage.py migrate && poetry runython3 manage.py runserver 2>/dev/null

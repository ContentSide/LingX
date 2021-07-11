FROM python:3.7.11-slim

WORKDIR /home

COPY . /home
RUN pip install -e .

CMD ["bash"]
FROM python:3.11-slim

RUN pip install uvicorn falcon
RUN mkdir -p /workspace
WORKDIR /workspace
COPY main.py /workspace/main.py

EXPOSE 8000
ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0" ]

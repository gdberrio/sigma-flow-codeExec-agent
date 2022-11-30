FROM python:3.10-bullseye
RUN pip install pymc seaborn "fastapi[all]"
COPY agent.py .
ADD data ./data
CMD ["uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "80"]
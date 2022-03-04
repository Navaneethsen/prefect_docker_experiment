FROM prefecthq/prefect:0.15.13

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

ENV PYTHONPATH="$PYTHONPATH:/app"

# Changing Prefect Backend to Server
RUN prefect backend server

# Running the Prefect Agent
CMD python agent.py

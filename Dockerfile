FROM prefecthq/prefect:0.15.13

WORKDIR /app

RUN mkdir -p ./input_dir

ADD . .

RUN pip install -r ./requirements.txt

# Changing Prefect Backend to Server
RUN prefect backend server

# Running the Translation Evaluator Prefect Agent
CMD python docker_agent/agent.py

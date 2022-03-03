# Prefect Docker Agent + Local Storage Flow

This is an experiment to run the setup for Docker RunConfig + Local Storage for the flow.

Currenty this is not working, and I am trying to figure out the problem.

##Steps

1. Build the Docker image with `docker build . -t test:latest`
2. Register the flow with `python workflow/flow.py`
3. Start your agent with `prefect agent docker start -l 'TestFlow'`
4. Run the flow with a `Quick Run` from the UI

##Courtesy
https://github.com/kvnkho/demos/tree/main/prefect/docker_with_local_storage

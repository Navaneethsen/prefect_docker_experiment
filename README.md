# Prefect Docker Agent + Local Storage Flow

This is an experiment to run the setup for Docker RunConfig + Local Storage for the flow.

~~Currenty this is not working, and I am trying to figure out the problem.~~
I have added a docker-compose.yml file to start the docker agent to run the flows.

## Steps

0. Please add the env variables accordingly

1. Build and Run the Docker image with `docker-compose -f ./docker-compose.yml --env-file ./.env -p "Test Agent" up --build -d`
2. Register the flow with `python workflow/flow.py`. (I have used my own prefect server, but if you want to use the cloud, you need to supply the accesskey somewhere)
3. Run the flow with a `Quick Run` from the UI

## Original Source
https://github.com/kvnkho/demos/tree/main/prefect/docker_with_local_storage

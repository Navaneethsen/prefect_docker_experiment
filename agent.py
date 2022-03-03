# Basic Imports
from os import environ


# Configuring the prefect server.
try:
    
    # External Imports of Prefect
    from prefect.agent.docker.agent import DockerAgent

except Exception:
    raise Exception


def main():
    """Main Function"""

    # Labels for the file drop flow to be monitored
    input_mount = environ.get("STORAGE_FOLDER_PATH") + ":" + "/store_dir"
    
    HOST_IP = environ.get("HOST_IP")

    # Setting environment variables for the flow
    env_vars = {
        "HTTP_PROXY": environ.get("HTTP_PROXY"),
        "HTTPS_PROXY": environ.get("HTTPS_PROXY"),
    }

    # Starting the Prefect DockerAgent
    prefect_agent = DockerAgent(
        env_vars=env_vars,
        name="Docker Test Agent",
        no_pull=True,
        volumes=[input_mount],
        labels=["TestAgent", f"IP:{HOST_IP}"],
        show_flow_logs=True,
    )
    
    prefect_agent.start()


if __name__ == "__main__":
    main()

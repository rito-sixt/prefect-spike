import sys
import prefect
from prefect import flow, task, get_run_logger
from utilities import AN_IMPORTED_MESSAGE


@task
def log_task(task_name):
    logger = get_run_logger()
    logger.info("Hello %s!", task_name)
    logger.info("Prefect Version = %s 🚀", prefect.__version__)
    logger.debug(AN_IMPORTED_MESSAGE)


@flow()
def log_flow(flow_name: str):
    log_task(flow_name)


if __name__ == "__main__":
    name = sys.argv[1]
    log_flow(name)

# Usage instructions

1. Create virtual environment
2. Install prefect - `pip install prefect`
3. Set sqlite database path
    - `prefect config set PREFECT_API_DATABASE_CONNECTION_URL="sqlite+aiosqlite://///Users/ritabratamoitra/.prefect/prefect.db"`
4. Run required flow - `python3 hello_world_flow.py

# Running the Prefect server

`prefect server start`

# Deployments

1. Implement a flow. Example - `sample_deployment_flow`
2. Build the config yaml
   - `prefect deployment build sample_deployment.py:log_flow -n log-simple -q test`. This generates `log_flow-deployment.yaml`
3. Apply the deployment - `prefect deployment apply log_flow-deployment.yaml`
4. Trigger a run - `prefect deployment run 'log-flow/log-simple'` ( This keeps the
   execution in queue, until agent of type `test` is triggered )
5. Instantiate an agent for execution - `prefect agent start -q 'test'`

More about Prefect deployments here - https://docs.prefect.io/tutorials/deployments/

# Docker Container as a deployment
1. Create docker container block by - `python blocks/docker_block.py`. This creates a infra block on Prefect
2. Build the docker image locally - `docker build -t test_prefect .`
3. 
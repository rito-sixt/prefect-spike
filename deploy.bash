docker build -t test-prefect .
IMAGE=$(docker images --no-trunc --quiet test-prefect)

# custom infra block
python blocks/docker_block.py
prefect deployment build flows/sample_deployment.py:log_flow -n log-flow-docker -ib docker-container/prod -q test --override image=$IMAGE --param flow_name=Rito --apply
prefect deployment run log-flow/log-flow-docker

from prefect.infrastructure import DockerContainer

docker_block = DockerContainer(image="test_prefect:latest")
uuid = docker_block.save("prod", overwrite=True)
print(uuid)

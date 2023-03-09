from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner


@task
def first_task(num):
    return num + num


@task
def second_task(num):
    return num * num


@flow(name="My Example Flow",
      task_runner=SequentialTaskRunner(),
      )
def my_flow(num):
    plus_num = first_task.submit(num)
    sq_num = second_task.submit(plus_num)
    print(f"add: {plus_num.result()}, square: {sq_num.result()}")


if __name__ == '__main__':
    my_flow(5)

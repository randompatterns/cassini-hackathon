from app import App
from dependencies import DEPENDENCIES, BOOTSTRAP
from pipelines import PIPELINE_1, PIPELINE_2
from tasks import TASK_1, TASK_2, TASK_3, TASK_4

app = App(bootstrap=BOOTSTRAP)

# register tasks to be executed within pipelines
PIPELINE_1.register_task(TASK_1)
PIPELINE_1.register_task(TASK_2)
PIPELINE_2.register_task(TASK_3)
PIPELINE_2.register_task(TASK_4)

# register pipelines for dependency injection and independent execution
app.register_pipeline(PIPELINE_1)
app.register_pipeline(PIPELINE_2)

# inject dependencies to tasks
app.inject_dependencies(DEPENDENCIES)

# execute pipelines
PIEPLINE_1_RESULT = app.execute_pipeline(name=PIPELINE_1.name)
PIPELINE_2_RESULT = app.execute_pipeline(name=PIPELINE_2.name)

from app import App
from dependencies import BOOTSTRAP
from pipelines import PIPELINE_1
from tasks import ACQUIRE_REGIONAL_CUBE_TASK
from use_cases.dependencies import DEPENDENCIES

app = App(bootstrap=BOOTSTRAP)

# register tasks to be executed within pipelines
PIPELINE_1.register_task(ACQUIRE_REGIONAL_CUBE_TASK)

# register pipelines for dependency injection and independent execution
app.register_pipeline(PIPELINE_1)

# inject dependencies to tasks
app.inject_dependencies(DEPENDENCIES)

# execute pipelines
PIPELINE_1_RESULT = app.execute_pipeline()

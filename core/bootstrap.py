import inspect

from core.decorators import logger
from core.interface import TaskInterface
from use_cases.dependencies import DEPENDENCIES
from use_cases.region_aquisition.task import AcquireRegionalCubeTask


class Bootstrap:
    """
    Bootstrap class responsible for injection of all dependencies required to all handlers involved in the
    user authentication process.
    """
    @classmethod
    @logger
    def inject_dependencies(cls, task: TaskInterface, dependencies: dict):
        parameters = cls.get_signature_parameters(task)
        task_dependencies = {key: value for key, value in dependencies.items() if key in parameters}
        return lambda data: task(data, **task_dependencies)

    @classmethod
    @logger
    def get_signature_parameters(cls, task: TaskInterface):
        return list(inspect.signature(task).parameters.keys())

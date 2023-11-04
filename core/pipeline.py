from copy import deepcopy
from typing import Any, Optional

from core.decorators import logger
from core.interface import PipelineTasks, TaskInterface, PipelineName


class Pipeline:
    tasks: PipelineTasks = []

    def __init__(self):
        self.name = PipelineName(self.__class__.__name__)

    @logger
    def register_task(self, task: TaskInterface):
        self.tasks.append(task)

    @logger
    def execute(self, data: Any) -> Optional[Any]:
        data = deepcopy(data)
        for task in self.tasks:
            data = task(data)
        return data

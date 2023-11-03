from dataclasses import dataclass
from typing import Protocol, Any, Optional


# ---------------------------------------------- dependency interfaces ----------------------------------------------- #
@dataclass
class DependenciesInterface(Protocol):
    ...


class BootstrapInterface(Protocol):
    ...


# -------------------------------------------------- task interfaces ------------------------------------------------- #
@dataclass
class TaskDataInterface(Protocol):
    data: Any


class TaskInterface(Protocol):
    def __call__(self, data: TaskDataInterface, *args: Any, **kwargs: Any) -> TaskDataInterface:
        ...


# ----------------------------------------------- pipeline interfaces ------------------------------------------------ #
PipelineTasks = list[Optional[TaskInterface]]


class PipelineName(str):
    ...


class PipelineInterface(Protocol):
    name: Optional[PipelineName] = None
    tasks: PipelineTasks

    def register_task(self, task: TaskInterface) -> None:
        ...

    def execute(self, data: Any) -> Optional[Any]:
        ...


# --------------------------------------------------- app interface -------------------------------------------------- #
class AppInterface(Protocol):
    def __init__(self, bootstrap: BootstrapInterface):
        ...

    def inject_dependencies(self, dependencies: DependenciesInterface):
        ...

    def register_pipeline(self, pipeline: PipelineInterface) -> None:
        ...

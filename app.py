from typing import Optional

from core.bootstrap import Bootstrap
from core.decorators import logger
from core.interface import PipelineInterface, DependenciesInterface
from core.pipeline import Pipeline


class App:
    dependencies: Optional[DependenciesInterface] = None
    pipeline: PipelineInterface

    def __init__(self, bootstrap: Bootstrap):
        self.bootstrap = bootstrap

    @logger
    def register_pipeline(self, pipeline: Pipeline):
        self.pipeline = pipeline

    @logger
    def inject_dependencies(self, dependencies: dict):
        for i, task in enumerate(self.pipeline.tasks):
            injected_task = self.bootstrap.inject_dependencies(task, dependencies)
            self.pipeline.tasks[i] = injected_task

    @logger
    def execute_pipeline(self):
        self.pipeline.execute(None)

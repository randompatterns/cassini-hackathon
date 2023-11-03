from typing import Optional

from core.interface import PipelineInterface
from core.pipeline import Pipeline
from use_cases.dependencies import Dependencies


class App:
    dependencies: Optional[Dependencies] = None
    pipelines: dict[str, PipelineInterface] = {}

    def __init__(self, bootstrap: Bootstrap):
        self.bootstrap = bootstrap

    def register_pipeline(self, pipeline: Pipeline):
        self.pipelines[pipeline.name] = pipeline

    def inject_dependencies(self, dependencies: Dependencies):
        ...  # call bootstrap to inject dependencies

    def execute_pipeline(self, name: str):
        ...

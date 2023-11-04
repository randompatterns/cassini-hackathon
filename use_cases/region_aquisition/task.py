from typing import Optional, Any

from core.decorators import logger
from core.interface import TaskDataInterface
from core.task_data import TaskData
from infrastructure.openeo_repository import OpeneoRepository
from use_cases.dependencies import DEPENDENCIES
from use_cases.region_aquisition.domain import Bands, TemporalExtent, SpatialExtent, CloudCoverage, CubeFormat, \
    BatchJobTitle, OutputPath


class AcquireRegionalCubeTask:
    @logger
    def __call__(
        self,
        data: Any,
        sentinel2_l2a_collection: OpeneoRepository,
        rgb_bands: Bands,
        cube_timeframe: TemporalExtent,
        cube_region: SpatialExtent,
        cloud_coverage: CloudCoverage,
        cube_format: CubeFormat,
        batch_job_title: BatchJobTitle,
        output_path: OutputPath
    ) -> Optional[TaskDataInterface]:
        data_cube = sentinel2_l2a_collection.get_cube(rgb_bands, cube_timeframe, cube_region, cloud_coverage)
        tif_cube = data_cube.save_result(format=cube_format)
        job = tif_cube.create_job()
        job.start_and_wait()
        results = job.get_results()
        results.download_files(target=output_path)
        output = TaskData(data=output_path)
        return output

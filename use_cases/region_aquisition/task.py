from typing import Optional

from core.interface import TaskDataInterface
from core.task_data import TaskData
from infrastructure.openeo_repository import OpeneoRepository
from use_cases.region_aquisition.config import AcquireRegionalCubeDependencies
from use_cases.region_aquisition.domain import Bands, TemporalExtent, SpatialExtent, CloudCoverage, CubeFormat, \
    BatchJobTitle, OutputPath


class AcquireRegionalCubeTask:
    def __call__(
        self,
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
        job = tif_cube.execute_batch(title=batch_job_title)
        results = job.get_results()
        results.download_files(target=output_path)
        output = TaskData(data=output_path)
        return output


if __name__ == "__main__":
    dependencies = AcquireRegionalCubeDependencies()
    task = AcquireRegionalCubeTask()
    task(
        dependencies.sentinel2_l2a_collection,
        dependencies.rgb_bands,
        dependencies.cube_timeframe,
        dependencies.cube_region,
        dependencies.cloud_coverage,
        dependencies.cube_format,
        dependencies.batch_job_title,
        dependencies.output_path)

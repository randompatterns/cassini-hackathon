from collections import UserDict

from infrastructure.openeo_repository import OpeneoRepository
from use_cases.region_aquisition.domain import Bands, TemporalExtent, SpatialExtent, CloudCoverage, CubeFormat, \
    BatchJobTitle, OutputPath

# connection
OPENEO_URL = "openeo.dataspace.copernicus.eu"

# bands
CUBE_RGB_BANDS = Bands.rgb()

# timeframe
CUBE_CUSTOM_TIMEFRAME = TemporalExtent("2022-05-01", "2022-05-30")
CUBE_LAST_DAY = TemporalExtent.last_day()
CUBE_LAST_WEEK = TemporalExtent.last_week()
CUBE_LAST_MONTH = TemporalExtent.last_month()

# cloud coverage
CUBE_MAX_CLOUD_COVERAGE = CloudCoverage(50)

# region 1
CUBE_REGION_1 = SpatialExtent(3.202609, 51.189474, 3.254708, 51.204641)
POLAND = SpatialExtent(-21.58, 45.5, 26.5, 55.183)

# collections
SENTINEL2_L2A_COLLECTION = OpeneoRepository(OPENEO_URL, "SENTINEL2_L2A")

# formats
TIF_FORMAT = "GTiff"

# batch job titles
JOB_1_TITLE = "Slice of S2 data"

# output paths
JOB_1_OUTPUT_PATH = "output/batch_job"


# dependencies
class AcquireRegionalCubeDependencies(UserDict):
    sentinel2_l2a_collection: OpeneoRepository = SENTINEL2_L2A_COLLECTION
    rgb_bands: Bands = CUBE_RGB_BANDS
    cube_timeframe: TemporalExtent = CUBE_CUSTOM_TIMEFRAME
    cube_region: SpatialExtent = CUBE_REGION_1
    cloud_coverage: CloudCoverage = CUBE_MAX_CLOUD_COVERAGE
    cube_format: CubeFormat = TIF_FORMAT
    batch_job_title: BatchJobTitle = JOB_1_TITLE
    output_path: OutputPath = JOB_1_OUTPUT_PATH

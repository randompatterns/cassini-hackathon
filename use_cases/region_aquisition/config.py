from infrastructure.openeo_repository import OpeneoRepository
from use_cases.region_aquisition.domain import Bands, TemporalExtent, SpatialExtent, CloudCoverage

# connection
OPENEO_URL = "openeo.dataspace.copernicus.eu"

# bands
CUBE_RGB_BANDS = Bands.rgb()

# timeframe
CUBE_CUSTOM_TIMEFRAME = TemporalExtent("2022-05-01", "2022-05-05")
CUBE_LAST_DAY = TemporalExtent.last_day()
CUBE_LAST_WEEK = TemporalExtent.last_week()
CUBE_LAST_MONTH = TemporalExtent.last_month()

# cloud coverage
CUBE_MAX_CLOUD_COVERAGE = CloudCoverage(0)

# region 1
CUBE_REGION_1 = SpatialExtent(3.202609, 51.189474, 3.254708, 51.204641)
POLAND = SpatialExtent(-21.58, 45.5, 26.5, 55.183)
SEA_TEST = SpatialExtent(27.062416, 31.347773, 27.572937, 31.640522)
MADRID = SpatialExtent(-3.888, 40.312, -3.517, 40.643)
# collections
SENTINEL2_L2A_COLLECTION = OpeneoRepository(OPENEO_URL, "SENTINEL2_L2A")

# formats
TIF_FORMAT = "GTiff"

# batch job titles
JOB_1_TITLE = "Slice of S2 data"

# output paths
JOB_1_OUTPUT_PATH = "output/batch_job"

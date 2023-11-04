from use_cases.region_aquisition.config import SENTINEL2_L2A_COLLECTION, CUBE_RGB_BANDS, CUBE_CUSTOM_TIMEFRAME, MADRID, \
    CUBE_MAX_CLOUD_COVERAGE, TIF_FORMAT, JOB_1_TITLE, JOB_1_OUTPUT_PATH

DEPENDENCIES = {
    "sentinel2_l2a_collection": SENTINEL2_L2A_COLLECTION,
    "rgb_bands": CUBE_RGB_BANDS,
    "cube_timeframe": CUBE_CUSTOM_TIMEFRAME,
    "cube_region": MADRID,
    "cloud_coverage": CUBE_MAX_CLOUD_COVERAGE,
    "cube_format": TIF_FORMAT,
    "batch_job_title": JOB_1_TITLE,
    "output_path": JOB_1_OUTPUT_PATH
}

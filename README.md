# cassini-hackathon
cassini hackathon 2023

### Description of satelites:
1. Weather
2. (B) Vegetation 13 spectral bands
3. Near real time water and ocea topography, color, temperature
4. Air Quality
5. (P) Trace gases
6. Sea surface
   
https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data

https://www.esa.int/Applications/Observing_the_Earth/Copernicus/The_Sentinel_missions

### openeo & sentinelhub documentation:

https://docs.openeo.cloud/getting-started/python/#installation

https://sentinelhub-py.readthedocs.io/en/latest/

### box finder:

http://bboxfinder.com/#0.000000,0.000000,0.000000,0.000000

### dashboard with sentinel credentials:

https://shapps.dataspace.copernicus.eu/dashboard/#/

WGS84
[(longitude and latitude coordinates of lower left and upper right corners)]

### Download batch with openEO

```
import openeo
import pathlib
import rasterio
import matplotlib.pyplot as plt

connection = openeo.connect(url="openeo.dataspace.copernicus.eu")
#To authenticate: visit https://aai.egi.eu/auth/realms/egi/device and enter the user code 'SLUO-BMUD'
connection.authenticate_oidc()

#print all available datasets
print(connection.list_collection_ids())

#printspecification for the datasets
print(connection.describe_collection("SENTINEL3_OLCI_L1B"))

cube = connection.load_collection(
    "SENTINEL2_L2A",
    bands=["B04", "B03", "B02"], #-> RGB channel
    temporal_extent=("2022-05-01", "2022-05-30"), #-> timeframe
    spatial_extent={
        "west": 3.202609,
        "south": 51.189474,
        "east": 3.254708,
        "north": 51.204641,
        "crs": "EPSG:4326", #-> EPSG:4326 Geodetic coordinate system for World
    },
    max_cloud_cover=50,
)

cube = cube.save_result(format="GTiff")
job = cube.execute_batch(title="Slice of S2 data")
print(job.job_id)
results = job.get_results()
results.download_files("output/batch_job")

fig, axes = plt.subplots(figsize=(6, 4), nrows=2, ncols=2, dpi=90)
for i, path in enumerate(sorted(pathlib.Path("output/batch_job/").glob("*tif"))[:4]):
    data = rasterio.open(path).read()
    ax = axes[i // 2, i % 2]
    ax.imshow((data.transpose(1, 2, 0) / 3000).clip(0, 1))
    ax.set_title(path.name)

```

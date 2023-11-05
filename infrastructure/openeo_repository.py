from __future__ import annotations

from dataclasses import asdict
from typing import Protocol
import openeo

from use_cases.region_aquisition.domain import CollectionName, Bands, TemporalExtent, SpatialExtent, CloudCoverage


class OpeneoRepository(Protocol):
    def __init__(self, url: str, collection_name: CollectionName):
        self.client = openeo.connect(url)
        self.client.authenticate_oidc()
        self.collection_name = collection_name
        self.description = self.client.describe_collection(self.collection_name)

    def get_bands(self) -> list[str]:
        return self.description.get("cube:dimensions").get("bands").get("values")

    def get_spatial_extent(self) -> list[list[str, str, str, str]]:
        return self.description.get("extent").get("spatial").get("bbox")

    def get_cube(
        self,
        bands: Bands,
        temporal_extent: TemporalExtent,
        spatial_extent: SpatialExtent,
        cloud_coverage: CloudCoverage
    ) -> openeo.DataCube:
        cube = self.client.load_collection(
            self.collection_name,
            bands=bands,
            temporal_extent=(temporal_extent.start, temporal_extent.end),
            spatial_extent=asdict(spatial_extent),
            max_cloud_cover=cloud_coverage,
        )
        return cube


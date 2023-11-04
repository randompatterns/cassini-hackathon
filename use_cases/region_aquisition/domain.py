from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta

from typing import Literal

CollectionName = Literal[
    'SENTINEL3_OLCI_L1B',
    'SENTINEL3_SLSTR',
    'SENTINEL_5P_L2',
    'SENTINEL2_L1C',
    'SENTINEL2_L2A',
    'SENTINEL1_GRD',
    'COPERNICUS_30'
]


class Bands(list):
    @classmethod
    def rgb(cls) -> Bands:
        return cls(["B04", "B03", "B02"])


@dataclass
class TemporalExtent:
    start: str
    end: str

    @classmethod
    def last_day(cls) -> TemporalExtent:
        return cls(cls._yesterday(), cls._today())

    @classmethod
    def last_week(cls) -> TemporalExtent:
        return cls(cls._week_ago(), cls._today())

    @classmethod
    def last_month(cls) -> TemporalExtent:
        return cls(cls._month_ago(), cls._today())

    @staticmethod
    def _today() -> str:
        return date.today().strftime("Y-M-D")

    @staticmethod
    def _yesterday() -> str:
        return (date.today() - timedelta(days=1)).strftime("Y-M-D")

    @staticmethod
    def _week_ago() -> str:
        return (date.today() - timedelta(days=7)).strftime("Y-M-D")

    @staticmethod
    def _month_ago() -> str:
        return (date.today() - timedelta(days=30)).strftime("Y-M-D")


@dataclass
class SpatialExtent:
    west: float
    south: float
    east: float
    north: float
    crs: str = field(default="EPSG:4326")


class CloudCoverage(float):
    ...


class CubeFormat(str):
    ...


class BatchJobTitle(str):
    ...


class OutputPath(str):
    ...

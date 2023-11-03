class City:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng

    def get_spatial_extent(self, radius=0.08):
        spatial_extent = {
            "west": self.lng-radius, 
            "south": self.lat-radius, 
            "east": self.lng+radius, 
            "north": self.lat+radius
        }
        return spatial_extent

    def get_features(self, radius=0.08):
        features = {
            "type": "FeatureCollection", 
            "features": [
                {
                    "type": "Feature", 
                    "properties": {},
                    "geometry": {
                        "type": "Polygon", 
                        "coordinates": [
                            [
                                [self.lat - radius, self.lng - radius], 
                                [self.lat + radius, self.lng - radius], 
                                [self.lat + radius, self.lng + radius], 
                                [self.lat - radius, self.lng + radius], 
                                [self.lat - radius, self.lng - radius]
                            ]
                        ]
                    }
                }
            ]
        }
        return features

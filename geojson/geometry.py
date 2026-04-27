from decimal import Decimal
from numbers import Number, Real

from geojson.base import GeoJSON


DEFAULT_PRECISION = 6


class Geometry(GeoJSON):
    """
    Represents an abstract base class for a WGS84 geometry.
    """

    def __init__(self, coordinates=None, validate=False, precision=None, **extra):
        """
        Initialises a Geometry object.

        :param coordinates: Coordinates of the Geometry object.
        :type coordinates: tuple or list of tuple
        :param validate: Raise exception if validation errors are present?
        :type validate: boolean
        :param precision: Number of decimal places for lat/lon coords.
        :type precision: integer
        """
        super().__init__(**extra)
        if precision is None:
            precision = DEFAULT_PRECISION
        self["coordinates"] = self.clean_coordinates(
            coordinates or [], precision)

        if validate:
            errors = self.errors()
            if errors:
                raise ValueError(f'{errors}: {coordinates}')

    @classmethod
    def clean_coordinates(cls, coords, precision):
        pass


class GeometryCollection(GeoJSON):
    """
    Represents an abstract base class for collections of WGS84 geometries.
    """

    def __init__(self, geometries=None, **extra):
        super().__init__(**extra)
        self["geometries"] = geometries or []

    def errors(self):
        pass

    def __getitem__(self, key):
        try:
            return self.get("geometries", ())[key]
        except (KeyError, TypeError, IndexError):
            return super(GeoJSON, self).__getitem__(key)


# Marker classes.

def check_point(coord):
    pass


class Point(Geometry):
    def errors(self):
        pass


class MultiPoint(Geometry):
    def errors(self):
        pass


def check_line_string(coord):
    pass


class LineString(MultiPoint):
    def errors(self):
        pass


class MultiLineString(Geometry):
    def errors(self):
        pass


def check_polygon(coord):
    pass


class Polygon(Geometry):
    def errors(self):
        pass


class MultiPolygon(Geometry):
    def errors(self):
        pass


class Default:
    """
    GeoJSON default object.
    """

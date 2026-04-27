from collections.abc import MutableMapping

try:
    import simplejson as json
except ImportError:
    import json

import geojson


GEO_INTERFACE_MARKER = "__geo_interface__"


def is_mapping(obj):
    """
    Checks if the object is an instance of MutableMapping.

    :param obj: Object to be checked.
    :return: Truth value of whether the object is an instance of
    MutableMapping.
    :rtype: bool
    """
    pass


def to_mapping(obj):

    pass

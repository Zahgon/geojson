try:
    import simplejson as json
except ImportError:
    import json

import geojson
import geojson.factory
from geojson.mapping import to_mapping


class GeoJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        pass


# Wrap the functions from json, providing encoder, decoders, and
# object creation hooks.
# Here the defaults are set to only permit valid JSON as per RFC 4267

def _enforce_strict_numbers(obj):
    pass


def dump(obj, fp, cls=GeoJSONEncoder, allow_nan=False, **kwargs):
    pass


def dumps(obj, cls=GeoJSONEncoder, allow_nan=False, ensure_ascii=False, **kwargs):
    pass


def load(fp,
         cls=json.JSONDecoder,
         parse_constant=_enforce_strict_numbers,
         object_hook=geojson.base.GeoJSON.to_instance,
         **kwargs):
    pass


def loads(s,
          cls=json.JSONDecoder,
          parse_constant=_enforce_strict_numbers,
          object_hook=geojson.base.GeoJSON.to_instance,
          **kwargs):
    pass


# Backwards compatibility
PyGFPEncoder = GeoJSONEncoder

import jsonschema_rs
import requests
import json
from pathlib import Path

OEO_METADATA = "https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/develop/metadata/v151/schema.json"
LOCAL_PATH = Path("tests/local/oeo_metadataschema.json")

LATEST_PATH = "oedatamodel/latest/v111/datapackage/OEDataModel-concrete-datapackage/OEDataModel-concrete-datapackage.json"

if not LOCAL_PATH.exists():
    response = requests.get(OEO_METADATA).json()
    with open(LOCAL_PATH, "w") as fp:
        json.dump(response, fp)
    schema = response
else:
    with open(LOCAL_PATH, "r") as fp:
        schema =json.load(fp)

validator = jsonschema_rs.JSONSchema(schema)


with open(LATEST_PATH, "r") as fp:
    latest_package =json.load(fp)


print([e.message for e in validator.iter_errors(latest_package)])
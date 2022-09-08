import pytest
import requests
import json 
import jsonschema_rs
from pathlib import Path
LATEST_CONCRETE= "oedatamodel/latest/v111/datapackage/OEDataModel-concrete-datapackage/OEDataModel-concrete-datapackage.json"
LATEST_NORMAL = "oedatamodel/latest/v111/datapackage/OEDataModel-normalization-datapackage/OEDataModel-normalization-datapackage.json"
METADATA_GENERIC = "https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/develop/metadata/{}/schema.json"

METADATA_VERSIONS = ["v130", "v140", "v141", "v150", "v151"]
PACKAGE_VERSIONS = ["v100", "v110"]

LATEST_METADATA = "v151"

LOCAL_PATH = "tests/local/metadata_{}.json"


def pytest_generate_tests(metafunc):
    if ("package" in metafunc.fixturenames) and ("version" in metafunc.fixturenames):
        test_latest_only = metafunc.config.getoption("--latest")
        if test_latest_only == "1":
            metafunc.parametrize("package", [LATEST_CONCRETE, LATEST_NORMAL])
            metafunc.parametrize("version", [LATEST_METADATA])
        else:
            specific_package = metafunc.config.getoption("--package")
            specific_metadata = metafunc.config.getoption("--metadata")
            pkg_to_test = [pkg for pkg in PACKAGE_VERSIONS if pkg == specific_package]
            meta_to_test = [mt for mt in METADATA_VERSIONS if mt == specific_metadata]
            metafunc.parametrize("package", pkg_to_test)
            metafunc.parametrize("version", meta_to_test)

def get_metadata_schema(source, local):
    if not Path(local).exists():
        response = requests.get(source).json()
        with open(local, "w") as fp:
            json.dump(response, fp)
        schema = response
    else:
        with open(local, "r") as fp:
            schema =json.load(fp)
    return schema

def load_metadata(version):
    source = METADATA_GENERIC.format(version)
    local = LOCAL_PATH.format(version)
    Path(local).parent.mkdir(exist_ok=True, parents=True)
    metadata = get_metadata_schema(source, local)
    return metadata

def get_package(source):
    with open(source, "r") as fp:
        package =json.load(fp)
    return package

def test_compilance(package, version):
    package_dictionary = get_package(package)
    metadata = load_metadata(version)
    validator = jsonschema_rs.JSONSchema(metadata)
    report = []
    valid_schema = validator.is_valid(package_dictionary)
    if not valid_schema:
        for error in validator.iter_errors(package_dictionary):
            error_dict = {
                "message": error.message,
                "schema_path": error.schema_path,
                "instance_path": error.instance_path
            }
            report.append(error_dict)
        name = Path(package).stem
        output_file = Path(f"tests/reports/report_{name}_{version}.json")
        output_file.parent.mkdir(exist_ok=True, parents=True)
        with open(output_file, "w") as fp:
            json.dump(report, fp,indent=4, sort_keys=False)

        assert valid_schema, f"The file {Path(package).name} is not valid agianst oemetadata {version}"

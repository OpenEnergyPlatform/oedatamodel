[![Build Status](https://travis-ci.org/OpenEnergyPlatform/edatamodel.svg?branch=develop)](https://travis-ci.org/OpenEnergyPlatform/oedatamodel)

<a href="http://oep.iks.cs.ovgu.de/"><img align="right" width="200" height="200" src="https://avatars2.githubusercontent.com/u/37101913?s=400&u=9b593cfdb6048a05ea6e72d333169a65e7c922be&v=4" alt="OpenEnergyPlatform"></a>

# Open Energy Family - Datamodel
A common open energy data model (oedatamodel) and datapackage format for energy and scenario data.

# Introduction
The oedatamodel is provided as a template data model as Entity Relationship Modell(ERM) and is designed
for the usage on the open energy platform but it can be used in common relational database systems. 
Additional we include a datapackage for every release. 

Existing approaches and ideas such as the [IAMC data format](https://github.com/IAMconsortium/pyam#data-model) or [Do-a-thon: Towards a common data standard 
for integrated assessment and energy systems modelling](https://forum.openmod-initiative.org/t/do-a-thon-towards-a-common-data-standard-for-integrated-assessment-and-energy-systems-modelling/1774/5) were adopted in the development process.

The latest version can be found in the folder oedatamodel/latest. 
The version available there offers the user 2 ERM's. The ERM "oedatamodel.pdf" shows the data model 
that can be implemented on a database (e.g. postgresql). Here tables, relations, column names and 
data types are provided. The ERM "oedatamodel-readable.pdf" is provided additionally and is designed 
to simplify the editing of the data by a user. It also provides tables and relations as well as column 
names and datatypes, but the tables are in a less normalized format. We recommend this version of the 
data model for the implementation in e.g. csv tables because the advantage of the human readable format 
is not optimal for the technical usage in a database. 

In addition, the raw files (file format: .er) from which the PDF respectively the ERM is generated are
also provided for each data model.

# Oedatamodel - Datapackage

We publish a data package for each release. The data package contains the file oedatamodel_datapackage.json 
with example and template content. This includes CSV files representing the data model. The JSON 
file contains the [oemetadata format](https://github.com/OpenEnergyPlatform/oemetadata), which is used to store/provide metadata for open data on the OEP. 
This includes:

- A general description of the data
- List of contributions 
- Licence information 
- Information about sources like records or model frameworks with license information for each source
- The datamodel with metadata for each field
- Table relations and key attributes to provide the information outside a database
- The metadata string itself can be validated using the [Open Metadata Integration (omi)](https://github.com/OpenEnergyPlatform/omi) tool
 
Oemetadata provides a [detailed description](https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/metadata/latest/metadata_key_description.md) with examples for each key in the metadata string.

# Oedatamodel - Usage

## OEDataModel variations
- OEDataModel-concrete
    - Main usage as CSV files
    - Tool that maps the concrete model to the normalization model will be provided. Please be aware about new features.

- OEDataModel-normalization
    - Main usage database (realtional database like postgreSQL)
    - Optimized to store data in a relational data model
    - Normalization for practical data relationships and reduced/no redundant fields to avoid redundant data

## Data model - Examples

The following examples are intended to provide a simple example as well as a detailed descriptoion on each field/column. For completeness we also link to
other examples already provided as file. 

Origin data model: [OEDataModel-concrete](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v100/OEDataModel-concrete.pdf)

### Scenario

| **Field**         | **Description**            |
|-------------------|----------------------------|
|   scenario id     |                            |
|   scenario        |                            |
|   region          |                            |
|   year            |                            |
|   source          |                            |
|   comment         |                            |


| **scenario id** (PK) | **scenario** | **region** | **year**  | **source** | **comment**  |
|----------------------|--------------|------------|-----------|------------|--------------|
| 0                    | 2035         | World      | 2020      | path       |Main scenario |
| ...                  | ...          | ...        | ...       | ...        | ...          |



### Scalar

| **Field**              | **Description**            |
|------------------------|----------------------------|
|   timeseries id        |                            |
|   scenario id          |                            |
|   region               |                            |
|   input energy vector  |                            |
|   output energy vector |                            |
|   parameter name       |                            |
|   technology           |                            |
|   technology type      |                            |
|   value                |                            |
|   unit                 |                            |
|   tags                 |                            |
|   method               |                            |
|   source               |                            |
|   comment              |                            |


| **scalar id** (PK) | **scenario id** (FK) | **region** | **input energy vector**   | **output energy vector** | **parameter name** | **technology** | **technology type** |**value** | **unit** | **tags** | **method** | **source** | **comment** |
|-----------|--------------|------------|----------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| TODO   | TODO | TODO      | TODO | TODO     |    TODO |    TODO |      ... |      ... |      ... |      ... |      ... |      ... |      ... |
| ...       | ...          | ...        | ...            | ...      |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |


### Timeseries

| **Field**              | **Description**            |
|------------------------|----------------------------|
|   timeseries id        |                            |
|   scenario id          |                            |
|   region               |                            |
|   input energy vector  |                            |
|   output energy vector |                            |
|   parameter name       |                            |
|   technology           |                            |
|   technology type      |                            |
|   timeindex start      |                            |
|   timeindex stop       |                            |
|   timeindex resolution |                            |
|   series               |                            |
|   unit                 |                            |
|   tags                 |                            |
|   method               |                            |
|   source               |                            |
|   comment              |                            |


| **timeseries id** (PK) | **scenario id** (FK) | **region** | **input energy vector**   | **output energy vector** | **parameter name** | **technology** | **technology type** |**timeindex start** | **timeindex stop** | **timeindex resolution** | **series** | **unit** | **tags** | **method** | **source** | **comment** |
|-----------|--------------|------------|----------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| TODO   | TODO | TODO      | TODO     |    TODO |    TODO |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |
| ...       | ...          | ...        | ...            | ...      |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |


- Example  Datapackage

    - Example JSON: [OEDataModel-concrete-datapackage](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v100/datapackage/OEDataModel-concrete-datapackage/OEDataModel-concrete-datapackage.json)

    - Example CSV: 
        - [concrete-datapackage_scalar](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v100/datapackage/OEDataModel-concrete-datapackage/OEDataModel-concrete-datapackage_scalar.csv)
        - [OEDataModel-concrete-datapackage_scenario](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v100/datapackage/OEDataModel-concrete-datapackage/OEDataModel-concrete-datapackage_scenario.csv)
        - [OEDataModel-concrete-datapackage_timeseries](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v100/datapackage/OEDataModel-concrete-datapackage/OEDataModel-concrete-datapackage_timeseries.csv)

# Edit the Entity Relationship Modell

For the generation of an ERM we use this [erm tool](https://github.com/BurntSushi/erd). The [er or erd](https://github.com/BurntSushi/erd#the-er-file-format) file format offers a simple syntax and 
can be created and saved using a standard text editor.  

For the generation of the ERM e.g. in .pdf format the installation of the erm tool is necessary. For 
detailed instructions, please see the [package description](https://github.com/BurntSushi/erd#installation).   

After successful installation, a terminal/CMD must be opened and the console command (Windows: 'cd path')
must be used to navigate to the folder where the .er/.erd file is stored. To execute the tools, the command 
is then used in the Terminal/CMD to generate the ERM: 

`erd -i oedatamodel.er -o oedatamodel.pdf`


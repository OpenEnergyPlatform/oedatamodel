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

The latest version can be found in the folder [oedatamodel/latest](https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop/oedatamodel/latest). 
The version available there offers the user 2 ERM's. The ERM "OEDataModel-normalization.pdf" shows the data model 
that can be implemented on a database (e.g. postgresql). Here tables, relations, column names and 
data types are provided. The ERM "OEDataModel-concrete.pdf" is provided additionally and is designed 
to simplify the editing of the data by a user. It also provides tables and relations as well as column 
names and datatypes, but the tables are in a less normalized format. We recommend this version of the 
data model for the implementation in e.g. csv tables because the advantage of the more human usable format 
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

## Fields that are not present or empty in your data

When transferring data from your own data format to the oedatamodel, it may happen that fields cannot be filled properly. In this case we recommend not to leave the field empty and to insert the value "unkown" into the field.

## Delimiter and decimal sepperators

If you transfer data into the oedatamodel format make sure to use the delimiter "," in e.g. .csv files for delimiting a series of values. Decimal numbers are separated by a "." .

Example:
A series ist stored inside an array datatype, each value is sapperated by ",".
| **series**         | 
|--------------------|
| [1423.55706450302, 1566.42140196079]|


## Apply a Datapackage to the Database

[Guide to publish data on the OEP](https://github.com/OpenEnergyPlatform/tutorial/blob/develop/upload/OEP_Research_Data_Publishing_Guidebook.ipynb)

In short:
- Create a OEP compatible [Datapackage](https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop/oedatamodel/latest/v100/datapackage/OEDataModel-concrete-datapackage)
- Start a OEP-Review process
- Start the Upload-Process 

[Guide to upload data to the OEP](https://github.com/OpenEnergyPlatform/tutorial/blob/develop/upload/OEP_Upload_Process_Data_and_Metadata_oem2orm.ipynb)

In short:
- Use your Datapackage files to:
    - Create Tables from the OEDataModel-Datapackage.json file usign [oem2orm](https://pypi.org/project/oem2orm/)
    - Apply OEMetadata to the table
    - Upload your data to the tables from the .csv files in OEDataModel format using Pandas with the oedialect

## Description and examples

The following examples are intended to provide a simple example table as well as a detailed descriptoion on each field/column. For completeness we also link to the datapacke examples which are already provided as file. 

**Since we offer two data model variants with almost identical field names, we provide a description that applies to both variants.**

Origin data model: [OEDataModel-concrete](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v100/OEDataModel-concrete.pdf)

### Scenario description

| **Field**         |  **Datatype** | **Description**            |
|-------------------|---------------|----------------------------|
|   scenario id     |     int       | A primary key is a field or set of fields that uniquely identifies each row in the table. It's recorded as a list of strings, since it is possible to define the primary key as made up of several columns.                           |
|   scenario        |     text      | Name of the scenario.                           |
|   region          |     json      | It describes the geographical scope of the dataset.                           |
|   year            |     int       | It describes the time frame of the dataset.                           |
|   source          |     text      | Human readable title of the source, e.g. document title or organisation name. The source must relate to a source provided in the oemetadata (datapackage) file.                           |
|   comment         |     text      | Free text comment on what's been done.                           |

### Example table:

| **scenario id** (PK) | **scenario** | **region** | **year**  | **source** | **comment**  |
|----------------------|--------------|------------|-----------|------------|--------------|
| 1                    | ToDo         | ['BB']     | 2020      | path       |ToDo          |
| 2                    | ToDo         | ['DE']     | ToDo      | ToDo       | ToDo         |
| 3                    | ToDo         | ['North']  | ToDo      | ToDo       | ToDo         |
| ...                  | ...          | ...        | ...       | ...        | ...          |



### Scalar description

| **Field**              |  **Datatype** | **Description**            |
|------------------------|---------------|----------------------------|
|   scalar id            |      int      | A primary key is a field or set of fields that uniquely identifies each row in the table. It's recorded as a list of strings, since it is possible to define the primary key as made up of several columns.                           |
|   scenario id          |      int      | A foreign key is a field that refers to a primary key column in another table.                           |
|   region               |      json     | It describes the area name in which a scalar operates.                           |
|   input energy vector  |      text     | It describes any type of energy or energy carrier (e.g. electricity, heat, solar radiation, natural gas, ...) that enters a technology.                           |
|   output energy vector |      text     | It describes any type of energy or energy carrier (e.g. electricity, heat, hydrogen, LNG, CO2, ...) that exits a technology.                           |
|   parameter name       |      text     | It describes a considered property of an element in the energy system. It can be technology-related or technology-independent. It can refer to technological, economic or environmental characteristics.                           |
|   technology           |      text     | It describes an element of the modelled energy system that processes an energy vector. A technology can be real (e.g. specific type of power plant) as well as abstracted as an aggregation of energy processes or a virtual process.                           |
|   technology type      |      text     | Is used to specify the technology field. The specification can be technological, or freely user-defined, based on the requirements of the model.                           |
|   value                |      decimal  | Indicates the numerical value of a scalar.                           |
|   unit                 |      text     | Indicates the measuring unit of a value.                           |
|   tags                 |      json     | Is used to further describe a scalar.                           |
|   method               |      json     | It describes the procedure for obtaining the value, in case it does not originate from a single source.                           |
|   source               |      text     | Human readable title of the source, e.g. document title or organisation name. The source must relate to a source provided in the oemetadata (datapackage) file.                           |
|   comment              |      text     | Free text comment on what's been done.                           |

### Example table:

| **scalar id** (PK) | **scenario id** (FK) | **region** | **input energy vector**   | **output energy vector** | **parameter name** | **technology** | **technology type** |**value** | **unit** | **tags** | **method** | **source** | **comment** |
|-----------|--------------|------------|----------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| 1   | 1 | ['DE']    | solar radiation | electricity     |    variable costs |    photovoltaics |      utility |      0.00 |      €/MWh |      Assumption |      ToDo |      ToDo |      ToDo |
| 2   | 1 | ['DE']      | lignite | co2     |    output ratio |    generator |      ToDo |      0.40 |      t/MWh |      ToDo |      ToDo |      ToDo |      ToDO |
| 3   | 2 | ['DE']      | heavyoil | co2     |    output ratio |    generator |      ToDo |      0.29 |      t/MWh |      ToDo |      ToDo |      ToDo |      ToDo |
| ...       | ...          | ...        | ...            | ...      |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |


### Timeseries description

| **Field**              |  **Datatype** | **Description**            |
|------------------------|---------------|----------------------------|
|   timeseries id        |     int       | A primary key is a field or set of fields that uniquely identifies each row in the table. It's recorded as a list of strings, since it is possible to define the primary key as made up of several columns.                           |
|   scenario id          |     int       | A foreign key is a field that refers to a primary key column in another table.                           |
|   region               |     json      | It describes the area name in which a timeseries operates.                           |
|   input energy vector  |     text      | It describes any type of energy or energy carrier (e.g. electricity, heat, solar radiation, natural gas, ...) that enters a technology.                           |
|   output energy vector |     text      | It describes any type of energy or energy carrier (e.g. electricity, heat, hydrogen, LNG, CO2, ...) that exits a technology.                           |
|   parameter name       |     text      | It describes a considered property of an element in the energy system. It can be technology-related or technology-independent. It can refer to technological, economic or environmental characteristics.                           |
|   technology           |     text      | It describes an element of the modelled energy system that processes an energy vector. A technology can be real (e.g. specific type of power plant) as well as abstracted as an aggregation of energy processes or a virtual process.                           |
|   technology type      |     text      | Is used to specify the technology field. The specification can be technological, or freely user-defined, based on the requirements of the model.                           |
|   timeindex start      |     [timestamp](https://www.postgresql.org/docs/9.5/datatype-datetime.html)          | Both date and time, with time zone.                           |
|   timeindex stop       |     timestamp | Both date and time, with time zone.                           |
|   timeindex resolution |     [intervall](https://www.postgresql.org/docs/9.5/datatype-datetime.html)          | The time span between individual points of information in a time series.                           |
|   series               |     [decimal] | Series of values, from start to stop with a step size of stepvalues.                           |
|   unit                 |     text      | Indicates the measuring unit of a value.                           |
|   tags                 |     json      | Is used to further describe a timeseries.                           |
|   method               |     json      | It describes the procedure for obtaining the value, in case it does not originate from a single source.                           |
|   source               |     text      | Human readable title of the source, e.g. document title or organisation name. The source must relate to a source provided in the oemetadata (datapackage) file.                           |
|   comment              |     text      | Free text comment on what's been done.                           |

### Example table:

| **timeseries id** (PK) | **scenario id** (FK) | **region** | **input energy vector**   | **output energy vector** | **parameter name** | **technology** | **technology type** |**timeindex start** | **timeindex stop** | **timeindex resolution** | **series** | **unit** | **tags** | **method** | **source** | **comment** |
|-----------|--------------|------------|----------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| 1   | 1 | ['DE']      | solar radiation     |    electricity |    capacity factor |      photovoltaics |      rooftop |      2016-09-30 16:00:00+01:00 |      2016-09-30 17:00:00+01:00 |      1 |      [0.014; 0] |      ToDo |      ToDo |      NUTS 2 aggregated to NUTS 1 and weighted per area |      ToDo |      ToDo |
| 2   | 1 | ['BB']      | air     |    electricity |    capacity factor |      wind turbine |      onshore |      2016-02-07 08:00:00+01:00 |      2016-02-07 09:00:00+01:00 |      1 |      [0.21546274939004; 0.140089694955441] |      ToDo |      ToDo |      NUTS 2 aggregated to NUTS 1 and weighted per area |      ToDo |      ToDo |
| 3   | 2 | TODO      | TODO     |    TODO |    TODO |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |
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


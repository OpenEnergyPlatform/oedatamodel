[![Build Status](https://travis-ci.org/OpenEnergyPlatform/edatamodel.svg?branch=develop)](https://travis-ci.org/OpenEnergyPlatform/oedatamodel)

<a href="http://oep.iks.cs.ovgu.de/"><img align="right" width="200" height="200" src="https://avatars2.githubusercontent.com/u/37101913?s=400&u=9b593cfdb6048a05ea6e72d333169a65e7c922be&v=4" alt="OpenEnergyPlatform"></a>

# Open Energy Family - Datamodel
A common open energy data model (oedatamodel) and datapackage format for energy and scenario data.

# Introduction
The oedatamodel is provided as a template data model and is designed for and used by energy system modelers. The core objective of the oedatamodel is to provide a data structure in which data from different frameworks can be stored. A uniform data basis will enable the comparability of the different models to be facilitated. Existing approaches and ideas such as the [IAMC data format](https://github.com/IAMconsortium/pyam#data-model) or [Do-a-thon: Towards a common data standard 
for integrated assessment and energy systems modelling](https://forum.openmod-initiative.org/t/do-a-thon-towards-a-common-data-standard-for-integrated-assessment-and-energy-systems-modelling/1774/5) were adopted in the development process. 

## Datamodel variations 
During development, it became apparent that the usability of datamodels that are available in a form that is primarily suitable for a database is not always comprehensible to users. For this reason, there are two variations of the oedata model. [Variation 1 Normalization](): Focuses on the avoidance of redundancies such as the same columns in different tables. The tables are normalized and are particularly suitable for installation on a database. [Variation 2 Concrete](): Efforts are made to simplify handling when a user fills in data to the tables. Data tables for scalar or time series data can be filled in as single tables. 

## Technical documentation
In this repository various resources are developed to support users in the application of the oedatamodel. 
The technical documentation is provided in the form of [entity relationship models]() (ERM). There the structure of the data model is shown on the basis of tables with column names, data types and key attributes, as well as the relationships between tables. This information is important to install the data model on a database such as [ProstgreSQL](). 

## Datapackage
As an alternative/addition to applying the data model to a database, a datapackage ([frictionless datapackage]()) was created. The datapackage consists of a datapackage.json file that documents various metadata and the datamodel. In addition to the JSON file, the datapackage also includes the data that is stored as a csv file. The datapackage format is used for data exchange and for data upload to the OEP database.

## Examples
To enhance the usability examples were created. On the one hand, there are example values for each table of the data model, which can be found in section Description and examples, and on the other hand, [template csv]() files have been created.

## Release content
The latest version can be found in the folder [oedatamodel/latest](https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop/oedatamodel/latest). Each release contains:

- ERM "OEDataModel-normalization.pdf" and "OEDataModel-concrete.pdf" 
- .er files that are used to generate the ERM .pdf files
- Datapackage with template content for "OEDataModel-concrete-datapackage" and "OEDataModel-normalization-datapackage"
 
# Installation



# Usage

##  Data conventions
### Fields that are not present or empty in your data

- When transferring data from your own data format to the oedatamodel, it may happen that fields cannot be filled properly. In this case we recommend not to leave the field empty and to insert the value "unkown" into the field.

### Delimiter and decimal sepperators

- If you insert data into the oedatamodel format make sure to use the delimiter "," in e.g. .csv files for delimiting a series of values. Decimal numbers are separated by a "." .

Example:
A series ist stored inside an array datatype, each value is delimited by ",".
| **series**         | 
|--------------------|
| [1423.55706450302, 1566.42140196079]|


## Upload a Data(-package) to the database

[Guide to publish data on the OEP](https://github.com/OpenEnergyPlatform/tutorial/blob/develop/upload/OEP_Research_Data_Publishing_Guidebook.ipynb)

TLDR:
- Create a OEP compatible [Datapackage](https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop/oedatamodel/latest/v100/datapackage/OEDataModel-concrete-datapackage)
- Start a OEP-Review process
- Start the Upload-Process 

[Guide to upload data to the OEP](https://github.com/OpenEnergyPlatform/tutorial/blob/develop/upload/OEP_Upload_Process_Data_and_Metadata_oem2orm.ipynb)

TLDR:
- Use your Datapackage files to:
    - Create Tables from the OEDataModel-Datapackage.json file usign [oem2orm](https://pypi.org/project/oem2orm/)
    - Apply OEMetadata to the table
    - Upload your data to the tables from the .csv files in OEDataModel format using Pandas with the oedialect

# Examples

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
| 3                    | ToDo         | ['North']  | ToDo.      | ToDo       | ToDo         |
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

# How to edit the Entity Relationship Modell

To generate an ERM as PDF we use a [erm tool](https://github.com/BurntSushi/erd). The [er or erd](https://github.com/BurntSushi/erd#the-er-file-format) file format offers a simple syntax and 
can be created and saved using a standard text editor.  

For the generation of the ERM e.g. in .pdf format the installation of the erm tool is necessary. For 
detailed instructions, please see the [package description](https://github.com/BurntSushi/erd#installation).   

After successful installation, a terminal/CMD must be opened and the console command (Windows: 'cd path')
must be used to navigate to the folder where the .er/.erd file is stored. To execute the tools, the command 
is then used in the Terminal/CMD to generate the ERM: 

`erd -i oedatamodel.er -o oedatamodel.pdf`


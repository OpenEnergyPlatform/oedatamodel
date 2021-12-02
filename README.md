[![Build Status](https://travis-ci.org/OpenEnergyPlatform/edatamodel.svg?branch=develop)](https://travis-ci.org/OpenEnergyPlatform/oedatamodel)

<a href="http://oep.iks.cs.ovgu.de/"><img align="right" width="200" height="200" src="https://avatars2.githubusercontent.com/u/37101913?s=400&u=9b593cfdb6048a05ea6e72d333169a65e7c922be&v=4" alt="OpenEnergyPlatform"></a>


# Open Energy Family - Datamodel
A common open energy data model (oedatamodel) and datapackage format for energy and scenario data.

# Introduction
The oedatamodel is provided as a template data model and is designed for and used by energy system modelers. The core objective of the oedatamodel is to provide a generic data structure in which data from multiple frameworks can be stored. A uniform data structure should facilitate the comparability of the different models. The oedatamodel was developed from the results of 5 energy system modeling frameworks, which include: Balomrel, oemof, genesys-mod, genesys-mod-2 and urbs. In addition existing approaches and ideas such as the [IAMC data format](https://github.com/IAMconsortium/pyam#data-model) or [Do-a-thon: Towards a common data standard 
for integrated assessment and energy systems modelling](https://forum.openmod-initiative.org/t/do-a-thon-towards-a-common-data-standard-for-integrated-assessment-and-energy-systems-modelling/1774/5) were adopted in the development process. 

## Datamodel variations 
During development, it became apparent that the usability of datamodels that are available in a form that is primarily suitable for a database is not always comprehensible to users. For this reason, there are two variations of the oedata model. 
- [Variation 1 Normalization](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v111/OEDataModel-normalization.pdf): Focuses on the avoidance of redundancies such as the same columns in different tables. The tables are normalized and are particularly suitable for installation on a database. The normalization variation consists of four tables: scenario, data, scalar and timeseries. The data table aggregates all fields that are equally relevant for scalar and timeseries data. The timeseries and sclar tables contain the raw data. 
- [Variation 2 Concrete](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v111/OEDataModel-concrete.pdf): Efforts are made to simplify handling when a user fills in data to the oedatamodel tables using file formats like .csv. The Concrete variation provides tables for scenario, scalar and timeseries data. This allows data sets to be filled in one table each for sclar or timeseries data.

## Technical documentation
The technical documentation is provided in the form of entity relationship models (ERM) see [ERM for normalization](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v111/OEDataModel-normalization.pdf) and [ERM for concrete](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v111/OEDataModel-concrete.pdf). The structure of the data model is shown on the basis of tables with column names, data types and key attributes, as well as the relationships between tables. This information is important to understand the structure and to install the data model on a database such as [ProstgreSQL](https://www.postgresql.org/). 

## Datapackage
To upload finished datasets to the OEP or to share the data outside of a database we use the [frictionless datapackage](https://frictionlessdata.io/standards/#standards-toolkit) format. A datapackage consists of a datapackage.json file that documents various metadata and the data structure. The data is stored as csv files. 

## Overview of all examples
To enhance the usability of the oedatamodel examples were created. On the one hand, there are descriptions and examples for each table of the oedatamodel concrete variation, which can be found [here](https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop#table-descrption-and-examples), and on the other hand, [template csv files](https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop/oedatamodel/latest/v111/datapackage/OEDataModel-concrete-datapackage) have been created to ease the process of data creation. 

In addition, an example of a [correctly created datapackage](https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop/examples) is provided, since a very precise procedure is important when creating it. The example datapackage contains a small part of the data from the project open_MODEX. 

## Release content
The latest version can be found in the folder [oedatamodel/latest](https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop/oedatamodel/latest). Each release contains:

- Specification of the OEDataModel as ERM "OEDataModel-normalization.pdf" and "OEDataModel-concrete.pdf" 
- .er files that are used to generate the ERM as .pdf files
- Datapackages with template content for each "OEDataModel-concrete-datapackage" and "OEDataModel-normalization-datapackage"
- Working example to get started with the OEDataModel

# Usage
Learn about the general approach to transfer data to the oedatamodel format as well as file and data conventions, oemedatamodel field descriptions and table examples that help to create correct datasets.

## General approach 

To use the oedata model for an existing project (assuming that a data structure / datamodel already exists), 2 approaches have been developed so far to migrate to the oeadatamodel format. Both approaches first require a comparison of the data fields of the currently used data structure with the available fields in the oedata model. As a result, it must be determined which fields fit together, i.e. in which field of the oedata model data can be entered: 
1. Convert "by hand": 
- data is entered manually into the oedatamodel concrete format. Then a datapackage must be created from the resulting csv files.  
2. Create mappings (upload and download): 
-  a datapackage is created with the individual/currently used data structure without any changes to the structure itself. Then a mapping that maps the fields of the individual data structure to the fields of the oedatamodel must be created using the [oedatamodel_api](https://github.com/open-modex/oedatamodel_api). This mapping can be used to upload the data to the OEP. 
- a second mapping must be created to download the data. Therefore the data on the OEP must be mapped back into the individual data format. Similar to the upload mapping, matching fields are mapped again. But this time the mapping is built from the oedatamodel normalization format to the original data structure. So exactly the other way around like the upload mapping.

## File conventions
To use the oedatamodel we recommend the use of [csv](https://en.wikipedia.org/wiki/Comma-separated_values) files to convert data from an individual data structure into the oedatamodel concrete format.  
To avoid further conflicts a ";" must be used as column/field delimiter in the csv file. The correct application is demonstrated in this [template](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v111/datapackage/OEDataModel-concrete-datapackage/OEDataModel-concrete-datapackage_scenario.csv).

##  Data conventions
### Fields that are not present or empty

- When transferring data from your own data format to the oedatamodel, it may happen that fields cannot be filled properly. In this case we recommend not to leave the field empty but to insert the value "unkown" into the field. 
- If there is no value for a field we recommend leaving the field empty as this will lead to the correct "null" value when uploading the dataset. For example: if there is no comment for a specific row in the record you can leaf the comment field empty. 

### Delimiter and decimal sepperators for data series 

- If you insert timeseries data into the oedatamodel format make sure to use the delimiter "," in e.g. .csv files for delimiting a series of values. Decimal numbers are separated by a "." .

Example:
A series ist stored inside an array datatype, each value is delimited by ",".
| **series**         | 
|--------------------|
| [1423.55706450302, 1566.42140196079]|

### Usage of single ('') and double ("") quotes 
- TBD

## Table descrption and examples

The following is intended to provide a simple example table as well as a detailed description on all fields and columns for ech tabel of the oedatamodel **concrete** variation. 

**Data model: [OEDataModel-concrete](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/OEDataModel-concrete.pdf)**

### Scenario description

| **Field**         |  **Datatype** | **Description**            |
|-------------------|---------------|----------------------------|
|   scenario id     |     int       | A primary key is a field or set of fields that uniquely identifies each row in the table. It's recorded as a list of strings, since it is possible to define the primary key as made up of several columns.                           |
|   scenario        |     text      | Name of the scenario.                           |
|   region          |     json      | It describes the geographical scope of the dataset.                           |
|   year            |     int       | It describes the time frame of the dataset.                           |
|   source          |     text      | Human readable title of the source, e.g. document title or organisation name. The source must relate to a source provided in the oemetadata (datapackage) file.                           |
|   comment         |     text      | Free text comment on what's been done.                           |

### Example table

| **scenario id** (PK) | **scenario** | **region** | **year**  | **source** | **comment**  |
|----------------------|--------------|------------|-----------|------------|--------------|
| 1                    | base         | {"DE":["BE", "BB"]}     | 2016      | modelname and/or attribution |The scenario depicts the electricity sector in Germany. It is divided into 18 nodes, 16 nodes as federal states and 2 offshore nodes. Germany's neighbouring countries are not considered.           |
| 2                    | variation1   | {"DE":["BB"]}     | 2020      | modelname and/or attribution | Some scenario descripton.         |
| 3                    | variation2   | {"DE":["BB"]}  | 2030      | modelname and/or attribution | Some scenario descripton         |
| ...                  | ...          | ...        | ...       | ...        | ...          |



### Scalar description

| **Field**              |  **Datatype** | **Description**            |
|------------------------|---------------|----------------------------|
|   scalar id            |      int      | A primary key is a field or set of fields that uniquely identifies each row in the table. It's recorded as a list of strings, since it is possible to define the primary key as made up of several columns. |
|   scenario id          |      int      | A foreign key is a field that refers to a primary key column in another table. |
|   region               |      json     | It describes the area name in which a scalar operates. |
|   input energy vector  |      text     | It describes any type of energy or energy carrier (e.g. electricity, heat, solar radiation, natural gas, ...) that enters a technology.|
|   output energy vector |      text     | It describes any type of energy or energy carrier (e.g. electricity, heat, hydrogen, LNG, CO2, ...) that exits a technology. |
|   parameter name       |      text     | It describes a considered property of an element in the energy system. It can be technology-related or technology-independent. It can refer to technological, economic or environmental characteristics. |
|   technology           |      text     | It describes an element of the modelled energy system that processes an energy vector. A technology can be real (e.g. specific type of power plant) as well as abstracted as an aggregation of energy processes or a virtual process. |
|   technology type      |      text     | Is used to specify the technology field. The specification can be technological, or freely user-defined, based on the requirements of the model.                           |
|   value                |      decimal  | Indicates the numerical value of a scalar. |
|   unit                 |      text     | Indicates the measuring unit of a value. |
|   tags                 |      json     | Is used to further describe a scalar. |
|   method               |      json     | It describes the procedure for obtaining the value, in case it does not originate from a single source. |
|   source               |      text     | Model/Framework name and source, e.g. document title or organisation name. The source must relate to a source provided in the oemetadata (datapackage) file. |
|   comment              |      text     | Free text comment on what's been done. |

### Example table

| **scalar id** (PK) | **scenario id** (FK) | **region** | **input energy vector**   | **output energy vector** | **parameter name** | **technology** | **technology type** |**value** | **unit** | **tags** | **method** | **source** | **comment** |
|-----------|--------------|------------|----------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| 1   | 1 | ["BB"]    | solar radiation | electricity | variable costs | photovoltaics | utility | 0.00 | €/MWh |       |       | modelname and/or attribution |       |
| 2   | 1 | ["BE"]      | lignite  | co2 |   output ratio |   generator | unknown | 0.40 |  t/MWh |       |       | modelname and/or attribution |       |
| 3   | 2 | ["BB"]      | electricity | electricity     |   installed capacity |   storage |     battery |      0.29 |      t/MWh |       |   {"value":"Capacity based on the date of commissioning and the remaining life of the technology"}  | modelname and/or attribution |       |
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
| 1   | 1 | ["BE"]      | electricity     |    electricity |    COP |      heat pump |     air-air |      2016-09-30 16:00:00+01:00 |      2016-09-30 17:00:00+01:00 |      1 |      [0.014; 0] |      MW |       |      NUTS 2 aggregated to NUTS 1 and weighted per area | modelname and/or attribution |       |
| 2   | 1 | ["BB"]      | air     |    electricity |    capacity factor |      wind turbine |      onshore |      2016-02-07 08:00:00+01:00 |      2016-02-07 09:00:00+01:00 |      1 |      [0.21546274939004; 0.140089694955441] |      MW |       |      NUTS 2 aggregated to NUTS 1 and weighted per area | modelname and/or attribution |       |
| ...       | ...          | ...        | ...            | ...      |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |      ... |

## Datapackge description, conventions and examples
As described in the introduction, a frictionless datapackage consists of csv files in which the data is stored and a json file named datapackage.json for metadata and to describe the data structure. Furthermore, it is important for the upload process to zip the datapackage to compress the amount of data. In this section, conventions are given for the folder structure in which the zipped datapackage must be present in order to be read. It also explains how the datapackage.json must be structured. 

### Metadata and data schema
The [datapackage.json](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/examples/Datapackage/datapackage.json) contains the name of the datapackage and describes the structure of the data tables as this example shows. This information meets the minimum requirements for a frictionless datapackage and allows validation. There are two top level keys created in the json name and resources. The resources contain several subkeys through which a detailed description of the data structure is possible. 

In the future, it should be possible to use all fields of the [oemetadata](https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/metadata/latest/example.json) to provide extensive metadata. However, this feature is still in the development stage.

### Conventions to folder structure
The folder structure is about creating a zip archive that contains the data and the datapackage.json files in an expected location so that they can technically be retrieved.
To avoid errors that can occur when uploading the datapackage, a folder structure must be maintained. However, the folder structure can be changed by modifying the datapackage.json file. To do this, the [path subkey](https://github.com/OpenEnergyPlatform/oedatamodel/blob/f230443075c8fed049a3a25a1abc94fabc54969b/examples/Datapackage/datapackage.json#L7) is adjusted under the key resources. There the exact path to the respective csv file must be deposited. The datapackage.json file should always be stored on the top level in the directory, since it is read first.

# Next Steps: Upload data(-package) to the OEP

### Create new oedatamodel tables

Before data can be uploaded to the OEP/database, the oedatamodel tables must be created on the OEP. To create tables on the OEP, the data structure of the tables is defined in a json file. The file contains all information about table names, schema, field names and data types as well as the relations between the tables. A template for the json file with all information about the tables can be found here: [OEDataModel-normalization](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v111/datapackage/OEDataModel-normalization-datapackage/OEDataModel-normalization-datapackage.json).
To distinguish the tables from other projects, a new table name must be assigned.To give tables an new name the value under the [key "name"](https://github.com/OpenEnergyPlatform/oedatamodel/blob/fac7f0318742728e0c45a2448bdaac426d85859d/oedatamodel/latest/v111/datapackage/OEDataModel-normalization-datapackage/OEDataModel-normalization-datapackage.json#L82) must be adapted. 
For example, the tables should then be then called **"project_name_oed_scenario"** etc. . This allows the oedatamodel to be used by multiple projects. To learn how to create tables on the OEP see this [Guide](https://github.com/OpenEnergyPlatform/tutorial/blob/develop/upload/OEP_Upload_Process_Data_and_Metadata_oem2orm.ipynb).

### Upload a datapackage
Subsequently, the [oedatamodel_api](https://github.com/open-modex/oedatamodel_api) can be used to upload datapackages. Datapackges can be imported to the api via a website (requires a locally installed instance of the oedatamodel_api) as a zipped Datapackage folder and then uploaded to the OEP, optinally with or without using a mapping. The datapackge is validated before the upload. The validation is very strict. In order to avoid problems here, the [datapackage example](https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop/examples) should be adhered to very precisely.

# FAQ
This section collects answers to frequently asked questions about the application of the oedatamodel. If you have a question, please create an [issue](https://github.com/OpenEnergyPlatform/oedatamodel/issues/new) in this repository or use following contact.
- Sarah.Berendes@rl-institut.de

# How to edit the Entity Relationship Modell

To generate an ERM as PDF we use a [erm tool](https://github.com/BurntSushi/erd). The [er or erd](https://github.com/BurntSushi/erd#the-er-file-format) file format offers a simple syntax and 
can be created and saved using a standard text editor.  

For the generation of the ERM e.g. in .pdf format the installation of the erm tool is necessary. For 
detailed instructions, please see the [package description](https://github.com/BurntSushi/erd#installation).   

After successful installation, a terminal/CMD must be opened and the console command (Windows: 'cd path')
must be used to navigate to the folder where the .er/.erd file is stored. To execute the tools, the command 
is then used in the Terminal/CMD to generate the ERM: 

`erd -i oedatamodel.er -o oedatamodel.pdf`


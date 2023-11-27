
.. figure:: https://user-images.githubusercontent.com/14353512/185425447-85dbcde9-f3a2-4f06-a2db-0dee43af2f5f.png
    :align: left
    :target: https://github.com/rl-institut/super-repo/
    :alt: Repo logo

.. image:: https://github.com/OpenEnergyPlatform/oedatamodel/actions/workflows/validate.yml/badge.svg
   :alt: example workflow

.. image:: https://avatars2.githubusercontent.com/u/37101913?s=400&u=9b593cfdb6048a05ea6e72d333169a65e7c922be&v=4
   :align: right
   :width: 200
   :height: 200
   :alt: OpenEnergyPlatform
   :target: http://oep.iks.cs.ovgu.de/

==============================
Open Energy Family - Datamodel
==============================

A common open energy data model (oedatamodel) and datapackage format for energy and scenario data.

.. list-table::
   :widths: auto

   * - License
     - |badge_license|
   * - Documentation
     - |badge_documentation|
   * - Publication
     -
   * - Development
     - |badge_issue_open| |badge_issue_closes| |badge_pr_open| |badge_pr_closes|
   * - Community
     - |badge_contributing| |badge_contributors| |badge_repo_counts|

.. contents::
    :depth: 2
    :local:
    :backlinks: top

Introduction
==============================

The oedatamodel is provided as a template data model and is designed for and used by energy system modelers. The core objective of the oedatamodel is to provide a generic data structure in which data from multiple frameworks can be stored. A uniform data structure should facilitate the comparability of the different models. The oedatamodel was developed from the results of 5 energy system modeling frameworks, which include: Balomrel, oemof, GENeSYS-MOD, GENESYS-2 and urbs. In addition, existing approaches and ideas such as the `IAMC data format <https://github.com/IAMconsortium/pyam#data-model>`_ or `Do-a-thon: Towards a common data standard for integrated assessment and energy systems modelling <https://forum.openmod-initiative.org/t/do-a-thon-towards-a-common-data-standard-for-integrated-assessment-and-energy-systems-modelling/1774/5>`_ were adopted in the development process.

Datamodel Variations
==============================

During development, it became apparent that the usability of datamodels that are available in a form that is primarily suitable for a database is not always comprehensible to users. For this reason, there are two variations of the oedata model:

- `Variation 1 Normalization <https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v111/OEDataModel-normalization.pdf>`_: Focuses on the avoidance of redundancies such as the same columns in different tables. The tables are normalized and are particularly suitable for installation on a database.
- `Variation 2 Concrete <https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v111/OEDataModel-concrete.pdf>`_: Efforts are made to simplify handling when a user fills in data to the oedatamodel tables using file formats like .csv.

Technical Documentation
==============================

The technical documentation is provided in the form of entity relationship models (ERM) see `ERM for normalization <https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v111/OEDataModel-normalization.pdf>`_ and `ERM for concrete <https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v111/OEDataModel-concrete.pdf>`_. The structure of the data model is shown on the basis of tables with column names, data types and key attributes, as well as the relationships between tables.

Datapackage
==============================

To upload finished datasets to the OEP or to share the data outside of a database we use the `frictionless datapackage <https://frictionlessdata.io/standards/#standards-toolkit>`_ format. Validation: We provide a GitHub action (CI) workflow that validates the datapackage json files for each oedatamodel variation against the latest version of the `oemetadata schema.json <https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/metadata/latest/schema.json>`_.

Overview of All Examples
==============================

To enhance the usability of the oedatamodel examples were created. Descriptions and examples for each table of the oedatamodel concrete variation can be found `here <https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop#table-descrption-and-examples>`_, and template csv files have been created to ease the process of data creation. An example of a correctly created datapackage is provided `here <https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop/examples>`_.

Release Content
==============================

The latest version can be found in the folder `oedatamodel/latest <https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop/oedatamodel/latest>`_. Each release contains specification of the OEDataModel as ERM, .er files for generating the ERM as .pdf files, Datapackages with template content, and working examples.

Usage
=====

Learn about the general approach to transfer data to the oedatamodel format, file and data conventions, oedatamodel field descriptions, and table examples that help to create correct datasets.

General Approach
==============================

To use the oedata model for an existing project, two approaches have been developed to migrate to the oedatamodel format. Both approaches first require a comparison of the data fields of the currently used data structure with the available fields in the oedata model.

File Conventions
==============================

To use the oedatamodel, we recommend the use of csv files to convert data from an individual data structure into the oedatamodel concrete format. To avoid conflicts, a ";" must be used as column/field delimiter in the csv file. The correct application is demonstrated in this `template <https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v111/datapackage/OEDataModel-concrete-datapackage/OEDataModel-concrete-datapackage_scenario.csv>`_.


Data Conventions
==============================

**Fields that are not Present or Empty**

- When transferring data from your own data format to the oedatamodel, it may happen that fields cannot be filled properly. In this case, it's recommended not to leave the field empty but to insert the value "unknown".
- If there is no value for a field, it's recommended to leave the field empty as this will lead to the correct "null" value when uploading the dataset. For example, if there is no comment for a specific row in the record, leave the comment field empty.

**Delimiter and Decimal Separators for Data Series**

- For timeseries data in the oedatamodel format, use the delimiter "," in .csv files for delimiting a series of values. Decimal numbers are separated by a ".".

  Example:

  A series is stored inside an array datatype, each value is delimited by ",".

  .. code-block:: none

     | **series**         |
     |--------------------|
     | [1423.55706450302, 1566.42140196079]|

**Usage of Single ('') and Double ("") Quotes**

- TBD

Table Description and Examples
==============================

**Data Model: `OEDataModel-concrete <https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/OEDataModel-concrete.pdf>`_**

**Scenario Description**

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - **Field**
     - **Datatype**
     - **Description**
   * - scenario id
     - int
     - A primary key uniquely identifies each row in the table.
   * - scenario
     - text
     - Name of the scenario.
   * - region
     - json
     - Describes the geographical scope of the dataset.
   * - year
     - int
     - Time frame of the dataset.
   * - source
     - text
     - Human readable title of the source.
   * - comment
     - text
     - Free text comment on what's been done.

**Example Table**

.. code-block:: none

   | **scenario id** (PK) | **scenario** | **region** | **year**  | **source** | **comment**  |
   |----------------------|--------------|------------|-----------|------------|--------------|
   | 1                    | base         | {"DE":["BE", "BB"]} | 2016 | modelname and/or attribution | The scenario depicts the electricity sector in Germany. |
   | 2                    | variation1   | {"DE":["BB"]} | 2020 | modelname and/or attribution | Some scenario description. |
   | 3                    | variation2   | {"DE":["BB"]} | 2030 | modelname and/or attribution | Some scenario description |
   | ...                  | ...          | ...        | ...      | ...        | ...          |

**Scalar Description**

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - **Field**
     - **Datatype**
     - **Description**
   * - scalar id
     - int
     - A primary key uniquely identifies each row in the table.
   * - scenario id
     - int
     - A foreign key that refers to a primary key column in another table.
   * - region
     - json
     - Describes the area name in which a scalar operates.
   * - input energy vector
     - text
     - Describes any type of energy or energy carrier that enters a technology.
   * - output energy vector
     - text
     - Describes any type of energy or energy carrier that exits a technology.
   * - parameter name
     - text
     - Describes a considered property of an element in the energy system.
   * - technology
     - text
     - Describes an element of the modelled energy system that processes an energy vector.
   * - technology type
     - text
     - Specifies the technology field.
   * - value
     - decimal
     - Indicates the numerical value of a scalar.
   * - unit
     - text
     - Indicates the measuring unit of a value.
   * - tags
     - json
     - Further describes a scalar.
   * - method
     - json
     - Describes the procedure for obtaining the value.
   * - source
     - text
     - Title of the source, must relate to a source in the oemetadata file.
   * - comment
     - text
     - Free text comment on what's been done.

**Example Table**

.. code-block:: none

   | **scalar id** (PK) | **scenario id** (FK) | **region** | **input energy vector** | **output energy vector** | **parameter name** | **technology** | **technology type** | **value** | **unit** | **tags** | **method** | **source** | **comment** |
   |--------------------|----------------------|------------|-------------------------|--------------------------|---------------------|----------------|---------------------|-----------|----------|----------|-------------|------------|-------------|
   | 1                  | 1                    | ["BB"]     | solar radiation         | electricity              | variable costs      | photovoltaics  | utility             | 0.00      | €/MWh    |          |             | modelname  |             |
   | 2                  | 1                    | ["BE"]     | lignite                 | co2                      | output ratio        | generator      | unknown             | 0.40      | t/MWh    |          |             | modelname  |             |
   | 3                  | 2                    | ["BB"]     | electricity             | electricity              | installed capacity  | storage        | battery             | 0.29      | t/MWh    |          | JSON example| modelname  |             |
   | ...                | ...                  | ...        | ...                     | ...                      | ...                 | ...            | ...                 | ...       | ...      | ...      | ...         | ...        | ...         |


Timeseries Description
==============================

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - **Field**
     - **Datatype**
     - **Description**
   * - timeseries id
     - int
     - A primary key uniquely identifies each row in the table.
   * - scenario id
     - int
     - A foreign key referring to a primary key in another table.
   * - region
     - json
     - Describes the area name in which a timeseries operates.
   * - input energy vector
     - text
     - Describes energy or energy carriers entering a technology.
   * - output energy vector
     - text
     - Describes energy or energy carriers exiting a technology.
   * - parameter name
     - text
     - Describes a property of an element in the energy system.
   * - technology
     - text
     - Describes an element processing an energy vector.
   * - technology type
     - text
     - Specifies the technology field.
   * - timeindex start
     - timestamp
     - Date and time, with time zone.
   * - timeindex stop
     - timestamp
     - Date and time, with time zone.
   * - timeindex resolution
     - interval
     - Time span between points in a time series.
   * - series
     - [decimal]
     - Series of values, from start to stop.
   * - unit
     - text
     - Measuring unit of a value.
   * - tags
     - json
     - Further describes a timeseries.
   * - method
     - json
     - Procedure for obtaining the value.
   * - source
     - text
     - Title of the source, must relate to a source in oemetadata.
   * - comment
     - text
     - Free text comment.

Example Table
==============================

.. code-block:: none

   | **timeseries id** (PK) | **scenario id** (FK) | **region** | **input energy vector** | **output energy vector** | **parameter name** | **technology** | **technology type** | **timeindex start** | **timeindex stop** | **timeindex resolution** | **series** | **unit** | **tags** | **method** | **source** | **comment** |
   |------------------------|----------------------|------------|-------------------------|--------------------------|---------------------|----------------|---------------------|---------------------|--------------------|-------------------------|-------------|----------|----------|-------------|------------|-------------|
   | 1                      | 1                    | ["BE"]     | electricity             | electricity              | COP                 | heat pump      | air-air             | 2016-09-30 16:00:00+01:00 | 2016-09-30 17:00:00+01:00 | 1                       | [0.014; 0] | MW       |          | NUTS 2 aggregated to NUTS 1 and weighted per area | modelname and/or attribution |             |
   | 2                      | 1                    | ["BB"]     | air                     | electricity              | capacity factor     | wind turbine   | onshore             | 2016-02-07 08:00:00+01:00 | 2016-02-07 09:00:00+01:00 | 1                       | [0.21546274939004; 0.140089694955441] | MW       |          | NUTS 2 aggregated to NUTS 1 and weighted per area | modelname and/or attribution |             |
   | ...                    | ...                  | ...        | ...                     | ...                      | ...                 | ...            | ...                 | ...                 | ...                | ...                     | ...         | ...      | ...      | ...         | ...        | ...         |

Datapackage Description, Conventions and Examples
==================================================

As described in the introduction, a frictionless datapackage consists of CSV files for data storage and a JSON file named `datapackage.json` for metadata and data structure description. It's important to zip the datapackage for the upload process to compress the amount of data. This section provides conventions for the folder structure in which the zipped datapackage must be present to be read and explains how the `datapackage.json` must be structured.

**Metadata and Data Schema**

The `datapackage.json` contains the name of the datapackage and describes the data tables' structure. This information meets the minimum requirements for a frictionless datapackage and allows validation. There are two top-level keys created in the JSON: `name` and `resources`. The `resources` contain several subkeys for a detailed description of the data structure.

In the future, it should be possible to use all fields of the [oemetadata](https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/metadata/latest/example.json) to provide extensive metadata.

**Conventions to Folder Structure**

The folder structure is about creating a zip archive that contains the data and the `datapackage.json` files in an expected location so that they can technically be retrieved. To avoid errors when uploading the datapackage, a folder structure must be maintained. The folder structure can be changed by modifying the `datapackage.json` file. To do this, adjust the `path` subkey under the `resources` key to specify the exact path to the respective CSV file. The `datapackage.json` file should always be stored on the top level in the directory.

Next Steps: Upload Data(-package) to the OEP
============================================

**Create New Oedatamodel Tables**

Before data can be uploaded to the OEP/database, the oedatamodel tables must be created on the OEP. To create tables on the OEP, define the data structure of the tables in a JSON file containing all information about table names, schema, field names, and data types, as well as the relations between the tables. A template for the JSON file with all information about the tables can be found here: [OEDataModel-normalization](https://github.com/OpenEnergyPlatform/oedatamodel/blob/develop/oedatamodel/latest/v111/datapackage/OEDataModel-normalization-datapackage/OEDataModel-normalization-datapackage.json). Assign a new table name to distinguish the tables from other projects. For example, the tables could be called **"project_name_oed_scenario"** etc. This allows multiple projects to use the oedatamodel.

**Upload a Datapackage**

Subsequently, use the [oedatamodel_api](https://github.com/open-modex/oedatamodel_api) to upload datapackages. Datapackages can be imported to the API via a website (requires a locally installed instance of the oedatamodel_api) as a zipped Datapackage folder and then uploaded to the OEP, optionally with or without using a mapping. The datapackage is validated before the upload. The validation is strict. Adhere precisely to the [datapackage example](https://github.com/OpenEnergyPlatform/oedatamodel/tree/develop/examples) to avoid problems.

FAQ
===

This section collects frequently asked questions about the application of the oedatamodel. If you have a question, please create an [issue](https://github.com/OpenEnergyPlatform/oedatamodel/issues/new) in this repository or use the following contact:

- Sarah.Berendes@rl-institut.de

How to Edit the Entity Relationship Model
=========================================

To generate an ERM as PDF, use the [erm tool](https://github.com/BurntSushi/erd). The [er or erd](https://github.com/BurntSushi/erd#the-er-file-format) file format offers a simple syntax and can be created using a standard text editor.

For generating the ERM (e.g., in .pdf format), install the erm tool. For detailed instructions, see the [package description](https://github.com/BurntSushi/erd#installation).

After installation, open a terminal/CMD and navigate to the folder where the .er/.erd file is stored. Use the following command to generate the ERM:

erd -i oedatamodel.er -o oedatamodel.pdf


.. |badge_license| image:: https://img.shields.io/github/license/OpenEnergyPlatform/oedatamodel
    :target: LICENSE.txt
    :alt: License

.. |badge_documentation| image::
    :target:
    :alt: Documentation

.. |badge_contributing| image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
    :alt: contributions

.. |badge_repo_counts| image:: http://hits.dwyl.com/OpenEnergyPlatform/oedatamodel.svg
    :alt: counter

.. |badge_contributors| image:: https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square
    :alt: contributors

.. |badge_issue_open| image:: https://img.shields.io/github/issues-raw/OpenEnergyPlatform/oedatamodel
    :alt: open issues

.. |badge_issue_closes| image:: https://img.shields.io/github/issues-closed-raw/OpenEnergyPlatform/oedatamodel
    :alt: closes issues

.. |badge_pr_open| image:: https://img.shields.io/github/issues-pr-raw/OpenEnergyPlatform/oedatamodel
    :alt: closes issues

.. |badge_pr_closes| image:: https://img.shields.io/github/issues-pr-closed-raw/OpenEnergyPlatform/oedatamodel
    :alt: closes issues

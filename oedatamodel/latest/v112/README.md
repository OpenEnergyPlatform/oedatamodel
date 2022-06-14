# Oedatamodel v1.1.2 - Technical description 

The oedatamodel release version 1.1.2 contains two datamodel´s as UML-ERM and the corresponding datapackage
for each datamodel. This section describes the technical aspects for each datamodel. 

Oedatamodel v1.1.2 now supports bandwidths for scalars (see related issue [#52](https://github.com/OpenEnergyPlatform/oedatamodel/issues/52))
and timeseries. In order to achieve this, scalar table contains new keys `bandwidth` and `bandwidth_type` instead of `value`.
The related scalars and timeseries for a scenario are now defined via tables "scalar_instance" and "timeseries_instance", 
which are both connected to a corresponding scalar or timeseries entry. In case of "scalar_instance", the chosen value
has to be set in column `value`. In case of "timeseries_instance", the related timeseries for the scenario is selected 
and other timeseries (within the bandwidth) are neglected.

We have created two variants of the data model to achieve different results. First we needed a good solution for 
the application of the data model in a database environment. For this purpose we have created 
"OEDataModel-normalization". This data model is developed as a [joint-table inheritance](https://docs.sqlalchemy.org/en/13/orm/inheritance.html#joined-table-inheritance) 
data model and is in a [normalized](https://en.wikipedia.org/wiki/Database_normalization#Example_of_a_step_by_step_normalization) state. 
By normalizing the data model we eliminate redundancies (within columns) and ensure that the data model meets the 
general requirements of data to be stored on a relational database system. Common table inheritance is our solution for 
the redundancy in the data tables "timeseries" and "scalar". We introduced an aggregated "data" table to 
the data model. The "data" table contains all redundant fields from the "timeseries" data and "scalar" data tables.
By introducing a shared primary key "data_id" in all data related tables and by introducing a new field in 
aggregated "data" table named "type" we can define the data type ("scalar" or "time series") for each row in the
Table. When retrieving the data, SQL allows us to connect the data tables with each other and create a readable 
joint record. 

The other data format is called "OEDataModel-concrete". This format is intended to be more user-friendly when working 
with datasets, for example, using a tool like Excel. The usability aspect that we wanted to achieve with this data 
model is to allow a user to edit a dataset in a table that contains all fields. Since we need to map this 
approach back to the "OEDataModel-normalization" data model, an adapter is required. This adapter has been developed 
within the Open_MODEX project and is available as [OEDatamobel_API](https://github.com/open-modex/oedatamodel_api).

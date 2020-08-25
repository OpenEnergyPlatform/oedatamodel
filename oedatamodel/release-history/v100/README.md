# Oedatamodel v1.0.0 - Technical description 

The oedatamodel release version 1.0.0 contains two datamodel´s as UML-ERM and the corresponding datapackage
for each datamodel. This section describes the technical aspects for each datamodel. 

We have created two variants of the data model to achieve different results. First we needed a good solution for 
the application of the data model in a database environment. For this purpose we have created "OEDataModel-normalization".
This data model is developed as a [joint-table inheritance](https://docs.sqlalchemy.org/en/13/orm/inheritance.html#joined-table-inheritance) data model and is in a [normalized](https://en.wikipedia.org/wiki/Database_normalization#Example_of_a_step_by_step_normalization) state. By normalizing the 
data model we eliminate redundancies (within columns) and ensure that the data model meets the general requirements of
Data to be stored on a relational database system. Common table inheritance is our solution for 
the redundancy in the data tables "timeseries" and "scalar". We introduced an aggregated "data" table to 
the data model. The "data" table contains all redundant fields from the "timeseries" data and "scalar" data tables.
By introducing a shared primary key "data_id" in all data related tables and by introducing a new field in 
aggregated "data" table named "type" we can define the data type ("scalar" or "time series") for each row in the
Table. When retrieving the data, SQL allows us to connect the data tables with each other and create a readable 
joint record. 


The other result is called "OEDataModel-concrete". This format is intended to be more user-friendly when working 
with datasets, for example, using a tool like Excel. The usability aspect that we wanted to achieve with this data 
model is to allow a user to edit a dataset in a table that contains all fields. This leads to a lot of redundant 
fields. In the data related tables, but the usability is much better for this use case. Since we need to map this 
approach to the "OEDataModel-joint" data model, the development of an adapter is required. We plan the development 
of the adapter within the next iterations of the development process. 

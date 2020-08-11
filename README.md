# oedatamodel
A common open energy data model (oedatamodel) and datapackage format for energy and scenario data.

# Introduction
The oedatamodel is provided as a template data model as Entity Relationship Modell(ERM) and is designed
for the usage on the open energy platform but it can be used in common relational database systems. 

Existing approaches and ideas such as the [IAMC data format](https://github.com/IAMconsortium/pyam#data-model) or [Do-a-thon: Towards a common data standard 
for integrated assessment and energy systems modelling](https://forum.openmod-initiative.org/t/do-a-thon-towards-a-common-data-standard-for-integrated-assessment-and-energy-systems-modelling/1774/5) were adopted in the development process.

The latest version can be found in the folder oedatamodel/latest. 
The version available there offers the user 2 ERM's. The ERM "oedatamodel.pdf" shows the data model 
that can be implemented on a database (e.g. postgresql). Here tables, relations and column names and 
data types are provided. The ERM "oedatamodel-readable.pdf" is provided additionally and is designed 
to simplify the editing of the data by a user. It also provides tables and relations as well as column 
names and datatypes, but the tables are in a less normalized format. We recommend this version of the 
data model for the implementation in e.g. csv tables because the advantage of the human readable format 
is not optimal for the technical usage in a database. 

In addition, the raw files (file format: .er) from which the PDF respectively the ERM is generated are
also provided for each data model.

 
# Edit the Entity Relationship Modell

For the generation of an ERM we use this [erm tool](https://github.com/BurntSushi/erd). The [er or erd](https://github.com/BurntSushi/erd#the-er-file-format) file format offers a simple syntax and 
can be created and saved using a standard text editor.  

For the generation of the ERM e.g. in .pdf format the installation of the erm tool is necessary. For 
detailed instructions, please see the [package description](https://github.com/BurntSushi/erd#installation).   

After successful installation, a terminal/CMD must be opened and the console command (Windows: 'cd path')
must be used to navigate to the folder where the .er/.erd file is stored. To execute the tools, the command 
is then used in the Terminal/CMD to generate the ERM: 

`erd -i oedatamodel.er -o oedatamodel.pdf`


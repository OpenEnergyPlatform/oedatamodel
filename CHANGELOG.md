# Changelog

All notable changes to this project will be documented in this file.

The format is inspired from [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and the versioning aim to respect [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

Here is a template for new release sections

```
## Current

### Added
-
### Changed
-
### Removed
-

## [_._._] - 20XX-MM-DD

### Added
-
### Changed
-
### Removed
-
```
## Current

### Added
- Improve description for each posssible table (column)
- Provide table examples 

### Changed
- Change OEDataModel Primary Key column names to "id" to support OEP API requirments [PR#30]
- Added new 'year' column to scalar table model [Issue#29]
- Updated ERM with datamodel changes 

## [1.0.0] Initial release

### Added
- ERM as pdf file format
- ERM as er file format
- datamodel is documented as ERM
- datamodel as joint table inheritance model and normalized 
- datamodel as concrete table inheritance model and human readable 
- datapackage for each datamodel 


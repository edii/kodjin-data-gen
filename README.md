# kodjin.data.generator

This project is a tool for generating synthetic datasets.

# Project sturcture

- The root directory contains Python source code and project configuration.
- `data/templates` contains Jinja templates that define the JSON structure.
- `data/terminology` contains FHIR CodeSystem and ValueSet resources representing various sets of codes used during generation, such as claim types, ICD-10 procedure codes, patient occupations and others.
- `data/weights` contains weight data for the terminology resources under `data/terminology`. This allows various terminology codes to be picked with the same prevalence as their appearance in real world data.
- `data` also contains some files with statistics that is handled separately from FHIR terminology, such as patient demographics and names.

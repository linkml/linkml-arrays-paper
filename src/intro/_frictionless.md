> The initial idea when the Frictionless Data project was started, 
> more than ten years ago, was for it to be mainly  about standards with 
> a few small code library implementations. 
> In time, it became clear that the standards  alone are not enough, 
> and that technical implementation of the standards is also crucial. 
> The focus has now  shifted to integration, and adoption. 
> A rich set of tools has been developed, 
> including a powerful Python  framework to describe, extract, validate, and transform tabular data.

@pettiFrictionlessDataStandards2022


- Standards: [DataPackage](https://datapackage.org/)
  - [DataResource](https://datapackage.org/standard/data-resource/) - single file
- attrs
  - project-based
  - metadata/resources split
  - 
- tools
  - [dataflows](https://www.dataflows.org/) - holy cow what a website 

Schema structure is very simple:

**Descriptor** - metadata definition of the dataset, v similar to a `pyproject.toml`,
`project.json`, `Cargo.toml`, etc. file. Linked to its data via a `sources` property:

```json
{
  "sources": [
    {
      "title": "World Bank and OECD",
      "path": "http://data.worldbank.org/indicator/NY.GDP.MKTP.CD"
    }
  ]
}
```

Then within that very general manifest of files one uses some additional descriptors for data types

eg. for tables one has various descriptions of serializations:

`````{tab-set}
````{tab-item} Delimited
```json
{
  "header": false,
  "commentChar": "#"
  "delimiter": ";",
  "doubleQuote": true,
  "lineTerminator": "\r\n",
  "quoteChar": "\"",
  "skipInitialSpace": true,
}
```
````
````{tab-item} Spreadsheet
```json
{
    "$schema": "https://datapackage.org/profiles/1.0/tabledialect.json"
    "header": "true"
    "headerRows": "1"
    "headerJoin": null
    "commentRows": "undefined" 
    "commentChar": "undefined" 
    "sheetNumber": 1
    "sheetName": "undefined"
}
```
```
````
````{tab-item} Database
```json
{
  "$schema": "https://datapackage.org/profiles/1.0/tabledialect.json",
  "table": "(name of a table in a database)"
}
```
````
`````

which expects the data to be in a text format,

and then one has a [table schema](https://datapackage.org/standard/table-schema/) for defining the data within a table:

```json
{
  "fields": [
    {
      "name": "name of field (e.g. column name)",
      "title": "A nicer human readable label or title for the field",
      "type": "A string specifying the type",
      "format": "A string specifying a format",
      "example": "An example value for the field",
      "description": "A description for the field",
      "constraints": {
        "required": true,
        "unique": true,
        "minLength": 0,
        "maxLength": 0,
        "minimum": 0,
        "maximum": 0,
        "jsonSchema": {"...":  "..."},
        "...":  "..."
      }
    },
    {"...": "..."}
  ],
  "fieldsMatch": ["exact", "equal", "subset", "superset", "partial"],
  "missingValues": [ "..." ],
  "primaryKey": [ "..." ],
  "foreignKeys": ["..." ],
  "uniqueKeys": ["..."]
}
```

problems are that the extensions quickly become subdialects - 
not enough interop in the schema language itself. e.g. the [fiscal data package](https://specs.frictionlessdata.
io/fiscal-data-package/)

Data can be stored in literal formats, but also referred to as [data resources](https://framework.frictionlessdata.io/docs/resources/json.html)

```json
{"name": "data",
 "type": "json",
 "path": "data.json",
 "scheme": "file",
 "format": "json",
 "mediatype": "text/json",
 "encoding": "utf-8",
 "hash": "sha256:80af3283a5c57e5d3a8d1d4099bebe639c610c4ecc8ce39fe53f9f9d9c441c4a",
 "bytes": 21}

```

```{draft}
which is great! but it's still a tight link between the dataset and a particular serialization
```

![Frictionless loader pattern](https://framework.frictionlessdata.io/assets/reading.png)


**Properties**
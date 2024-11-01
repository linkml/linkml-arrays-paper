# Prior Art

## Open Science, FAIR Data, and Formats

```{draft} outline
- Whats goin down with open science and shit
  - FAIR data, ya ya we've all heard that, but like how does that map onto practice
  - formats as a critical infrastructural medium between the goals of open science
    and the reality of scientific work
- What are data formats anyway?
- Which ones are we talking about?
  - e.g. there are tons of formats for the raw data, sample all the ones in 
    spikeinterface or nwb conversion tools or whatever it's called now.
  - that's not really what we're talking about
  - instead we're talking about formats intended for interchange of open scientific data
  - typically these are domain-specific by necessity...
```


## The Open Data Format Stack

```{draft} outline
- Components of a scientific data format
  - Schema language
    - eg. @pettiFrictionlessDataStandards2022 [frictionless data](https://framework.frictionlessdata.
    io/docs/getting-started.html)'s schema, where 
  - Schema
  - programmatic API, user-facing tools, ways of interacting with it
  - serialization - data on disk
  - overlay infrastructure - indexing, archiving, etc.
  - governance - how the format evolves, facility for researchers to change/extend
    - distinct from an API, which is how we use the thing as it exists,
      but equally important to the technical reality of the format is
      how researchers are able to change it to make it meet their needs
- modalities
  - tables
  - trees (json-like)
  - ... but whence arrays?
```

## How formats bundle the stack

- Survey of some neuro-/bio-/med-specific formats

### NWB

### BIDS

### Frictionless data

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

## Linked Open Data

```{draft} outline
- Prior art on representing bulk data in RDF-like things
- The status of LoD as infrastructure: where does it exist? how is it used?
- Part of what is pinning us to the journal system is that it's simply impractical
  to actually have any generic indexing system for scientific data.
  it wouldn't be meaningful, and you wouldn't be able to access the data anyway.
  (e.g. @kinneySemanticScholarOpen2023 - why is that kind of graph of scholarship
  limited strictly to bibliometric data?)
- Meanwhile the NIH is pushing ahead on the Biomedical Translator project,
  and the NSF is doing the same on OKN, and there isn't really a good
  strategy for dealing with bulk data except for "pay a bazillion dollars to
  dump it onto the cloud." Most of that tech is built for scalar data,
  traditional KGs to do "AI" inference off of rather than actually handling
  primary research data
  
```

From the other side... we have linked data, which has done great things with
scalar values, but so far has settled for being able to describe the
metadata in scientific datasets. 

## Problems

```{draft} outline
- which parts are fixed in place?
    - to some degree that's what standards *are*, some assemblage of fixed, agreed-on
      components, and navigating that fluid boundary between mutual intelligibility
      and expressiveness is the whole challenge
    - e.g. frictionless data, bids, etc. a fixed number of types with no means of expressing more
- there's not really any reason for most scientists or programmers to use data standards
  - most are archival standards, ways to structure data, and sometimes adjoining tooling for analysing and visualizing,
    but they are not well suited to data acquisition, HPC, realtime computing, etc.  
  - So there's a gulf between web-ready, lightweight, scalar and tabular data formats and huge heterogeneous binary 
  data and encoded data
  - need to have practical benefit for researchers and tool developers alike
```



---

## Notes

```{draft}
theez are all scraps as i'm working on the draft text above.
Mostly preserving the lists ryan made on the scoping issue.
```

## Data Formats

```{draft}

- HDMF
- [CORAL](https://github.com/jmchandonia/CORAL)
- [NeXus](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4453170/)
- netCFG?
- OME-NGFF
- geospatial data?
- JSON Schema Arrays
- [DataCite](https://schema.datacite.org/)
- [DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [Research Object Bundle](https://www.researchobject.org/specifications/bundle/)
- Neuroimaging Data Model
```

## Serialization Formats

A million of em

- binary file
- numpy npy/npz
- HDF5
- Zarr
- N5
- JSON
- CSV/TSV
- grib
- tiff
- fits


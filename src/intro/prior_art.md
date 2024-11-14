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
  - Vocabulary - things that exist
  - Schema - rules and structure about things that exist
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

```{include} _frictionless.md
```

### FASTA/FASTQ

https://academic.oup.com/nar/article/38/6/1767/3112533?login=false
great example of *de facto* data format that has a pretty messy ontology/serialization format history

### SAM/BAM/CRAM/MIGS/MIxS

https://github.com/samtools/hts-specs
https://www.gensc.org/pages/standards-intro.html
http://samtools.github.io/hts-specs/CRAMv3.pdf

### Astronomy - FITS

https://fits.gsfc.nasa.gov/fits_primer.html

### High Energy Physics - ROOT

https://root.cern/


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

### Examples

Mostly ontologies and vocabularies! 
Useful for metadata, not useful for actual research data 
(or at least not usable by researchers using research data).

- DataCite
- NCBI Taxonomy
- Gene Ontology
- DOIs
- https://fairsharing.org/search?fairsharingRegistry=Standard&isMaintained=true&page=1&isRecommended=true&status=ready


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


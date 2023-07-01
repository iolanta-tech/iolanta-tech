---
title: "∗-LD"
exclude_from_blog: true
description: Review of available & future serialization formats for Linked Data.
$included:
  - $id: endemic-formats-table
    table:columns:
      - table:self
      - popularity
    table:class:
      $id: EndemicFormat
      $reverse:
        rdf:type:
          - schema:url: …
            rdfs:label: Turtle
          - schema:url: …
            rdfs:label: N3
          - schema:url: …
            rdfs:label: TriG

  - $id: mapped-formats-table
    table:columns:
      - rdfs:label: Underlying format
        table:columns:
          - underlying-format
          - underlying-format-popularity
      - rdfs:label: Linked Data format
        table:columns:
          - table:self
          - popularity
    table:class:
      $id: MappedFormat
      $reverse:
        rdf:type:
          - schema:url: …
            rdfs:label: RDF/XML
            underlying-format:
              rdfs:label: XML
              schema:url: …
          - schema:url: …
            rdfs:label: JSON-LD
            underlying-format:
              rdfs:label: JSON
              schema:url: …
          - schema:url: …
            rdfs:label: YAML-LD
            underlying-format:
              rdfs:label: YAML
              schema:url: …
          - schema:url: …
            rdfs:label: Protobuf-LD
            underlying-format:
              rdfs:label: Protobuf
              schema:url: …
          - schema:url: …
            rdfs:label: Parquet-LD
            underlying-format:
              rdfs:label: Parquet
              schema:url: …
          - schema:url: …
            rdfs:label: Avro-LD
            underlying-format:
              rdfs:label: Avro
              schema:url: …
          - schema:url: …
            rdfs:label: CSV-LD
            underlying-format:
              rdfs:label: CSV
              schema:url: …
          - schema:url: …
            rdfs:label: CBOR-LD
            underlying-format:
              rdfs:label: CBOR
              schema:url: …
---

# :material-asterisk:-LD

!!! abstract
    {{ page.meta.description }}

## Endemic formats

{{ render("endemic-formats-table") }}

## Mapped formats

{{ render("mapped-formats-table") }}

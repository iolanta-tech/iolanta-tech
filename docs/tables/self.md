---
title: "table:self"
hide:
  - toc
---

Use this as a column (in {{ render("table:columns") }} and perhaps in {{ render("table:order-by") }}) to render a representation of the whole row instead of a particular column.

With default implementation this means that the following properties will be taken in account for rendering:

* {{ render("rdfs:label") }}
* {{ render("schema:url") }}

{{ render("self", environments="side-by-side") }}

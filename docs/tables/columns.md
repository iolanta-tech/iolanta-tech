---
title: "table:columns"
$id: table:columns
---

# :material-view-column: `table:columns`

List columns of a table. Order is preserved.

## Shorthand

{{ code("samples/simple.yaml", language="yaml", first_line=2, last_line=6) }}

Every column listed in this format is a global identifier (is interpreted as {{ render("keyword-id") }}). However, in this form you cannot define `title` or other properties of a column. For that, the longhand form is required.

## Lengthy form

{{ code("samples/arda-countries.yaml", language="yaml", first_line=2, last_line=5) }}

The nature of `country-name` as a global identifier is now revealed.

## Nested columns

{{ code("tables/examples/earth-like-planets.yaml", language="yaml", first_line=2, last_line=10) }}

See result at the home page for {{ render("iolanta-tables") }}.

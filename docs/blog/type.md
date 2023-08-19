---
$id: type-comparison
table:columns:
    - $id: keyword
      rdfs:label: Keyword
    - $id: context
      rdfs:label: Context
    - $id: usage
      rdfs:label: Usage
    - $id: example
      rdfs:label: Example
    - $id: inline-type-description
      rdfs:label: Describe type inline
    - $id: typed-literals
      rdfs:label: Specify Types of Literals?

table:rows:
    - keyword: "$type | @type"
      context: JSON-LD
      usage: "Sets data type of a node or value."
      inline-type-description: no
      typed-literals: yes

    - keyword: "rdf:type"
      context: RDF
      usage: "States a resource is an instance of a class."
      inline-type-description: yes
      typed-literals: no
---

# `rdf:type` vs `"@type"`/`$type`

These two methods both are used to specify types, but they're not interchangeable.

{{ render("type-comparison") }}

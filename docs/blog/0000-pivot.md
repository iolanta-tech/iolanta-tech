---
title: "Pivot: Visualization system → Knowledge As Code workspace"
$id: pivot

roadmap:roadmap:
  - $id: pivot
    is-blocked-by:
      - title: Research whether there are Notion As Code projects already
      - title: Choose Notion use case(s) to reproduce
      - title: Abstract → AIST Conf
      - title: Rebuild the front page
      - title: "`{{ render() }}` → `{{ iolanta() }}` or some kind of a DSL"
      - title: Editing experience
      - title: "Shorthand for $reverse + rdf:type"
      - title: Import from Notion
        is-blocked-by:
          - title: Support CSV-LD
---

## Context

At this moment, Iolanta is called a "Linked Data visualization framework". From this name, no particular target audience is evident.

* **What is Linked Data?** — pretty much no one knows, and those who know believe this is something esoteric
* **What is a visualization framework?** — from these words, a software developer will infer a meaning which has nothing in common with what Iolanta actually is.

## Decision

Iolanta is now a **Knowledge as Code** workspace. Its nearest competitor is Notion. Its comparative advantage is that it manages knowledge in code rather than via ClickOps. Its primary use case **at this point** is documentation for software projects, because: 

* Notion already has penetrated that space and we have a base to jump start from
* Software projects are managed by developers, and developers know why code rulez

## Consequences

{{ render("pivot") }}

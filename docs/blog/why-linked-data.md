---
title: Why Linked Data?
roadmap:roadmap:
  - title: Do large-scale long-term planning with RDF
    $id: long-term-planning
    is-blocked-by:
      - title: Humanity is facing a number of existential threats
        bug: true

  - title: Is humanity still alive by year 3000?
    $id: survive-iii-millenium
    branches:
      - title: ✅
        is-blocked-by:
          - title: Conserve resources
            is-blocked-by: long-term-planning
          - title: Take climate change under control
            is-blocked-by: long-term-planning
          - title: Produce energy sustainably
            is-blocked-by: long-term-planning
          - title: Be at peace
            is-blocked-by: long-term-planning
          - title: …
            is-blocked-by: long-term-planning

      - title: ❌
        is-blocked-by:
          - title: Build The Library in RDF

---

<div>
{{ render("survive-iii-millenium") }}
</div>

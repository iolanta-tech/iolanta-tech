---
title: Use … for autocomplete @ VS Code
roadmap:roadmap:
  - $id: ultimate-iolanta-ide
    title: Ultimate Iolanta IDE
    is-blocked-by:
      - title: Autocomplete
      - title: Go to definition
        is-blocked-by: json-ld-lsp
      - title: Find usages
        is-blocked-by: json-ld-lsp

  - title: JSON-LD LSP
    $id: json-ld-lsp
    is-blocked-by:
      - title: Before implementing LSP, use JSON Schema as an intermediate solution?
        branches:
          - title: yes
            is-blocked-by:
              - title: Request having RedHat YAML insatlled
                schema:url: https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml
              - title: Any luck with https://blogs.pjjk.net/phil/json-schema-for-json-ld/
              - title: Try out remark-lint-frontmatter-schema for Markdown frontmatter
                schema:url: https://github.com/JulianCataldo/remark-lint-frontmatter-schema#vs-code-optional
              - title: Automatically set up the IDE
                is-blocked-by:
                  - title: jeeves-generate
              - title: iolanta-json-schema
                is-blocked-by:
                  - title: Look at https://github.com/holodex/schema-jsonld-context
          - title: no
        is-blocked-by:
          - title: Try out JSON-LD LSP
            schema:url:
              - https://ajuvercr.github.io/jsonld-lsp/
              - https://github.com/ajuvercr/jsonld-lsp

---

## Context

YAML autocomplete in VS Code is a requirement for any kind of an adequate developer experience. SaaS Clickops tools provide that kind of experience via sleek UIs, the option we, by design, do not have. We have to provide adequate code editing experience instead.

<div>{{ render("ultimate-iolanta-ide") }}</div>

## Decision

…

## Consequences

…
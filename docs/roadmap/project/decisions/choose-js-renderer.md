---
$id: choose-js-renderer
table:columns:
  - table:self
  - supports-roadmap

table:rows:
  - rdfs:label: d3js
    schema:url: https://d3js.org/
    supports-roadmap: no

  - rdfs:label: flowchart.js
    schema:url: https://flowchart.js.org
    supports-roadmap: no

  - schema:url: https://gojs.net
    rdfs:label: GoJS
    supports-roadmap: yes

  - schema:url: https://github.com/bitterbit/flowjs
    rdfs:label: FlowJS
    supports-roadmap: yes

  - schema:url: https://jerosoler.github.io/Drawflow/
    rdfs:label: Drawflow
    supports-roadmap: yes
    visual-appearance: 10
    automatic-nodes-positioning: no

  - schema:url: https://www.rudabegga.com/diagramflowjs-master/flownewindex
    rdfs:label: DiagramFlowJS
    visual-appearance: 1

  - schema:url: https://github.com/WithoutHaste/Pinker
    rdfs:label: Pinker.js
    available: no

  - schema:url: https://visjs.github.io/vis-network/docs/network/
    rdfs:label: vis.js
    visual-appearance: 5
    automatic-nodes-positioning: yes
    html-in-nodes: yes

  - schema:url: https://www.sigmajs.org/
    rdfs:label: SigmaJS
    visual-appearance: 5
---

{{ render("choose-js-renderer") }}

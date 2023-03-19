---
title: "Iolanta: Linked Data authoring and ontology-based visualization system"
date: "2023-03-19"
hide:
  - navigation
---

Linked Data ⋅ JSON-LD ⋅ YAML-LD ⋅ Data Visualization

> TODO: abstract

## Introduction


Recent years have seen an increase of adoption for Linked Data technology [TODO see materials of conferences perhaps], but it is still far from the mainstream [TODO look into StackOverflow keyword statistics]. Wider, mainstream adoption among professionals, students, and general audience is the key [TODO] to unlock the full potential of this powerful technology stack for the benefit of humanity as a whole.

Arguably one of the reasons of World Wide Web success was its potential to virality [TODO]: HTML was an easy enough language for technically savvy users to start develop new websites at the era of early Web. How to establish a similar virality for Linked Data?

* Linked Data should be easy to author for technical users,
* They should see a reason, a motivation for getting into authoring their own pieces of Linked Data: that should solve their problems, relieve their pains.

[TODO why do we choose JSON-LD and YAML-LD as serialization formats? Compare editor support maybe]


It would seem obvious that, if professionals in other areas are to utilize Linked Data technology in their work they cannot be expected to dive deep into the depths of raw triples, which are not very suitable for human consumption. Users would need tools to *visualize* the raw triples, converting them into a form better suitable for human eye.

That need is met with Linked Data visualization tools — software systems which present Linked Data as

* lists,
* tables,
* charts,
* maps,
* trees,
* graphs,
* and a variety of subtypes of those [TODO: Visualization Methods Periodic Table].

Data visualization is a way to help the user create a mental model [TODO], converting data into understanding; for each particular situation and use case a unique visualization might be needed.

Linked Data Visualization book [TODO] provides a comprehensive review of state-of-the-art for Linked Data visualization tools as of 2020. The book lists 100500+ [TODO] software packages and compares them by a multitude of parameters. To present the results of analysis, the book uses tables [TODO], timelines [TODO], … and other visualization methods.

Curiously, none of the tools analyzed in the book was actually used to generate any of the data visualizations it posesses. At least that is what we have to assume: otherwise the authors would probably have mentioned the fact because it makes a point about usability and practical wortheness of Linked Data capable software.

What kind of a visualizaion system could the Linked Data Visualization book authors use to help generate tables and diagrams in their book?

## Visualization system: criteria

### Use case?

[TODO]

### Category

The instruments are categorized into a few groups:

1. browsers and exploratory tools [TODO],
2. tools using multiple visualization types [TODO] — essential, since for preparing papers, presentations and any kind of information analysis, it is essential to be able to use any visualization method that is appropriate to the case at hand;
3. graph-based visualization tools [TODO] is a special category because Linked Data is graph data by nature; but we cannot ,
4. domain and vocabulary specific, and device oriented tools [TODO],
5. ontology visualization tools [TODO] — can be probably excluded because an ontology is just one possible subject for data visualization, and probably not its focus in most use cases.


### Self-hostedness

In software compilers industry, a self-hosted compiler is a compiler which is capable of compiling itself from source code [TODO]. Can a visualization of Linked Data be self-hosted — in other words, can it be described *as Linked Data*?

Applying the 5-star model of Linked Data [TODO: https://www.w3.org/2011/gld/wiki/5\_Star\_Linked\_Data] to visualizations themselves seems to promise a few valuable benefits:

* *Visualization is available on the Web* which enables anyone to retrieve and enjoy applying to to the data,
* *Visualization is available as machine-readable structured data* and can be not only reused but easily customized,
* *Available in a non-proprietary format,* say as a JSON-LD (or any other RDF serialization) document,
* *Published using open standards from the W3C*, which JSON-LD is,
* *All of the above and links to other Linked Open Data* — which it does because a visualization must reference certain aspects of source data to specify how to visualize that.

Self-hosted Linked Data visualizations should be extremely easy to share and to use for professionals in other areas of human activity, from aerospace engineering to fine arts.

[TODO: target this better to the book writing use case]

### Plugin support

The range of available visualizations is infinite, and it would be impossible to accommodate any possible use case in one software package. Users might want to create their own visualizations for their very specific needs. These thoughts call for a plugin approach [TODO], where a visualization toolkit can be extended using predefined hooks via third-party plugins.


### Embeddability

There are different information tools people utilize to prepare books, papers, presentations:

* Static site builders,
* LaTeX,
* Presentations,
* Word processors,
* Spreadsheets,
* …

The ideal Linked Data visualization system should easily and seamlessly integrate with popular information management and publishing tools.


### Open Source

…

### Plain files

[TODO]

## Iolanta: tutorial

To solve the issues outlined above, we propose an open source visualization tool by the name of `iolanta`, build in Python programming language. In order to reduce development time and sooner arrive at a minimum viable prototype [TODO] this version of the tool is restricted to two usage scenarios:

* Python-specific application user interface (API),
* Command line interface (CLI).

For installation, `iolanta` requires a working Python 3.10 environment. The installation is handled via `pip`:

```
$ pip install iolanta iolanta-record iolanta-tables
```

Here, we install not only `iolanta` itself but two of its plugins as well.

```
$ iolanta render schema:Person
```



### Visualize a table with something

### Generate a LaTeX table

### Visualize stuff in MkDocs

### Retrieve information from GitHub

### Retrieve information from program text


### Vocabulary for self-hosted visualizations

Description of visualizations requires some meta-vocabulary which should be useful regardless of data type and of visualization type to use. Such a vocabulary should aid the Semantic Web browser orchestrating the visualizations and choosing which visualization type to utilize at any given situation.

#### Fresnel vocabulary

Fresnel Vocabulary [https://www.w3.org/2005/04/fresnel-info/] is a browser-independent vocabulary to specify how to render an RDF model. Fresnel's two foundational concepts are as follows:

* *lenses* define which properties of an RDF resource to display and how to order them,
* *formats* define how to render those properties using
    * RDF-specific formatting attributes
    * and hooks to CSS [http://www.w3.org/Style/CSS/].


The visualization process Fresnel uses is described in see [TODO Figure: Fresnel vocab]).

![fresnel.png](fresnel.png)

> Stages of RDF Fresnel rendering process.

While Fresnel aims to be platform independent, it still has a binding to CSS, thus making HTML and SVG kind of preferred formats.

Fresnel vocabulary is used by a number of tools:


* IsaViz [https://www.w3.org/2001/11/IsaViz/],
* Longwell / Piggy Bank (SIMILE/W3C/MIT) [http://simile.mit.edu/longwell/] and [http://simile.mit.edu/piggy-bank/],
* Horus [http://www.wiwiss.fu-berlin.de/suhl/bizer/rdfapi/tutorial/horus/index.htm],
* LENA browser [http://isweb.uni-koblenz.de/Research/lena],
* OAT: OpenLink AJAX Toolkit (OpenLink Software) [http://sourceforge.net/projects/oat],
* Marbles [http://mes.github.io/marbles].


## `iolanta` vocabulary

`iolanta` operation is based on a simple vocabulary which is bundled with the application. Iolanta vocabulary defines a few classes and a few properties connecting them to each other.

Prefix we use is `iolanta:`, and it resolves to https://iolanta.tech/.

[TODO: visualize Iolanta ontology as a graph]

### Class: `iolanta:Environment`

Data visualization might be performed in various contexts, which we call Environments. Iolanta defines a few instances of this class:


* `iolanta:html` calls for HTML output;
* `iolanta:cli` is for rendering in the command line;
* `iolanta:tex` is for \LaTeX documents (such as this paper itself).


`iolanta` plugins might define more environments, for that it is enough to define them as `rdf:type iolanta:Environment`.

### Class: `Facet`

[TODO! what is a facet, anyway?]

[TODO! what faceted visualization tools already exist?]

Facet is a unit of executable program code used to visualize RDF nodes in an environment. Generally speaking, facet can be described as a black box which has three inputs:


* Identifier of an RDF `node` to visualize (an IRI, a Blank Node, or a Literal);
* Identifier of an `environment` (IRI or Blank Node) which the node must be visualized within;
* `iolanta` instance, which contains the current graph queryable via SPARQL [TODO: cite].


Facet can run arbitrary SPARQL queries against `iolanta` graph to retrieve any information about the `node` it might require. The simplest of all is `iolanta.facets.Link` facet targeted at `iolanta:html` environment.

Current version of `iolanta` supports only one kind of Facets: Python classes which are subclasses of `iolanta.Facet` abstract base class.

[TODO: visualize Facet class in class diagram format or WTF]

### Property: `iolanta:supports`

* [Domain] `iolanta:Facet`
* [Range] `iolanta:Environment`
* [Inverse] `iolanta:isSupportedBy`

Not every facet suits every possible environment. For instance, if a facet returns a string that contains HTML code that result would be next to useless for a \LaTeX document, and vice versa. Thus, it is necessary to describe for every facet which environment(s) it is suitable for. We use `iolanta:supports` for that.

### Property: `iolanta:facet`

* [Range] `iolanta:Facet`

This property might be attached to any IRI or BNode in an RDF graph. If we decidedly know which facet to use for a particular node we can explicitly connect the node and the facet in our RDF graph. For example:

```
    :something iolanta:facet <python://iolanta.facets.Link> .
```

From this example, it is evident how we identify facets. These are import paths native for Python programming language, which we define by `python://` protocol.

[TODO: This example should be closer to real life]

[TODO: Visualize this as a graph!]

### Property: `iolanta:hasInstanceFacet`

*[Domain] `rdfs:Class`
*[Range] `iolanta:Facet`
*[Inverse] `iolanta:isInstanceFacetOf`

It would be tedious to attach `iolanta:facet` to *each and every* node this facet might be able to render; oftentimes, it is sufficient to attach a facet to a whole class of nodes. That's what `iolanta:hasInstanceFacet` is for: `iolanta` will find the facet by classes the node is attached to.

### Property: `iolanta:hasDefaultFacet`

* [Domain] `iolanta:Environment`
* [Range] `iolanta:Facet`
* [Inverse] `iolanta:isDefaultFacetOf`

If neither `iolanta:facet` nor `iolanta:hasInstanceFacet` provide a suitable `iolanta:Facet` then we look into the `iolanta:Environment` the rendering is targeted at. The environment can define a default facet used for that environment.

## Facet search algorithm

[TODO: draw this algorithm as a flow chart]

`Iolanta.render()` method accepts arguments:

* [node] is an RDF node to render;
* [environments] is a **list** of `iolanta:Environment` instance references.

Given that information, we need to find a facet in our graph and execute that facet to construct a visualization for our node in one of these environments.


* Look for `iolanta:facet` link such that `\$node iolanta:facet ?facet . ?facet iolanta:supports ?environment` .


## Iolanta browser

Iolanta browser is an open source tool built in Python programming language in attempt to illustrate the principles of this article and pave a way to a powerful, versatile Linked Data visualization system.

TODO a diagram of how the browser works

### Facet API

#### query

#### show

#### render

### Iolanta API

## Iolanta plugins

### iolanta-tables

### iolanta-jinja2

## Future directions


* Implement more plugins for various use cases, such as:
    * drawing roadmaps and network planning,
    * drawing C4 [TODO] architecture diagrams,
    * and more;
* Provide interactive browsing experience;
* Implement more facet types, such as:
    * Web components,
    * JSON-RPC [TODO] controlled plugins;
* Improve the experience of browsing remote networks;
* …

import funcy
from dominate.tags import table, tr, td, code, div, body
from dominate.util import raw
from iolanta.facets.html.base import HTMLFacet
from iolanta.namespaces import LOCAL, IOLANTA


class SideBySide(HTMLFacet):
    """YAML code and its rendering."""

    def show(self):
        """Render Side by Side for HTML."""
        rows = self.query(
            'SELECT * WHERE { GRAPH ?page { $iri ?p ?o } }',
            iri=self.iri,
        )

        page = funcy.first(rows)['page']

        renderable = self.render(self.iri, environments=[IOLANTA.html])
        return div(
            self.render(
                page,
                environments=[LOCAL.term('code')],
            ),
            div(raw(renderable)) if isinstance(renderable, str) else renderable,
            data_facet='side-by-side',
            cls='grid',
            markdown='markdown',
        )

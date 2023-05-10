import funcy
from dominate.tags import table, tr, td, code
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

        return table(
            tr(
                td(
                    self.render(
                        page,
                        environments=[LOCAL.term('code')],
                    ),
                ),
                td(
                    '⇒',
                    style='font-size: 200%; vertical-align: middle',
                ),
                td(
                    code(
                        '{{ render(\'%s\') }}' % str(self.iri).replace(
                            'local:',
                            '',
                        ),
                    ),
                    self.render(self.iri, environments=[IOLANTA.html]),
                ),
            ),
            data_facet='side-by-side',
        )

from pathlib import Path

import funcy
from dominate.tags import code, table, td, tr
from dominate.util import raw
from iolanta.facets.html.base import HTMLFacet
from iolanta.namespaces import LOCAL, IOLANTA

CODE_TEMPLATE = """
```{language} title="{title}"
{code}
```

{annotations}
"""


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


class Code(HTMLFacet):
    """Print contents of a file in a code fence."""

    def show(self):
        """Render code as HTML."""
        path = Path(str(self.iri).replace('file://', ''))
        return raw(
            CODE_TEMPLATE.format(
                language='yaml',
                code=path.read_text(),
                title=path.name,
                annotations='',
            ),
        )

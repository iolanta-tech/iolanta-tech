from pathlib import Path

from dominate.util import raw
from iolanta.facets.html.base import HTMLFacet

CODE_TEMPLATE = """
```{language} title="{title}"
{code}
```

{annotations}
"""


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

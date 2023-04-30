import funcy
from iolanta.facets.html.base import HTMLFacet
from iolanta.namespaces import IOLANTA, LOCAL
from iolanta_tables.models import TABLE

TEMPLATE = '''
!!! {type} "Criterion {number}"
    {content}
'''


class Criterion(HTMLFacet):
    def show(self) -> str:
        number, = funcy.pluck(
            'number',
            self.query(
                'SELECT * WHERE { $criterion local:number ?number }',
                criterion=self.iri,
            ),
        )

        admonition_type = {
            IOLANTA.html: 'question',
            LOCAL.satisfied: 'success',
            LOCAL.failed: 'failure',
        }[self.environment]

        return TEMPLATE.format(
            content=self.render(
                node=self.iri,
                environments=[TABLE.td],  # To avoid recursion with iolanta:html
            ),
            number=number,
            type=admonition_type,
        )

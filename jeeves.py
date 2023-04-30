import rich
from sh import grep, mkdocs


def todo():
    """Print TODOs."""
    rows: str = grep(
        '-oP',
        r'\{# todo: (\K[^#]+) #\}',
        'docs/blog/whitepaper/index.md',
    )

    todos = [
        row.replace(' #}', '')
        for row in rows.split('\n')
    ]

    for todo_item in todos:
        if todo_item:
            rich.print(f'▢ {todo_item}')


def serve():
    """
    Serve the iolanta.tech site.

    The site will be available at http://localhost:9841
    """
    mkdocs.serve(
        '-a', 'localhost:6451',
        _fg=True,
    )

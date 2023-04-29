import rich
from sh import grep


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

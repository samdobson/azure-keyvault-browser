from rich.console import Console, ConsoleOptions, RenderResult
from rich.table import Table
from textual.keys import Keys

from .. import styles

UP = "\u2191"
DOWN = "\u2193"
LEFT = "\u2190"
RIGHT = "\u2192"


class HelpRenderable:
    """A help renderable"""

    shortcuts = {
        "global": {
            "back": Keys.Escape,
            "help": "?",
            "quit": Keys.ControlC,
        },
        "navigation": {
            "next row": f"{DOWN}",
            "previous row": f"{UP}",
            "next page": f"{RIGHT}",
            "previous page": f"{LEFT}",
            "first page": "f",
            "last page": "l",
            "select": Keys.Enter,
        },
        "secret properties": {
            "unlock": Keys.ControlS,
            "view": Keys.ControlK,
        },
    }

    def __str__(self) -> str:
        return str(self.shortcuts)

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:

        table = Table(
            box=None, expand=True, show_footer=False, show_header=False, width=40
        )

        table.add_column(style=styles.GREY)
        table.add_column(style=f"{styles.ORANGE} bold")
        for category, shortcuts in self.shortcuts.items():
            table.add_row(f"[{styles.GREEN}]{category}[/]")
            for action, shortcut in shortcuts.items():
                table.add_row(action, shortcut)
            else:
                table.add_row()

        yield table

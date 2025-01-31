import pyfiglet
from rich.console import Console
from rich.panel import Panel

console = Console()


def welcome():
    """Affiche une belle bannière pour Centre Échecs App"""
    ascii_banner = pyfiglet.figlet_format(
        "WELCOME")  # Génère le texte en ASCII
    console.print(Panel.fit(
        ascii_banner, title="[bold cyan]♟️ Centre Échecs App ♟️[/bold cyan]", border_style="blue"))




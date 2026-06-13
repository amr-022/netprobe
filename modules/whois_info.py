import whois
from rich.console import Console

console = Console()

def whois_lookup(target):
    console.print("\n[bold yellow][ WHOIS Lookup ][/bold yellow]")
    try:
        w = whois.whois(target)
        console.print(f"  [green]✅ Registrar:[/green] {w.registrar}")
        console.print(f"  [green]✅ Creation Date:[/green] {w.creation_date}")
        console.print(f"  [green]✅ Country:[/green] {w.country}")
    except Exception as e:
        console.print(f"  [red]❌ WHOIS Failed: {e}[/red]")

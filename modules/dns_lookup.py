import socket
from rich.console import Console

console = Console()

def dns_lookup(target):
    console.print("\n[bold yellow][ DNS Lookup ][/bold yellow]")
    try:
        ip = socket.gethostbyname(target)
        console.print(f"  [green]✅ IP Address:[/green] {ip}")
        return ip
    except socket.gaierror:
        console.print("  [red]❌ DNS Lookup Failed[/red]")
        return None

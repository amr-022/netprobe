import socket
from rich.console import Console

console = Console()

SUBDOMAINS = [
    "www", "mail", "ftp", "api", "dev",
    "staging", "admin", "blog", "shop",
    "remote", "vpn", "portal", "cdn", "app"
]

def find_subdomains(domain):
    console.print("\n[bold yellow][ Subdomain Finder ][/bold yellow]")
    found = []
    for sub in SUBDOMAINS:
        target = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(target)
            console.print(f"  [green]✅ {target} → {ip}[/green]")
            found.append(target)
        except socket.gaierror:
            pass
    if not found:
        console.print("  [red]❌ No subdomains found[/red]")
    return found

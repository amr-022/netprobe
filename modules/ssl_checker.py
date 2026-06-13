import ssl
import socket
from datetime import datetime
from rich.console import Console

console = Console()

def check_ssl(domain):
    console.print("\n[bold yellow][ SSL Certificate ][/bold yellow]")
    try:
        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=domain
        )
        conn.settimeout(3)
        conn.connect((domain, 443))
        cert = conn.getpeercert()
        conn.close()

        issued_to = cert["subject"][0][0][1]
        issued_by = cert["issuer"][1][0][1]
        expire_date = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
        days_left = (expire_date - datetime.utcnow()).days

        console.print(f"  [green]✅ Issued To:  {issued_to}[/green]")
        console.print(f"  [green]✅ Issued By:  {issued_by}[/green]")
        console.print(f"  [green]✅ Expires:    {expire_date.strftime('%Y-%m-%d')}[/green]")

        if days_left > 30:
            console.print(f"  [green]✅ Days Left:  {days_left} days[/green]")
        elif days_left > 0:
            console.print(f"  [yellow]⚠️  Days Left:  {days_left} days - Expiring Soon![/yellow]")
        else:
            console.print(f"  [red]❌ Certificate EXPIRED![/red]")

        return days_left

    except Exception as e:
        console.print(f"  [red]❌ SSL Check Failed: {e}[/red]")
        return 0

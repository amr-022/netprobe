import requests
from rich.console import Console

console = Console()

SECURITY_HEADERS = {
    "Strict-Transport-Security": ("HSTS", "HIGH RISK", "Forces HTTPS - missing means downgrade attacks possible!"),
    "X-Frame-Options": ("Clickjacking Protection", "MEDIUM RISK", "Missing means site vulnerable to clickjacking!"),
    "X-Content-Type-Options": ("MIME Sniffing Protection", "MEDIUM RISK", "Missing means MIME type attacks possible!"),
    "Content-Security-Policy": ("CSP", "HIGH RISK", "Missing means XSS attacks are easier!"),
    "X-XSS-Protection": ("XSS Protection", "MEDIUM RISK", "Missing means less browser XSS protection!"),
    "Referrer-Policy": ("Referrer Policy", "LOW RISK", "Missing means sensitive URLs may leak!")
}

def check_http_headers(target):
    console.print("\n[bold yellow][ HTTP Security Headers ][/bold yellow]")
    vulnerabilities = []
    safe_headers = []

    try:
        response = requests.get(f"http://{target}", timeout=5)
        headers = response.headers

        for header, (name, risk, reason) in SECURITY_HEADERS.items():
            if header in headers:
                console.print(f"  [green]✅ {name}: Present[/green]")
                safe_headers.append(name)
            else:
                if risk == "HIGH RISK":
                    color = "red"
                elif risk == "MEDIUM RISK":
                    color = "yellow"
                else:
                    color = "cyan"

                console.print(f"  [{color}]❌ {name}: MISSING - {risk}[/{color}]")
                console.print(f"  [{color}]   ⚠ {reason}[/{color}]")
                vulnerabilities.append((name, risk))

    except Exception as e:
        console.print(f"  [red]❌ HTTP Headers Check Failed: {e}[/red]")

    return vulnerabilities, safe_headers

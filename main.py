import sys
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from modules.dns_lookup import dns_lookup
from modules.whois_info import whois_lookup
from modules.port_scanner import port_scan
from modules.ip_reputation import check_reputation
from modules.geoip import geoip_lookup
from modules.subdomain_finder import find_subdomains
from modules.ssl_checker import check_ssl
from modules.banner_grabber import grab_banners
from modules.http_headers import check_http_headers

load_dotenv()
console = Console()

def show_summary(target, ip, open_ports, score, city, isp, subdomains, ssl_days, banner_results, vulnerabilities, safe_headers):
    table = Table(title="📋 NetProbe Summary", style="bold cyan")
    table.add_column("Field", style="yellow")
    table.add_column("Result", style="green")

    table.add_row("Target", target)
    table.add_row("IP Address", ip if ip else "Not Found")
    table.add_row("City", city)
    table.add_row("ISP", isp)
    table.add_row("Open Ports", ", ".join(str(p) for p in open_ports) if open_ports else "None")
    table.add_row("Subdomains Found", str(len(subdomains)))
    table.add_row("SSL Days Left", f"{ssl_days} days")
    table.add_row("Abuse Score", f"{score}%")

    high_risk = [f"{p}/{s}" for p, s, r in banner_results if r == "HIGH RISK"]
    medium_risk = [f"{p}/{s}" for p, s, r in banner_results if r == "MEDIUM RISK"]
    safe = [f"{p}/{s}" for p, s, r in banner_results if r == "SAFE"]

    table.add_row("🔴 High Risk Ports", ", ".join(high_risk) if high_risk else "None")
    table.add_row("🟡 Medium Risk Ports", ", ".join(medium_risk) if medium_risk else "None")
    table.add_row("🟢 Safe Ports", ", ".join(safe) if safe else "None")

    high_vulns = [n for n, r in vulnerabilities if r == "HIGH RISK"]
    medium_vulns = [n for n, r in vulnerabilities if r == "MEDIUM RISK"]

    table.add_row("🔴 Critical Vulnerabilities", ", ".join(high_vulns) if high_vulns else "None")
    table.add_row("🟡 Medium Vulnerabilities", ", ".join(medium_vulns) if medium_vulns else "None")
    table.add_row("🟢 Secure Headers", ", ".join(safe_headers) if safe_headers else "None")

    console.print("\n")
    console.print(table)

def main():
    if len(sys.argv) < 2:
        console.print("[red]Usage: python3 main.py <target>[/red]")
        sys.exit(1)

    target = sys.argv[1]

    console.print(Panel(f"🛡️  NetProbe - Target: [cyan]{target}[/cyan]",
                        style="bold green"))

    ip = dns_lookup(target)

    city, isp = "Unknown", "Unknown"
    if ip:
        city, isp = geoip_lookup(ip)

    whois_lookup(target)
    subdomains = find_subdomains(target)
    ssl_days = check_ssl(target)
    vulnerabilities, safe_headers = check_http_headers(target)

    open_ports = []
    score = 0
    banner_results = []

    if ip:
        open_ports = port_scan(ip)
        score = check_reputation(ip)
        banner_results = grab_banners(ip)

    show_summary(target, ip, open_ports, score, city, isp, subdomains, ssl_days, banner_results, vulnerabilities, safe_headers)

if __name__ == "__main__":
    main()

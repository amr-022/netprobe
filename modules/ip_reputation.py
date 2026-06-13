import requests
import os
from rich.console import Console
from dotenv import load_dotenv

load_dotenv()
console = Console()

def check_reputation(ip):
    API_KEY = os.getenv("ABUSEIPDB_KEY")
    console.print("\n[bold yellow][ IP Reputation ][/bold yellow]")
    try:
        response = requests.get(
            "https://api.abuseipdb.com/api/v2/check",
            headers={"Key": API_KEY, "Accept": "application/json"},
            params={"ipAddress": ip, "maxAgeInDays": 90}
        )
        data = response.json()["data"]
        score = data["abuseConfidenceScore"]
        reports = data["totalReports"]
        country = data["countryCode"]

        if score == 0:
            console.print(f"  [green]✅ Abuse Score: {score}% - Clean[/green]")
        elif score < 50:
            console.print(f"  [yellow]⚠️  Abuse Score: {score}% - Suspicious[/yellow]")
        else:
            console.print(f"  [red]❌ Abuse Score: {score}% - Dangerous![/red]")

        console.print(f"  [cyan]📊 Total Reports: {reports}[/cyan]")
        console.print(f"  [cyan]🌍 Country: {country}[/cyan]")
        return score

    except Exception as e:
        console.print(f"  [red]❌ Reputation Check Failed: {e}[/red]")
        return 0

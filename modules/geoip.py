import requests
from rich.console import Console

console = Console()

def geoip_lookup(ip):
    console.print("\n[bold yellow][ GeoIP Location ][/bold yellow]")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data["status"] == "success":
            console.print(f"  [green]🌍 Country:  {data['country']}[/green]")
            console.print(f"  [green]🏙️  City:     {data['city']}[/green]")
            console.print(f"  [green]📡 ISP:      {data['isp']}[/green]")
            console.print(f"  [green]📍 Lat/Lon:  {data['lat']}, {data['lon']}[/green]")
            return data['city'], data['isp']
        else:
            console.print("  [red]❌ GeoIP lookup failed[/red]")
            return "Unknown", "Unknown"

    except Exception as e:
        console.print(f"  [red]❌ Error: {e}[/red]")
        return "Unknown", "Unknown"

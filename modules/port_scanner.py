import socket
from rich.console import Console

console = Console()

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

def port_scan(ip):
    console.print("\n[bold yellow][ Port Scanner ][/bold yellow]")
    open_ports = []
    for port, service in COMMON_PORTS.items():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                console.print(f"  [green]✅ {port}/{service} - OPEN[/green]")
                open_ports.append(port)
            s.close()
        except:
            pass
    if not open_ports:
        console.print("  [red]❌ No open ports found[/red]")
    return open_ports

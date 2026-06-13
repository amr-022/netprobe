import socket
from rich.console import Console

console = Console()

PORT_RISK = {
    21:   ("FTP",      "HIGH RISK",   "red",    "Unencrypted file transfer - easily exploited!"),
    22:   ("SSH",      "MEDIUM RISK", "yellow", "Secure but can be brute-forced if exposed."),
    23:   ("Telnet",   "HIGH RISK",   "red",    "Completely unencrypted - very dangerous!"),
    25:   ("SMTP",     "MEDIUM RISK", "yellow", "Can be abused for spam if misconfigured."),
    80:   ("HTTP",     "MEDIUM RISK", "yellow", "Unencrypted web traffic - prefer HTTPS."),
    443:  ("HTTPS",    "SAFE",        "green",  "Encrypted web traffic - good."),
    3306: ("MySQL",    "HIGH RISK",   "red",    "Database port should never be public!"),
    8080: ("HTTP-Alt", "MEDIUM RISK", "yellow", "Alternative HTTP - check if intentional.")
}

def assess_port(port):
    if port in PORT_RISK:
        return PORT_RISK[port]
    elif port < 1024:
        return ("Unknown", "MEDIUM RISK", "yellow", "Well-known port range - investigate why it's open.")
    elif port < 49152:
        return ("Unknown", "HIGH RISK", "red", "Registered port open unexpectedly - could be suspicious!")
    else:
        return ("Unknown", "HIGH RISK", "red", "Dynamic/private port open - very suspicious!")

def grab_banners(ip):
    console.print("\n[bold yellow][ Banner Grabbing & Risk Assessment ][/bold yellow]")
    found = False
    results = []

    ports_to_scan = list(PORT_RISK.keys()) + [8443, 3389, 5900, 6379, 27017]

    for port in ports_to_scan:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((ip, port))
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024).decode(errors="ignore").strip()
            s.close()

            service, risk, color, reason = assess_port(port)
            first_line = banner.split("\n")[0] if banner else "No banner"

            console.print(f"  [{color}]Port {port}/{service} - {risk}[/{color}]")
            console.print(f"  [{color}]  ⚠ {reason}[/{color}]")
            if first_line and first_line != "No banner":
                console.print(f"  [cyan]  Banner: {first_line}[/cyan]")

            results.append((port, service, risk))
            found = True

        except:
            pass

    if not found:
        console.print("  [red]❌ No open ports found[/red]")

    return results

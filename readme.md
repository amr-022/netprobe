# 🛡️ NetProbe - Network & Security Analyzer

A Python CLI tool that performs full network reconnaissance and security analysis on any domain or IP.

## 🔍 Features
- DNS Lookup → resolves domain to IP
- GeoIP Location → finds city, country & ISP
- WHOIS Info → domain ownership & registration
- Subdomain Finder → discovers hidden subdomains
- Port Scanner → detects open ports with risk assessment
- SSL Certificate → checks validity & expiry
- Banner Grabbing → identifies services & versions
- HTTP Security Headers → detects missing security headers & vulnerabilities
- IP Reputation → checks against AbuseIPDB threat database
- Summary Table → full report at the end

## ⚙️ Installation

git clone https://github.com/amr-022/netprobe.git
cd netprobe
python3 -m venv venv
source venv/bin/activate
pip install rich requests python-whois python-dotenv

## 🔑 API Key Setup

1. Register free at https://www.abuseipdb.com/register
2. Get your API key from https://www.abuseipdb.com/account/api
3. Create a .env file:

ABUSEIPDB_KEY=YOUR_API_KEY_HERE

## 🚀 Usage

python3 main.py google.com
python3 main.py github.com
python3 main.py scanme.nmap.org

## 💻 Tech Stack
- Python 3
- Rich (CLI formatting)
- Sockets
- AbuseIPDB API
- ip-api.com

## ⚠️ Disclaimer
This tool is for educational purposes only.
Use only on targets you have explicit permission to scan.

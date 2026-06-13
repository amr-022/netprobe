# 🛡️ NetProbe - Network & Security Analyzer

A Python CLI tool that performs network reconnaissance and security analysis on any domain or IP.

## Features
- 🔍 DNS Lookup
- 📋 WHOIS Information
- 🔓 Port Scanner
- ⚠️  IP Reputation Check (AbuseIPDB)

## Installation
git clone https://github.com/YOUR_USERNAME/netprobe.git
cd netprobe
python3 -m venv venv
source venv/bin/activate
pip install rich requests python-whois

## Usage
python3 main.py google.com
python3 main.py scanme.nmap.org

## Tech Stack
- Python 3
- Rich (CLI formatting)
- AbuseIPDB API
- Socket / WHOIS

## ⚠️ Disclaimer
This tool is for educational purposes only.
Use only on targets you have permission to scan.

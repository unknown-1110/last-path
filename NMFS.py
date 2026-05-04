import os
import socket
import requests
import subprocess
import platform
import hashlib
import time
import random
import re
import ssl
import string
import threading
import concurrent.futures
import ipaddress
import json
from datetime import datetime
from urllib.parse import urlparse, urljoin
from html.parser import HTMLParser


NMFS_ASCII = r"""
 ███╗   ██╗███╗   ███╗███████╗███████╗
 ████╗  ██║████╗ ████║██╔════╝██╔════╝
 ██╔██╗ ██║██╔████╔██║█████╗  ███████╗
 ██║╚██╗██║██║╚██╔╝██║██╔══╝  ╚════██║
 ██║ ╚████║██║ ╚═╝ ██║██║     ███████║
 ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝     ╚══════╝
"""

def show_banner():
    print(NMFS_ASCII)
    print("        NO MERCY FOR SOCIETY - PENTEST TOOL v6.0")
    print("        github: https://github.com/unknown-1110")
    print("        \"This tool is for educational & pentesting only.\"")
    print("  " + "="*55)


def show_menu():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    show_banner()
    print("""
  +-------------------+-------------------+-------------------+
  |  [1]  Port Scanner | [2]  Subdomain    | [3]  Ping Sweeper |
  |                   |       Finder       |                   |
  +-------------------+-------------------+-------------------+
  |  [4]  DNS Lookup  | [5]  Dir Brute    | [6]  Network Info |
  +-------------------+-------------------+-------------------+
  |  [7]  Evil Corp   | [8]  Hash Cracker | [9]  GeoIP Tracker|
  |       Detector    |  (MD5/SHA1/SHA256) |                   |
  +-------------------+-------------------+-------------------+
  | [10]  Email Valid | [11]  Pass Gen    | [12]  Link Extract|
  +-------------------+-------------------+-------------------+
  | [13]  WHOIS Lookup| [14]  SSL Checker | [15]  Robots/Smap |
  +-------------------+-------------------+-------------------+
  | [16]  HTTP Header | [17]  Banner Grab | [18]  HTTP Timer  |
  |       Analyzer    |                   |                   |
  +-------------------+-------------------+-------------------+
  | [19]  Open Redir  | [20]  Reverse IP  | [21]  URL Fuzzer  |
  |       Checker     |       Lookup      |                   |
  +-------------------+-------------------+-------------------+
  | [22]  Tech Stack  | [23]  Cookie      | [24]  CORS Checker|
  |       Detector    |       Analyzer    |                   |
  +-------------------+-------------------+-------------------+
  | [25]  CIDR Calc   | [26]  JWT Decoder | [27]  HTTP Method |
  |                   |      [NEW]        |  Tester  [NEW]    |
  +-------------------+-------------------+-------------------+
  | [28]  Encode/     | [29]  Username    | [30]  Email       |
  |  Decode Tool      |  Lookup [OSINT]   |  Breach Check     |
  |                   |                   |  [OSINT]          |
  +-------------------+-------------------+-------------------+
  | [31]  Metadata    |                   |                   |
  |  Extractor[OSINT] |    [99]  EXIT     |                   |
  +-------------------+-------------------+-------------------+
    """)
    print("  [NMFS@kali:~]$", end=" ")


def port_scanner():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           PORT SCANNER - NMFS mode")
    print("="*55)

    target = input("\n[NMFS] Masukkan IP/Domain: ").strip()
    port_input = input("[NMFS] Port range atau list (contoh: 1-1000 atau 22,80,443): ").strip()

    ports_list = []
    if '-' in port_input and ',' not in port_input:
        parts = port_input.split('-')
        try:
            ports_list = list(range(int(parts[0]), int(parts[1]) + 1))
        except:
            print("  [!] Format range tidak valid")
            input("\n[!] Tekan Enter untuk kembali...")
            return
    else:
        try:
            ports_list = [int(p.strip()) for p in port_input.split(',')]
        except:
            print("  [!] Format port tidak valid")
            input("\n[!] Tekan Enter untuk kembali...")
            return

    services = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB",
        3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 6379: "Redis",
        8080: "HTTP-Alt", 8443: "HTTPS-Alt", 27017: "MongoDB"
    }

    print(f"\n[*] Scanning {target} ({len(ports_list)} ports)...\n")
    open_ports = []
    lock = threading.Lock()

    def scan_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.8)
            result = sock.connect_ex((target, port))
            sock.close()
            if result == 0:
                service = services.get(port, "Unknown")
                with lock:
                    open_ports.append(port)
                    print(f"  [OPEN]  Port {port:<6} -> {service}")
        except:
            pass

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_port, ports_list)

    print(f"\n  [*] Scan complete. {len(open_ports)} port terbuka dari {len(ports_list)} port.")
    input("\n[!] Tekan Enter untuk kembali...")


def subdomain_finder():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           SUBDOMAIN FINDER - NMFS mode")
    print("="*55)

    domain = input("\n[NMFS] Masukkan domain (contoh: google.com): ")

    subdomains = [
        'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
        'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'blog', 'shop', 'api',
        'dev', 'test', 'staging', 'admin', 'portal', 'support', 'forum', 'news',
        'vpn', 'secure', 'remote', 'backup', 'sql', 'db', 'mysql', 'internal',
        'cdn', 'static', 'assets', 'media', 'images', 'upload', 'downloads',
        'beta', 'alpha', 'old', 'new', 'demo', 'app', 'mobile', 'wap',
        'cloud', 'server', 'host', 'mx', 'mx1', 'mx2', 'relay', 'gateway'
    ]

    print(f"\n[*] Mencari subdomain untuk {domain}...\n")

    found = []
    for sub in subdomains:
        url = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(url)
            found.append(url)
            print(f"  [FOUND]  {url:<40} -> {ip}")
        except:
            pass

    print(f"\n  [*] Total ditemukan: {len(found)} subdomain")
    input("\n[!] Tekan Enter untuk kembali...")


def ping_sweeper():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           PING SWEEPER - NMFS mode")
    print("="*55)

    network = input("\n[NMFS] Masukkan network (contoh: 192.168.1): ")
    start = int(input("[NMFS] Mulai dari (1-254): "))
    end = int(input("[NMFS] Sampai (1-254): "))

    print(f"\n[*] Scanning {network}.{start}-{end}...\n")

    param = '-n' if platform.system() == 'Windows' else '-c'
    alive = []

    for i in range(start, end + 1):
        ip = f"{network}.{i}"
        response = subprocess.run(
            ['ping', param, '1', '-W', '1', ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if response.returncode == 0:
            alive.append(ip)
            print(f"  [UP]  {ip}")

    print(f"\n  [*] {len(alive)} host aktif ditemukan.")
    input("\n[!] Tekan Enter untuk kembali...")


def dns_lookup():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           DNS LOOKUP - NMFS mode")
    print("="*55)

    target = input("\n[NMFS] Masukkan domain/IP: ")

    try:
        print(f"\n[*] Resolving {target}...\n")

        ip = socket.gethostbyname(target)
        print(f"  IP Address    : {ip}")

        try:
            hostname = socket.gethostbyaddr(ip)
            print(f"  Hostname      : {hostname[0]}")
            if hostname[1]:
                print(f"  Aliases       : {', '.join(hostname[1])}")
        except:
            pass

        try:
            all_ips = socket.getaddrinfo(target, None)
            unique_ips = list(set([r[4][0] for r in all_ips]))
            if len(unique_ips) > 1:
                print(f"  All Records   : {', '.join(unique_ips)}")
        except:
            pass

    except socket.gaierror:
        print("  [!] Domain tidak valid atau tidak bisa di-resolve!")

    input("\n[!] Tekan Enter untuk kembali...")


def dir_brute():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           DIRECTORY BRUTE - NMFS mode")
    print("="*55)

    url = input("\n[NMFS] Masukkan URL (contoh: http://example.com): ")

    dirs = [
        'admin', 'administrator', 'backup', 'config', 'css', 'img', 'js', 'login',
        'wp-admin', 'wp-login.php', 'robots.txt', 'sitemap.xml', 'uploads', 'user',
        'api', 'v1', 'v2', 'secret', 'hidden', 'private', '.git', '.env',
        'database', 'sql', 'phpmyadmin', 'cpanel', 'panel', 'dashboard',
        'console', 'manager', 'management', 'server-status', 'info.php',
        'phpinfo.php', 'test.php', 'shell.php', 'readme.txt', 'CHANGELOG.txt',
        'license.txt', 'wp-config.php.bak', 'config.php.bak', 'db.sql'
    ]

    print(f"\n[*] Brute forcing {url}...\n")

    found_count = 0
    for d in dirs:
        test_url = f"{url.rstrip('/')}/{d}"
        try:
            response = requests.get(test_url, timeout=4, allow_redirects=False)
            if response.status_code == 200:
                found_count += 1
                print(f"  [200]  {test_url}")
            elif response.status_code == 403:
                print(f"  [403]  {test_url}  (Forbidden - ada tapi blocked)")
            elif response.status_code == 401:
                print(f"  [401]  {test_url}  (Unauthorized - butuh login)")
            elif response.status_code in (301, 302):
                print(f"  [{response.status_code}]   {test_url}  (Redirect -> {response.headers.get('Location', '?')})")
        except:
            pass

    print(f"\n  [*] Selesai. {found_count} path ditemukan (200 OK).")
    input("\n[!] Tekan Enter untuk kembali...")


def network_info():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           NETWORK INFO - NMFS mode")
    print("="*55)

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print(f"""
    +-------------------------------------+
    |         NETWORK INFORMATION         |
    +-------------------------------------+
    |  Hostname    : {hostname}
    |  Local IP    : {local_ip}
    |  OS          : {platform.system()} {platform.release()}
    |  Architecture: {platform.machine()}
    |  Python Ver  : {platform.python_version()}
    +-------------------------------------+
    """)

    try:
        public_ip = requests.get('https://api.ipify.org', timeout=5).text
        print(f"  Public IP   : {public_ip}")
    except:
        print("  Public IP   : Gagal mengambil (no internet?)")

    input("\n[!] Tekan Enter untuk kembali...")


def evil_corp_detector():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           EVIL CORP DETECTOR")
    print("="*55)

    print("""
    +==========================================+
    |  who makes this tools???????????.        |
    |   AUTHOR: NMFS / unknown-1110            |
    |   github: github.com/unknown-1110        |
    +==========================================+
    """)

    target = input("\n[NMFS] Masukkan domain untuk diinvestigasi: ")

    evil_keywords = ['ecorp', 'e-corp', 'bank', 'evil', 'corp']

    print(f"\n[*] Investigating {target}...\n")

    is_evil = any(keyword in target.lower() for keyword in evil_keywords)

    if is_evil:
        print("  [WARNING] Target terkait dengan Evil Corp!")
        print("  NMFS: Execute operation!")
    else:
        print("  [OK] Target aman (untuk saat ini)")
        print("  NMFS: Stay vigilant, friend")

    input("\n[!] Tekan Enter untuk kembali...")


def hash_cracker():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           HASH CRACKER - NMFS mode")
    print("="*55)

    print("""
    Supported hash types:
    [1] MD5
    [2] SHA1
    [3] SHA256
    """)

    hash_type = input("\n[NMFS] Pilih tipe hash (1-3): ")
    target_hash = input("[NMFS] Masukkan hash yang mau di-crack: ").strip().lower()

    common_passwords = [
        'password', '123456', '123456789', 'qwerty', 'abc123', 'admin',
        'letmein', 'welcome', 'monkey', 'dragon', 'master', 'football',
        'shadow', 'baseball', 'superman', 'iloveyou', 'password123',
        '111111', '123123', 'pass', 'root', 'toor', 'test', 'guest',
        'login', 'hello', 'qwerty123', 'password1', '1q2w3e4r', 'changeme'
    ]

    print(f"\n[*] Brute forcing hash...\n")

    found = False
    for word in common_passwords:
        if hash_type == '1':
            hashed = hashlib.md5(word.encode()).hexdigest()
        elif hash_type == '2':
            hashed = hashlib.sha1(word.encode()).hexdigest()
        else:
            hashed = hashlib.sha256(word.encode()).hexdigest()

        print(f"  Trying: {word}...")

        if hashed == target_hash:
            print(f"\n  [CRACKED] Password: {word}")
            found = True
            break

    if not found:
        print("\n  [FAIL] Password not found in dictionary")

    input("\n[!] Tekan Enter untuk kembali...")


def geoip_tracker():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           GEOIP TRACKER - NMFS mode")
    print("="*55)

    target = input("\n[NMFS] Masukkan IP Address: ")

    try:
        response = requests.get(f'http://ip-api.com/json/{target}', timeout=5)
        data = response.json()

        if data['status'] == 'success':
            print(f"""
    +-------------------------------------+
    |         GEOIP INFORMATION           |
    +-------------------------------------+
    |  IP Address    : {data['query']}
    |  Country       : {data['country']} ({data['countryCode']})
    |  Region        : {data['regionName']}
    |  City          : {data['city']}
    |  ZIP Code      : {data['zip']}
    |  ISP           : {data['isp']}
    |  Organization  : {data['org']}
    |  Latitude      : {data['lat']}
    |  Longitude     : {data['lon']}
    +-------------------------------------+
            """)
            print(f"  Maps: https://www.google.com/maps?q={data['lat']},{data['lon']}")
        else:
            print("  [!] Failed to get location info")

    except Exception as e:
        print(f"  [!] Error: {e}")

    input("\n[!] Tekan Enter untuk kembali...")


def email_validator():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           EMAIL VALIDATOR - NMFS mode")
    print("="*55)

    email = input("\n[NMFS] Masukkan email address: ")

    pattern = r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        print("  [!] Invalid email format!")
    else:
        print(f"  [OK] Email format valid")

        domain = email.split('@')[1]
        print(f"  Domain: {domain}")

        try:
            socket.gethostbyname(domain)
            print(f"  [OK] Domain {domain} exists")
        except:
            print(f"  [?]  Domain {domain} might not exist")

        disposable = ['tempmail', '10minutemail', 'guerrillamail', 'mailinator', 'yopmail', 'throwam']
        is_disposable = any(d in domain.lower() for d in disposable)

        if is_disposable:
            print("  [WARNING] This looks like a temporary/disposable email!")

    input("\n[!] Tekan Enter untuk kembali...")


def password_generator():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           PASSWORD GENERATOR - NMFS mode")
    print("="*55)

    length = int(input("\n[NMFS] Panjang password (default 16): ") or 16)
    use_upper = input("[NMFS] Pakai huruf besar? (y/n): ").lower() == 'y'
    use_lower = input("[NMFS] Pakai huruf kecil? (y/n): ").lower() == 'y'
    use_digits = input("[NMFS] Pakai angka? (y/n): ").lower() == 'y'
    use_symbols = input("[NMFS] Pakai simbol? (y/n): ").lower() == 'y'

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += '!@#$%^&*()_+-=[]{}|;:,.<>?'

    if not characters:
        characters = string.ascii_letters + string.digits

    print("\n[*] Generated Passwords:\n")
    for i in range(5):
        password = ''.join(random.choice(characters) for _ in range(length))

        strength = "Weak"
        if len(password) >= 12 and any(c in password for c in '!@#$%^&*'):
            strength = "Strong"
        elif len(password) >= 8:
            strength = "Medium"

        print(f"  {i+1}. {password}  [{strength}]")

    input("\n[!] Tekan Enter untuk kembali...")


class LinkParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        tag_attr_map = {
            'a': 'href', 'link': 'href', 'script': 'src', 'img': 'src',
            'iframe': 'src', 'frame': 'src', 'embed': 'src', 'source': 'src',
            'form': 'action', 'area': 'href', 'base': 'href',
            'blockquote': 'cite', 'q': 'cite',
        }

        attr_name = tag_attr_map.get(tag)
        if attr_name and attr_name in attrs_dict:
            self._add_link(attrs_dict[attr_name].strip())

        for attr_name, val in attrs_dict.items():
            if attr_name in ('data-href', 'data-src', 'data-url') and val:
                self._add_link(val.strip())

    def _add_link(self, raw):
        if not raw:
            return
        if (raw.startswith('#') or raw.lower().startswith('javascript:') or
                raw.lower().startswith('mailto:') or raw.lower().startswith('tel:') or
                raw == 'void(0)'):
            return
        resolved = urljoin(self.base_url, raw)
        if resolved.startswith('http://') or resolved.startswith('https://'):
            self.links.add(resolved)


def link_extractor():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           LINK EXTRACTOR v2 - NMFS mode")
    print("="*55)

    url = input("\n[NMFS] Masukkan URL website: ").strip()
    if not url.startswith('http'):
        url = 'https://' + url

    show_all = input("[NMFS] Tampilkan semua link? (y/n, default n): ").lower() == 'y'
    filter_internal = input("[NMFS] Filter hanya link internal? (y/n, default n): ").lower() == 'y'

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        print(f"\n[*] Fetching {url}...")
        response = requests.get(url, timeout=15, headers=headers, allow_redirects=True)
        final_url = response.url

        print(f"  Status   : {response.status_code}")
        print(f"  Final URL: {final_url}")
        print(f"  Size     : {len(response.text):,} bytes")

        parser = LinkParser(base_url=final_url)
        parser.feed(response.text)

        all_links = sorted(parser.links)
        parsed_base = urlparse(final_url)
        base_domain = parsed_base.netloc

        if filter_internal:
            all_links = [l for l in all_links if urlparse(l).netloc == base_domain]

        total = len(all_links)
        internal = [l for l in all_links if urlparse(l).netloc == base_domain]
        external = [l for l in all_links if urlparse(l).netloc != base_domain]

        print(f"\n  Total link unik : {total}")
        print(f"  Internal link   : {len(internal)}")
        print(f"  External link   : {len(external)}\n")

        display_links = all_links if show_all else all_links[:50]

        for i, link in enumerate(display_links, 1):
            tag = "[INT]" if urlparse(link).netloc == base_domain else "[EXT]"
            display = link if len(link) <= 90 else link[:87] + "..."
            print(f"  {i:>4}. {tag} {display}")

        if not show_all and total > 50:
            print(f"\n  ... dan {total - 50} link lagi.")

        save = input("\n[NMFS] Simpan semua link ke file .txt? (y/n): ").lower()
        if save == 'y':
            filename = f"links_{base_domain.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Link Extractor Result\nURL: {final_url}\nTotal: {total} links\n")
                f.write(f"Waktu: {datetime.now()}\n{'='*80}\n\n")
                for i, link in enumerate(all_links, 1):
                    f.write(f"{i}. {link}\n")
            print(f"  [OK] Disimpan ke: {filename}")

    except requests.exceptions.ConnectionError:
        print(f"  [!] Gagal connect ke {url}.")
    except Exception as e:
        print(f"  [!] Error: {e}")

    input("\n[!] Tekan Enter untuk kembali...")


def whois_lookup():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           WHOIS LOOKUP - NMFS mode")
    print("="*55)

    domain = input("\n[NMFS] Masukkan domain: ")

    try:
        print(f"\n[*] Looking up WHOIS for {domain}...\n")

        try:
            ip = socket.gethostbyname(domain)
            print(f"  IP Address: {ip}")
        except:
            print(f"  [!] Cannot resolve domain")

        try:
            result = subprocess.run(['whois', domain], capture_output=True, text=True, timeout=10)
            if result.stdout:
                lines = result.stdout.split('\n')
                keywords = ['Domain Name', 'Registrar', 'Creation Date', 'Expiry Date',
                            'Name Server', 'Status', 'Updated Date', 'Registrant']
                important_info = []
                for line in lines[:80]:
                    for keyword in keywords:
                        if keyword.lower() in line.lower():
                            important_info.append(line.strip())
                            break
                if important_info:
                    print("\n  WHOIS Data:")
                    for info in important_info[:20]:
                        print(f"    {info}")
                else:
                    print("  No detailed WHOIS data found")
            else:
                print("  WHOIS command returned no data")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            print("  [!] WHOIS command not available. Install: sudo apt install whois")

    except Exception as e:
        print(f"  [!] Error: {e}")

    input("\n[!] Tekan Enter untuk kembali...")


def ssl_checker():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           SSL/TLS CHECKER - NMFS mode")
    print("="*55)

    target = input("\n[NMFS] Masukkan domain (contoh: google.com): ").strip()
    target = target.replace('https://', '').replace('http://', '').split('/')[0]
    port = int(input("[NMFS] Port (default 443): ").strip() or 443)

    print(f"\n[*] Checking SSL/TLS certificate for {target}:{port}...\n")

    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((target, port), timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=target) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
                version = ssock.version()

        subject = dict(x[0] for x in cert.get('subject', []))
        issuer = dict(x[0] for x in cert.get('issuer', []))
        not_before = cert.get('notBefore', 'N/A')
        not_after = cert.get('notAfter', 'N/A')

        try:
            expire_date = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
            days_left = (expire_date - datetime.utcnow()).days
            if days_left <= 0:
                expire_status = f"EXPIRED {abs(days_left)} hari lalu!"
            elif days_left <= 30:
                expire_status = f"AKAN EXPIRE dalam {days_left} hari!"
            else:
                expire_status = f"Valid ({days_left} hari lagi)"
        except:
            expire_status = "N/A"

        san_list = []
        for san_type, san_val in cert.get('subjectAltName', []):
            san_list.append(f"{san_type}:{san_val}")

        print(f"  +---------------------------------------------+")
        print(f"  |          SSL CERTIFICATE INFO               |")
        print(f"  +---------------------------------------------+")
        print(f"  |  Common Name    : {subject.get('commonName', 'N/A')}")
        print(f"  |  Organization   : {subject.get('organizationName', 'N/A')}")
        print(f"  |  Issued By      : {issuer.get('commonName', 'N/A')}")
        print(f"  |  Issuer Org     : {issuer.get('organizationName', 'N/A')}")
        print(f"  |  Valid From     : {not_before}")
        print(f"  |  Valid Until    : {not_after}")
        print(f"  |  Status         : {expire_status}")
        print(f"  |  TLS Version    : {version}")
        print(f"  |  Cipher Suite   : {cipher[0]}")
        print(f"  |  Key Bits       : {cipher[2]}")
        print(f"  +---------------------------------------------+")

        if san_list:
            print(f"\n  Subject Alternative Names ({len(san_list)}):")
            for san in san_list[:15]:
                print(f"    -> {san}")
            if len(san_list) > 15:
                print(f"    ... dan {len(san_list) - 15} lagi")

        print("\n  Security Assessment:")
        if version in ('TLSv1.2', 'TLSv1.3'):
            print(f"    [OK]   TLS version {version}")
        else:
            print(f"    [WARN] TLS version {version} -- terlalu lama, upgrade disarankan")

        if cipher[2] and cipher[2] >= 256:
            print(f"    [OK]   Key strength {cipher[2]} bit -- Strong")
        elif cipher[2] and cipher[2] >= 128:
            print(f"    [OK]   Key strength {cipher[2]} bit -- Acceptable")
        else:
            print(f"    [FAIL] Key strength {cipher[2]} bit -- Weak!")

    except ssl.SSLCertVerificationError as e:
        print(f"  [!] SSL Verification Error: {e}")
    except ConnectionRefusedError:
        print(f"  [!] Connection refused ke {target}:{port}")
    except socket.timeout:
        print(f"  [!] Timeout saat connect ke {target}:{port}")
    except Exception as e:
        print(f"  [!] Error: {e}")

    input("\n[!] Tekan Enter untuk kembali...")


def robots_sitemap_viewer():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           ROBOTS.TXT & SITEMAP VIEWER - NMFS mode")
    print("="*55)

    url = input("\n[NMFS] Masukkan base URL (contoh: https://example.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url
    url = url.rstrip('/')

    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1)'}
    print(f"\n[*] Fetching robots.txt...\n")
    sitemap_list = []

    try:
        r = requests.get(f"{url}/robots.txt", timeout=10, headers=headers)
        if r.status_code == 200:
            print(f"  [OK] robots.txt ditemukan ({len(r.text)} bytes)\n")
            print("  " + "-" * 46)

            disallow_list = []
            allow_list = []

            for line in r.text.splitlines():
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if line.lower().startswith('user-agent:'):
                    current_agent = line.split(':', 1)[1].strip()
                    print(f"\n  User-Agent: {current_agent}")
                elif line.lower().startswith('disallow:'):
                    path = line.split(':', 1)[1].strip()
                    if path:
                        disallow_list.append(path)
                        print(f"    Disallow : {path}")
                elif line.lower().startswith('allow:'):
                    path = line.split(':', 1)[1].strip()
                    if path:
                        allow_list.append(path)
                        print(f"    Allow    : {path}")
                elif line.lower().startswith('sitemap:'):
                    sm = line.split(':', 1)[1].strip()
                    sitemap_list.append(sm)
                    print(f"    Sitemap  : {sm}")
                else:
                    print(f"    {line}")

            print(f"\n  Ringkasan:")
            print(f"    Disallow paths : {len(disallow_list)}")
            print(f"    Allow paths    : {len(allow_list)}")
            print(f"    Sitemap refs   : {len(sitemap_list)}")

            if disallow_list:
                interesting = [p for p in disallow_list if any(
                    kw in p.lower() for kw in
                    ['admin', 'api', 'backup', 'config', 'login', 'secret',
                     'private', 'internal', 'test', 'dev', 'staging', 'db']
                )]
                if interesting:
                    print(f"\n  [!] Interesting Disallow Paths:")
                    for p in interesting:
                        print(f"    -> {url}{p}")
        else:
            print(f"  [!] robots.txt tidak ditemukan (HTTP {r.status_code})")

    except Exception as e:
        print(f"  [!] Error fetching robots.txt: {e}")

    print(f"\n[*] Fetching sitemap.xml...\n")
    sitemap_urls_to_check = sitemap_list if sitemap_list else [f"{url}/sitemap.xml", f"{url}/sitemap_index.xml"]
    all_sitemap_urls = []

    for sm_url in sitemap_urls_to_check[:3]:
        try:
            r = requests.get(sm_url, timeout=10, headers=headers)
            if r.status_code == 200:
                print(f"  [OK] Sitemap: {sm_url}")
                locs = re.findall(r'<loc>\s*(.*?)\s*</loc>', r.text, re.IGNORECASE)
                all_sitemap_urls.extend(locs)
                print(f"    -> {len(locs)} URL ditemukan")
            else:
                print(f"  [!] {sm_url} -> HTTP {r.status_code}")
        except Exception as e:
            print(f"  [!] Error: {e}")

    if all_sitemap_urls:
        print(f"\n  Total URL dari sitemap: {len(all_sitemap_urls)}")
        print(f"  (Menampilkan 20 pertama)\n")
        for i, u in enumerate(all_sitemap_urls[:20], 1):
            print(f"  {i:>4}. {u}")
        if len(all_sitemap_urls) > 20:
            print(f"\n  ... dan {len(all_sitemap_urls) - 20} URL lagi")

        save = input("\n[NMFS] Simpan semua sitemap URL ke file? (y/n): ").lower()
        if save == 'y':
            fname = f"sitemap_{urlparse(url).netloc.replace('.', '_')}.txt"
            with open(fname, 'w') as f:
                for u in all_sitemap_urls:
                    f.write(u + '\n')
            print(f"  [OK] Disimpan ke: {fname}")

    input("\n[!] Tekan Enter untuk kembali...")


def header_analyzer():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           HTTP HEADER ANALYZER - NMFS mode")
    print("           Analisis security headers website")
    print("="*55)

    url = input("\n[NMFS] Masukkan URL (contoh: https://example.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url

    print(f"\n[*] Fetching headers dari {url}...\n")

    try:
        req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, timeout=10, headers=req_headers, allow_redirects=True)
        resp_headers = response.headers

        print(f"  Status Code  : {response.status_code}")
        print(f"  Final URL    : {response.url}\n")

        print("  All Response Headers:")
        print("  " + "-" * 46)
        for k, v in resp_headers.items():
            print(f"    {k:<35}: {v[:80]}")

        print("\n\n  Security Header Analysis:")
        print("  " + "-" * 46)

        security_headers = {
            'Strict-Transport-Security': {'desc': 'HSTS -- paksa HTTPS', 'good': lambda v: 'max-age=' in v.lower()},
            'Content-Security-Policy': {'desc': 'CSP -- cegah XSS & injection', 'good': lambda v: len(v) > 5},
            'X-Frame-Options': {'desc': 'Cegah Clickjacking', 'good': lambda v: v.upper() in ('DENY', 'SAMEORIGIN')},
            'X-Content-Type-Options': {'desc': 'Cegah MIME sniffing', 'good': lambda v: v.lower() == 'nosniff'},
            'Referrer-Policy': {'desc': 'Kontrol Referrer info', 'good': lambda v: len(v) > 0},
            'Permissions-Policy': {'desc': 'Batasi browser API', 'good': lambda v: len(v) > 0},
            'X-XSS-Protection': {'desc': 'XSS filter (legacy)', 'good': lambda v: v.startswith('1')},
            'Cross-Origin-Opener-Policy': {'desc': 'Isolasi cross-origin', 'good': lambda v: len(v) > 0},
        }

        score = 0
        max_score = len(security_headers)

        for header, info in security_headers.items():
            val = resp_headers.get(header)
            if val:
                is_good = info['good'](val)
                status = "[OK]  " if is_good else "[WARN]"
                if is_good:
                    score += 1
                print(f"  {status} {header}")
                print(f"         -> {info['desc']}")
                print(f"         -> Value: {val[:70]}")
            else:
                print(f"  [MISS] {header}")
                print(f"         -> {info['desc']}")

        print("\n\n  Technology Fingerprint (dari headers):")
        print("  " + "-" * 46)
        leaky = {
            'Server': 'Web server & versi', 'X-Powered-By': 'Backend technology',
            'X-AspNet-Version': 'ASP.NET version', 'X-Generator': 'CMS generator',
            'X-Drupal-Cache': 'Drupal CMS', 'X-Pingback': 'WordPress XML-RPC',
        }
        found_leak = False
        for h, desc in leaky.items():
            val = resp_headers.get(h)
            if val:
                print(f"  [LEAK] {h}: {val}  <- {desc}")
                found_leak = True
        if not found_leak:
            print("  [OK] Tidak ada header teknologi yang bocor")

        percentage = int((score / max_score) * 100)
        grade = "A" if percentage >= 80 else "B" if percentage >= 60 else "C" if percentage >= 40 else "D"
        print(f"\n  Security Score: {score}/{max_score} ({percentage}%) -- Grade: {grade}")

    except Exception as e:
        print(f"  [!] Error: {e}")

    input("\n[!] Tekan Enter untuk kembali...")


def banner_grabber():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           BANNER GRABBER - NMFS mode")
    print("="*55)

    target = input("\n[NMFS] Masukkan IP/Domain: ").strip()
    port_input = input("[NMFS] Port yang mau digrab (pisah koma, contoh: 21,22,80,443): ").strip()

    try:
        ports = [int(p.strip()) for p in port_input.split(',')]
    except:
        print("  [!] Format port tidak valid")
        input("\n[!] Tekan Enter untuk kembali...")
        return

    http_ports = {80, 443, 8080, 8443, 8000, 8888}
    print(f"\n[*] Grabbing banners dari {target}...\n")

    for port in ports:
        print(f"  Port {port}:")
        try:
            if port in http_ports or port == 443:
                scheme = 'https' if port in (443, 8443) else 'http'
                try:
                    r = requests.get(
                        f"{scheme}://{target}:{port}", timeout=5,
                        headers={'User-Agent': 'Mozilla/5.0'}, verify=False
                    )
                    server = r.headers.get('Server', 'N/A')
                    powered = r.headers.get('X-Powered-By', 'N/A')
                    print(f"    Status     : HTTP {r.status_code}")
                    print(f"    Server     : {server}")
                    print(f"    X-Powered  : {powered}")
                    title_match = re.search(r'<title>(.*?)</title>', r.text[:2000], re.IGNORECASE)
                    if title_match:
                        print(f"    Page Title : {title_match.group(1).strip()[:80]}")
                except requests.exceptions.SSLError:
                    print(f"    [!] SSL error pada port {port}")
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((target, port))
                try:
                    sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                except:
                    pass
                try:
                    banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                    if banner:
                        for line in banner.splitlines()[:6]:
                            if line.strip():
                                print(f"    {line.strip()[:100]}")
                    else:
                        print(f"    (no banner)")
                except:
                    print(f"    (tidak bisa baca banner)")
                sock.close()
        except (ConnectionRefusedError, socket.timeout):
            print(f"    [CLOSED] Port tidak terbuka atau timeout")
        except Exception as e:
            print(f"    [!] Error: {e}")
        print()

    input("\n[!] Tekan Enter untuk kembali...")


def http_response_timer():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           HTTP RESPONSE TIMER - NMFS mode")
    print("           Ukur kecepatan respon website")
    print("="*55)

    url = input("\n[NMFS] Masukkan URL (contoh: https://example.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url

    try:
        count = int(input("[NMFS] Jumlah request (default 5): ").strip() or 5)
    except:
        count = 5

    print(f"\n[*] Mengirim {count} request ke {url}...\n")

    times = []
    status_codes = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for i in range(count):
        try:
            start = time.time()
            r = requests.get(url, timeout=15, headers=headers, allow_redirects=True)
            elapsed = (time.time() - start) * 1000
            times.append(elapsed)
            status_codes.append(r.status_code)
            bar = "#" * min(int(elapsed / 20), 50)
            print(f"  Request {i+1:>2} : {elapsed:>8.1f} ms  [{r.status_code}]  {bar}")
        except requests.exceptions.Timeout:
            print(f"  Request {i+1:>2} : TIMEOUT")
            times.append(15000)
            status_codes.append(0)
        except Exception as e:
            print(f"  Request {i+1:>2} : ERROR - {e}")
        time.sleep(0.3)

    if times:
        valid_times = [t for t in times if t < 15000]
        if valid_times:
            avg = sum(valid_times) / len(valid_times)
            mn = min(valid_times)
            mx = max(valid_times)
            print(f"\n  +-------------------------------------+")
            print(f"  |          STATISTIK RESPONSE         |")
            print(f"  +-------------------------------------+")
            print(f"  |  Total Request : {count}")
            print(f"  |  Sukses        : {len(valid_times)}")
            print(f"  |  Timeout       : {times.count(15000)}")
            print(f"  |  Min           : {mn:.1f} ms")
            print(f"  |  Max           : {mx:.1f} ms")
            print(f"  |  Average       : {avg:.1f} ms")
            print(f"  +-------------------------------------+")

            if avg < 200:
                verdict = "SANGAT CEPAT"
            elif avg < 500:
                verdict = "NORMAL"
            elif avg < 1000:
                verdict = "LAMBAT"
            else:
                verdict = "SANGAT LAMBAT"

            print(f"\n  Verdict : {verdict}")

    input("\n[!] Tekan Enter untuk kembali...")


def open_redirect_checker():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           OPEN REDIRECT CHECKER - NMFS mode")
    print("           Deteksi kerentanan open redirect")
    print("="*55)

    url = input("\n[NMFS] Masukkan base URL (contoh: https://example.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url
    url = url.rstrip('/')

    redirect_payloads = [
        '//evil.com', '///evil.com', 'https://evil.com',
        'http://evil.com', '//evil.com/%2F..', '/\\evil.com',
        '/%09/evil.com', '/%2F%2Fevil.com', 'https:evil.com',
    ]

    common_params = [
        'redirect', 'url', 'next', 'return', 'returnUrl', 'return_url',
        'goto', 'redir', 'redirect_url', 'redirect_uri', 'destination',
        'target', 'link', 'out', 'view', 'to', 'checkout_url', 'continue',
        'forward', 'location', 'go', 'ref', 'login_url', 'callback'
    ]

    print(f"\n[*] Testing {url} untuk open redirect...\n")

    vulnerable = []
    tested = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for param in common_params:
        for payload in redirect_payloads[:3]:
            test_url = f"{url}?{param}={payload}"
            tested += 1
            try:
                r = requests.get(test_url, timeout=5, headers=headers, allow_redirects=False)
                location = r.headers.get('Location', '')
                if location and ('evil.com' in location or location.startswith('//')):
                    print(f"  [VULN] Param: {param} | Payload: {payload}")
                    print(f"         Status: {r.status_code} | Location: {location}")
                    vulnerable.append(test_url)
                else:
                    print(f"  [SAFE] ?{param}={payload[:30]}  -> {r.status_code}")
            except:
                pass

    print(f"\n  [*] Tested  : {tested} kombinasi")
    print(f"  [*] Vulnerable: {len(vulnerable)}")

    if vulnerable:
        print(f"\n  VULNERABLE ENDPOINTS:")
        for v in vulnerable:
            print(f"    -> {v}")
    else:
        print("\n  [OK] Tidak ditemukan open redirect.")

    input("\n[!] Tekan Enter untuk kembali...")


def reverse_ip_lookup():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           REVERSE IP LOOKUP - NMFS mode")
    print("           Cari domain lain di IP yang sama")
    print("="*55)

    target = input("\n[NMFS] Masukkan IP Address atau domain: ").strip()

    if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', target):
        try:
            ip = socket.gethostbyname(target)
            print(f"\n  [*] Resolved {target} -> {ip}")
            target_ip = ip
        except:
            print(f"  [!] Tidak bisa resolve domain: {target}")
            input("\n[!] Tekan Enter untuk kembali...")
            return
    else:
        target_ip = target

    print(f"\n[*] Reverse IP Lookup untuk {target_ip}...\n")
    found_domains = set()

    try:
        hostname = socket.gethostbyaddr(target_ip)
        if hostname[0]:
            found_domains.add(hostname[0])
            print(f"  [PTR Record] {hostname[0]}")
        if hostname[1]:
            for alias in hostname[1]:
                found_domains.add(alias)
                print(f"  [Alias]      {alias}")
    except Exception as e:
        print(f"  [!] Error PTR: {e}")

    print(f"\n[*] Mencoba HackerTarget API (gratis)...")
    try:
        r = requests.get(
            f"https://api.hackertarget.com/reverseiplookup/?q={target_ip}",
            timeout=10, headers={'User-Agent': 'Mozilla/5.0'}
        )
        if r.status_code == 200 and 'error' not in r.text.lower()[:20]:
            domains = [d.strip() for d in r.text.splitlines() if d.strip()]
            for d in domains:
                found_domains.add(d)
            print(f"  [OK] HackerTarget: {len(domains)} domain ditemukan")
        else:
            print(f"  [!] HackerTarget: {r.text[:100]}")
    except Exception as e:
        print(f"  [!] HackerTarget error: {e}")

    if found_domains:
        print(f"\n  Total domain ditemukan di {target_ip}: {len(found_domains)}\n")
        for i, domain in enumerate(sorted(found_domains), 1):
            print(f"  {i:>4}. {domain}")

        save = input("\n[NMFS] Simpan ke file? (y/n): ").lower()
        if save == 'y':
            fname = f"reverseip_{target_ip.replace('.', '_')}.txt"
            with open(fname, 'w') as f:
                f.write(f"Reverse IP Lookup: {target_ip}\nWaktu: {datetime.now()}\n{'='*50}\n")
                for d in sorted(found_domains):
                    f.write(d + "\n")
            print(f"  [OK] Disimpan ke: {fname}")
    else:
        print(f"\n  [!] Tidak ada domain ditemukan untuk {target_ip}")

    input("\n[!] Tekan Enter untuk kembali...")


def url_param_fuzzer():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           URL PARAMETER FUZZER - NMFS mode")
    print("           Fuzz GET parameter untuk temukan anomali")
    print("="*55)

    url = input("\n[NMFS] Masukkan URL target (contoh: https://example.com/page): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url

    param = input("[NMFS] Nama parameter yang mau difuzz (contoh: id): ").strip()
    if not param:
        print("  [!] Nama parameter tidak boleh kosong")
        input("\n[!] Tekan Enter untuk kembali...")
        return

    fuzz_payloads = [
        "1", "0", "-1", "9999", "' OR '1'='1", "\" OR \"1\"=\"1",
        "<script>alert(1)</script>", "../../../etc/passwd",
        "../../../../windows/win.ini", "%00", "null", "undefined",
        "true", "false", "[]", "{}", "1;DROP TABLE users--",
        "admin", "test", "' UNION SELECT NULL--", "%27",
        "1 AND 1=1", "1 AND 1=2", "{{7*7}}", "${7*7}",
        "1|whoami", "; ls -la", "&& id", "| cat /etc/passwd"
    ]

    baseline_url = f"{url}?{param}=BASELINE_VALUE_12345"
    print(f"\n[*] Mengambil baseline response...\n")

    try:
        baseline_r = requests.get(baseline_url, timeout=8,
                                   headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True)
        baseline_status = baseline_r.status_code
        baseline_len = len(baseline_r.text)
        print(f"  Baseline Status : {baseline_status}")
        print(f"  Baseline Length : {baseline_len} bytes")
    except Exception as e:
        print(f"  [!] Gagal ambil baseline: {e}")
        input("\n[!] Tekan Enter untuk kembali...")
        return

    print(f"\n[*] Mulai fuzzing parameter '{param}' dengan {len(fuzz_payloads)} payload...\n")
    print(f"  {'PAYLOAD':<35} {'STATUS':>7}  {'LENGTH':>8}  {'DIFF':>8}  FLAG")
    print("  " + "-" * 70)

    anomalies = []

    for payload in fuzz_payloads:
        test_url = f"{url}?{param}={requests.utils.quote(payload)}"
        try:
            r = requests.get(test_url, timeout=8, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True)
            status = r.status_code
            length = len(r.text)
            diff = length - baseline_len

            flags = []
            if status != baseline_status:
                flags.append("STATUS-CHANGE")
            if abs(diff) > 500:
                flags.append("SIZE-DIFF")
            if status == 500:
                flags.append("SERVER-ERROR")
            if re.search(r'(sql|mysql|syntax|error|warning|exception)', r.text[:3000], re.IGNORECASE):
                flags.append("ERROR-MSG")
            if status in (301, 302, 303, 307, 308):
                flags.append("REDIRECT")

            flag_str = " | ".join(flags) if flags else "-"
            short_payload = payload[:33] + ".." if len(payload) > 35 else payload
            diff_str = f"+{diff}" if diff > 0 else str(diff)

            line = f"  {short_payload:<35} {status:>7}  {length:>8}  {diff_str:>8}  {flag_str}"
            if flags:
                print(f"\033[93m{line}\033[0m")
                anomalies.append({'payload': payload, 'url': test_url, 'status': status, 'flags': flags})
            else:
                print(line)

        except requests.exceptions.Timeout:
            print(f"  {payload[:35]:<35} {'TIMEOUT':>7}")
        except Exception as e:
            print(f"  {payload[:35]:<35} {'ERROR':>7}  {str(e)[:30]}")

    print(f"\n  [*] Selesai. {len(anomalies)} anomali ditemukan dari {len(fuzz_payloads)} payload.")
    if anomalies:
        print(f"\n  ANOMALI TERDETEKSI:")
        for a in anomalies:
            print(f"    -> [{', '.join(a['flags'])}] {a['url'][:90]}")

    input("\n[!] Tekan Enter untuk kembali...")


def tech_stack_detector():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           TECH STACK DETECTOR - NMFS mode")
    print("           Identifikasi teknologi di balik website")
    print("="*55)

    url = input("\n[NMFS] Masukkan URL target (contoh: https://example.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url

    print(f"\n[*] Menganalisis {url}...\n")

    try:
        req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        r = requests.get(url, timeout=10, headers=req_headers, allow_redirects=True)
        headers = r.headers
        body = r.text[:50000]
    except Exception as e:
        print(f"  [!] Gagal fetch URL: {e}")
        input("\n[!] Tekan Enter untuk kembali...")
        return

    findings = {}
    server = headers.get('Server', '')
    powered = headers.get('X-Powered-By', '')
    generator = headers.get('X-Generator', '')
    via = headers.get('Via', '')

    if server: findings['Web Server'] = server
    if powered: findings['Backend'] = powered
    if generator: findings['Generator'] = generator
    if via: findings['Proxy/CDN'] = via

    cms_signatures = {
        'WordPress': [r'wp-content/', r'wp-includes/', r'wp-json/'],
        'Joomla': [r'/components/com_', r'Joomla!', r'/media/jui/'],
        'Drupal': [r'Drupal\.settings', r'/sites/default/files/'],
        'Magento': [r'Mage\.', r'/skin/frontend/', r'magento'],
        'Shopify': [r'cdn\.shopify\.com', r'Shopify\.theme'],
        'Laravel': [r'laravel_session', r'XSRF-TOKEN'],
        'Django': [r'csrfmiddlewaretoken', r'django'],
        'Ruby on Rails': [r'authenticity_token', r'rails'],
        'Next.js': [r'__NEXT_DATA__', r'/_next/static/'],
        'React': [r'react\.development\.js', r'react-dom', r'data-reactroot'],
        'Vue.js': [r'vue\.js', r'__vue__', r'v-bind:'],
        'Angular': [r'ng-version', r'angular\.js', r'ng-app'],
        'Bootstrap': [r'bootstrap\.min\.css', r'bootstrap\.bundle'],
        'jQuery': [r'jquery\.min\.js', r'jquery-\d'],
        'Cloudflare': [r'__cf_bm', r'cf-ray', r'cloudflare'],
        'Google Analytics': [r'google-analytics\.com', r'gtag\('],
        'reCAPTCHA': [r'recaptcha', r'google\.com/recaptcha'],
    }

    detected_tech = {}
    combined_text = body + str(dict(headers))

    for tech, patterns in cms_signatures.items():
        for pattern in patterns:
            if re.search(pattern, combined_text, re.IGNORECASE):
                detected_tech[tech] = True
                break

    print(f"  Status Code : {r.status_code}")
    print(f"  Final URL   : {r.url}")
    print(f"  Page Size   : {len(body):,} bytes\n")
    print("  +---------------------------------------------+")
    print("  |          TECH STACK DETECTION RESULT        |")
    print("  +---------------------------------------------+")

    if findings:
        print("\n  [Headers]")
        for k, v in findings.items():
            print(f"    {k:<20} : {v}")

    if detected_tech:
        print("\n  [Detected Technologies]")
        for tech in sorted(detected_tech.keys()):
            print(f"    [+] {tech}")
    else:
        print("\n  [?] Tidak ada teknologi spesifik yang terdeteksi")

    title_match = re.search(r'<title>(.*?)</title>', body, re.IGNORECASE | re.DOTALL)
    if title_match:
        print(f"\n  Page Title : {title_match.group(1).strip()[:100]}")

    input("\n[!] Tekan Enter untuk kembali...")


def cookie_analyzer():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           COOKIE ANALYZER - NMFS mode")
    print("           Analisis security flag pada cookies")
    print("="*55)

    url = input("\n[NMFS] Masukkan URL target (contoh: https://example.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url

    print(f"\n[*] Mengambil cookies dari {url}...\n")

    try:
        session = requests.Session()
        r = session.get(url, timeout=10,
                        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'},
                        allow_redirects=True)

        raw_cookies = r.headers.get('Set-Cookie', '')
        all_set_cookie = r.raw.headers.getlist('Set-Cookie') if hasattr(r.raw.headers, 'getlist') else []
        if not all_set_cookie and raw_cookies:
            all_set_cookie = [raw_cookies]

        cookies_from_jar = session.cookies

        if not all_set_cookie and not cookies_from_jar:
            print("  [!] Tidak ada cookie yang ditemukan dari response ini.")
            input("\n[!] Tekan Enter untuk kembali...")
            return

        print(f"  Status     : {r.status_code}")
        print(f"  Final URL  : {r.url}")
        print(f"  Cookies    : {len(list(cookies_from_jar))} cookie ditemukan\n")

        total_issues = 0

        if all_set_cookie:
            print("  " + "="*51)
            print("  Analisis dari Set-Cookie headers (raw):")
            print("  " + "="*51)

            for raw_cookie in all_set_cookie:
                parts = [p.strip() for p in raw_cookie.split(';')]
                if not parts:
                    continue

                name_val = parts[0]
                name = name_val.split('=')[0].strip() if '=' in name_val else name_val
                attrs_lower = [p.lower() for p in parts[1:]]

                has_httponly = any('httponly' in a for a in attrs_lower)
                has_secure = any(a.strip() == 'secure' for a in attrs_lower)
                has_samesite = any('samesite' in a for a in attrs_lower)
                samesite_val = next((a.split('=')[1].strip() for a in attrs_lower if 'samesite' in a), None)
                has_path = any('path' in a for a in attrs_lower)
                has_domain = any('domain' in a for a in attrs_lower)
                has_expires = any('expires' in a or 'max-age' in a for a in attrs_lower)

                print(f"\n  Cookie : {name}")
                print(f"  Raw    : {raw_cookie[:100]}{'...' if len(raw_cookie) > 100 else ''}\n")

                issues = []
                if has_httponly:
                    print(f"    [OK]  HttpOnly    : Set")
                else:
                    print(f"    [!!]  HttpOnly    : MISSING -- rentan XSS cookie theft!")
                    issues.append("Missing HttpOnly")

                if has_secure:
                    print(f"    [OK]  Secure      : Set")
                else:
                    if url.startswith('https'):
                        print(f"    [!!]  Secure      : MISSING -- cookie bisa dikirim via HTTP!")
                        issues.append("Missing Secure on HTTPS site")
                    else:
                        print(f"    [?]   Secure      : MISSING (site pakai HTTP)")

                if has_samesite:
                    sv = samesite_val.capitalize() if samesite_val else "Unknown"
                    if sv.lower() == 'none':
                        print(f"    [!!]  SameSite    : {sv} -- rentan CSRF!")
                        issues.append("SameSite=None")
                    elif sv.lower() == 'lax':
                        print(f"    [OK]  SameSite    : {sv}")
                    elif sv.lower() == 'strict':
                        print(f"    [OK]  SameSite    : {sv}")
                else:
                    print(f"    [!!]  SameSite    : MISSING -- risiko CSRF")
                    issues.append("Missing SameSite")

                print(f"    [i]   Persistent  : {'Ya (Expires/Max-Age)' if has_expires else 'Session cookie'}")

                if issues:
                    print(f"\n    Masalah: {len(issues)}")
                    for iss in issues:
                        print(f"      - {iss}")
                    total_issues += len(issues)
                else:
                    print(f"\n    [OK] Cookie ini sudah aman")

        print(f"\n  Total masalah keamanan cookie: {total_issues}")

    except Exception as e:
        print(f"  [!] Error: {e}")

    input("\n[!] Tekan Enter untuk kembali...")


def cors_checker():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           CORS MISCONFIGURATION CHECKER - NMFS mode")
    print("           Deteksi kerentanan CORS pada target")
    print("="*55)

    url = input("\n[NMFS] Masukkan URL target (contoh: https://api.example.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url

    print(f"\n[*] Mengecek CORS misconfiguration pada {url}...\n")

    test_origins = [
        "https://evil.com", "https://attacker.com", "null",
        f"https://evil.{urlparse(url).netloc}",
        f"https://{urlparse(url).netloc}.evil.com",
        "http://localhost", "https://127.0.0.1",
    ]

    issues = []
    base_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Accept': '*/*'}

    print(f"  {'ORIGIN':<45} {'ACAO':>5}  {'ACAC':>5}  RESULT")
    print("  " + "-" * 75)

    for origin in test_origins:
        req_headers = {**base_headers, 'Origin': origin}
        try:
            r = requests.get(url, timeout=8, headers=req_headers, allow_redirects=True)
            acao = r.headers.get('Access-Control-Allow-Origin', '-')
            acac = r.headers.get('Access-Control-Allow-Credentials', '-')

            vulnerable = False
            result = "SAFE"

            if acao == '*':
                result = "WILDCARD (*)"
                vulnerable = True
            elif acao == origin:
                if acac.lower() == 'true':
                    result = "VULN! ACAO=Origin + ACAC=true"
                    vulnerable = True
                    issues.append({'origin': origin, 'acao': acao, 'acac': acac,
                                   'severity': 'HIGH', 'desc': 'Full CORS bypass!'})
                else:
                    result = "REFLECTED (no creds)"
            elif acao == 'null' and origin == 'null':
                result = "NULL ORIGIN ALLOWED"
                vulnerable = True

            short_origin = origin[:43] + ".." if len(origin) > 45 else origin
            acao_short = acao[:4] if acao and acao != '-' else '-'
            flag = "[VULN]" if vulnerable else "[ OK ]"
            print(f"  {short_origin:<45} {acao_short:>5}  {acac[:4]:>5}  {flag} {result}")

        except Exception as e:
            print(f"  {origin[:45]:<45} ERROR: {str(e)[:30]}")

    print(f"\n  {'='*55}")
    if not issues:
        print("  [OK] Tidak ditemukan CORS misconfiguration yang jelas.")
    else:
        print(f"  [!!] Ditemukan {len(issues)} potensi CORS misconfiguration!")
        for iss in issues:
            print(f"    Severity : {iss['severity']}")
            print(f"    Origin   : {iss['origin']}")
            print(f"    Desc     : {iss['desc']}")

    input("\n[!] Tekan Enter untuk kembali...")


def cidr_calculator():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           IP RANGE CALCULATOR / CIDR TOOL - NMFS mode")
    print("           Kalkulasi subnet, range IP, dan broadcast")
    print("="*55)

    print("""
    Pilih mode:
    [1] CIDR ke IP Range (contoh: 192.168.1.0/24)
    [2] IP + Subnet Mask ke Range (contoh: 192.168.1.0 + 255.255.255.0)
    [3] Hitung CIDR yang dibutuhkan dari jumlah host
    [4] Bandingkan apakah IP ada dalam network
    """)

    mode = input("[NMFS] Pilih mode (1-4): ").strip()

    if mode == '1':
        cidr_input = input("\n[NMFS] Masukkan CIDR (contoh: 192.168.1.0/24): ").strip()
        try:
            net = ipaddress.ip_network(cidr_input, strict=False)
            hosts = list(net.hosts())
            print(f"\n  +---------------------------------------------+")
            print(f"  |          CIDR CALCULATION RESULT           |")
            print(f"  +---------------------------------------------+")
            print(f"  Network Address   : {net.network_address}")
            print(f"  Broadcast Address : {net.broadcast_address}")
            print(f"  Subnet Mask       : {net.netmask}")
            print(f"  Wildcard Mask     : {net.hostmask}")
            print(f"  Prefix Length     : /{net.prefixlen}")
            print(f"  Total Addresses   : {net.num_addresses}")
            print(f"  Usable Hosts      : {len(hosts)}")
            if hosts:
                print(f"  First Host        : {hosts[0]}")
                print(f"  Last Host         : {hosts[-1]}")
            print(f"  IP Version        : IPv{net.version}")
            print(f"  Is Private        : {'Ya' if net.is_private else 'Tidak'}")

            if net.num_addresses <= 256:
                show = input("\n[NMFS] Tampilkan semua IP? (y/n): ").lower()
                if show == 'y':
                    for i, ip in enumerate(net.hosts(), 1):
                        print(f"    {i:>5}. {ip}")
        except ValueError as e:
            print(f"  [!] CIDR tidak valid: {e}")

    elif mode == '2':
        ip_input = input("\n[NMFS] Masukkan IP Address: ").strip()
        mask_input = input("[NMFS] Masukkan Subnet Mask: ").strip()
        try:
            net = ipaddress.ip_network(f"{ip_input}/{mask_input}", strict=False)
            hosts = list(net.hosts())
            print(f"\n  Network Address   : {net.network_address}")
            print(f"  Broadcast Address : {net.broadcast_address}")
            print(f"  CIDR Notation     : {net.compressed}")
            print(f"  Usable Hosts      : {len(hosts)}")
        except ValueError as e:
            print(f"  [!] Input tidak valid: {e}")

    elif mode == '3':
        try:
            num_hosts = int(input("\n[NMFS] Masukkan jumlah host yang dibutuhkan: ").strip())
            prefix = 32
            while (2 ** (32 - prefix)) - 2 < num_hosts and prefix > 0:
                prefix -= 1
            net = ipaddress.ip_network(f"0.0.0.0/{prefix}", strict=False)
            print(f"\n  Untuk {num_hosts} host:")
            print(f"  Prefix yang dibutuhkan : /{prefix}")
            print(f"  Usable hosts           : {net.num_addresses - 2}")
            print(f"  Subnet mask            : {net.netmask}")
        except ValueError:
            print(f"  [!] Masukkan angka yang valid")

    elif mode == '4':
        ip_input = input("\n[NMFS] Masukkan IP yang mau dicek: ").strip()
        cidr_input = input("[NMFS] Masukkan network CIDR: ").strip()
        try:
            ip = ipaddress.ip_address(ip_input)
            net = ipaddress.ip_network(cidr_input, strict=False)
            if ip in net:
                print(f"\n  [YES] {ip} BERADA dalam network {net}")
            else:
                print(f"\n  [NO] {ip} TIDAK berada dalam network {net}")
        except ValueError as e:
            print(f"  [!] Input tidak valid: {e}")
    else:
        print("  [!] Pilihan tidak valid")

    input("\n[!] Tekan Enter untuk kembali...")


# ============================================================
# [NEW] TOOL 26: JWT DECODER
# Decode dan analisis JWT token tanpa library tambahan
# ============================================================
def jwt_decoder():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           JWT DECODER & ANALYZER - NMFS mode")
    print("           Decode & analisis JWT token")
    print("="*55)

    token = input("\n[NMFS] Masukkan JWT token: ").strip()

    parts = token.split('.')
    if len(parts) != 3:
        print("  [!] Bukan JWT valid (harus ada 3 bagian dipisah titik)")
        input("\n[!] Tekan Enter untuk kembali...")
        return

    import base64

    def b64_decode(data):
        data += '=' * (4 - len(data) % 4)
        try:
            return json.loads(base64.urlsafe_b64decode(data).decode('utf-8'))
        except:
            return None

    header = b64_decode(parts[0])
    payload = b64_decode(parts[1])
    signature = parts[2]

    print("\n  +---------------------------------------------+")
    print("  |                JWT ANALYSIS                 |")
    print("  +---------------------------------------------+")

    if header:
        print("\n  [HEADER]")
        for k, v in header.items():
            print(f"    {k:<15} : {v}")
        alg = header.get('alg', '')
        if alg.lower() == 'none':
            print(f"\n  [!!] CRITICAL: Algorithm = none -- JWT tidak terverifikasi!")
        elif alg.upper() in ('HS256', 'HS384', 'HS512'):
            print(f"  [*]  Algorithm: {alg} (Symmetric -- secret key dibutuhkan)")
        elif alg.upper() in ('RS256', 'RS384', 'RS512'):
            print(f"  [*]  Algorithm: {alg} (Asymmetric -- public key)")
    else:
        print("  [!] Gagal decode header")

    if payload:
        print("\n  [PAYLOAD]")
        for k, v in payload.items():
            print(f"    {k:<15} : {v}")

        # Cek expiry
        now = int(time.time())
        if 'exp' in payload:
            exp = payload['exp']
            exp_dt = datetime.utcfromtimestamp(exp).strftime('%Y-%m-%d %H:%M:%S UTC')
            if now > exp:
                print(f"\n  [!!] TOKEN SUDAH EXPIRED! Expired: {exp_dt}")
            else:
                sisa = exp - now
                print(f"\n  [OK]  Token masih valid. Expires: {exp_dt} ({sisa} detik lagi)")
        else:
            print(f"\n  [!]  Tidak ada 'exp' claim -- token tidak ada expiry!")

        if 'iat' in payload:
            iat_dt = datetime.utcfromtimestamp(payload['iat']).strftime('%Y-%m-%d %H:%M:%S UTC')
            print(f"  [*]  Issued at: {iat_dt}")

        # Cek sensitive data
        sensitive = ['password', 'pass', 'secret', 'key', 'token', 'card', 'ssn', 'credit']
        for k in payload.keys():
            if any(s in k.lower() for s in sensitive):
                print(f"  [!!] Data sensitif ditemukan di payload: '{k}' -- hindari simpan di JWT!")
    else:
        print("  [!] Gagal decode payload")

    print(f"\n  [SIGNATURE]")
    print(f"    {signature[:60]}{'...' if len(signature) > 60 else ''}")
    print(f"\n  [!] Note: Tool ini hanya decode, TIDAK verifikasi signature.")
    print(f"  [*]  github: https://github.com/unknown-1110")

    input("\n[!] Tekan Enter untuk kembali...")


# ============================================================
# [NEW] TOOL 27: HTTP METHOD TESTER
# Test method HTTP apa saja yang diizinkan server (GET, POST, PUT, DELETE, OPTIONS, dll)
# ============================================================
def http_method_tester():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           HTTP METHOD TESTER - NMFS mode")
    print("           Test allowed HTTP methods pada server")
    print("="*55)

    url = input("\n[NMFS] Masukkan URL target (contoh: https://example.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url

    methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD', 'TRACE', 'CONNECT']

    print(f"\n[*] Testing {len(methods)} HTTP methods pada {url}...\n")
    print(f"  {'METHOD':<10} {'STATUS':>7}  {'LENGTH':>8}  {'SERVER':<30}  INFO")
    print("  " + "-" * 75)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    dangerous_found = []

    for method in methods:
        try:
            r = requests.request(method, url, timeout=8, headers=headers,
                                  allow_redirects=False, verify=False)
            status = r.status_code
            length = len(r.content)
            server = r.headers.get('Server', 'N/A')[:28]
            allow_hdr = r.headers.get('Allow', '')

            info = ""
            if method == 'OPTIONS' and allow_hdr:
                info = f"Allow: {allow_hdr[:40]}"
            elif method == 'TRACE' and status == 200:
                info = "[!!] TRACE ENABLED -- XST risk!"
                dangerous_found.append("TRACE enabled -- rentan XST (Cross-Site Tracing)")
            elif method in ('PUT', 'DELETE') and status in (200, 201, 204):
                info = "[!!] DANGEROUS METHOD ALLOWED!"
                dangerous_found.append(f"{method} method allowed -- bisa modifikasi/hapus resource!")
            elif status == 200:
                info = "OK"
            elif status == 405:
                info = "Method Not Allowed"
            elif status == 403:
                info = "Forbidden"
            elif status in (301, 302):
                info = f"Redirect -> {r.headers.get('Location', '?')[:40]}"

            color = "\033[91m" if "[!!]" in info else "\033[92m" if status == 200 else "\033[0m"
            reset = "\033[0m"
            print(f"  {color}{method:<10} {status:>7}  {length:>8}  {server:<30}  {info}{reset}")

        except requests.exceptions.SSLError:
            print(f"  {method:<10} {'SSL ERR':>7}  {'':>8}  {'':30}  SSL Error")
        except requests.exceptions.Timeout:
            print(f"  {method:<10} {'TIMEOUT':>7}")
        except Exception as e:
            print(f"  {method:<10} {'ERROR':>7}  -- {str(e)[:40]}")

    if dangerous_found:
        print(f"\n  [!!] DANGEROUS FINDINGS:")
        for d in dangerous_found:
            print(f"    -> {d}")
    else:
        print(f"\n  [OK] Tidak ada method berbahaya yang ditemukan.")

    print(f"  [*]  github: https://github.com/unknown-1110")
    input("\n[!] Tekan Enter untuk kembali...")


# ============================================================
# [NEW] TOOL 28: ENCODE / DECODE TOOL
# Multi-format encode & decode: Base64, URL, Hex, HTML Entity, ROT13
# ============================================================
def encode_decode_tool():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           ENCODE / DECODE TOOL - NMFS mode")
    print("           Multi-format encoder & decoder")
    print("="*55)

    import base64
    import urllib.parse
    import html
    import codecs

    print("""
    Format yang tersedia:
    [1]  Base64      Encode / Decode
    [2]  URL         Encode / Decode
    [3]  Hex         Encode / Decode
    [4]  HTML Entity Encode / Decode
    [5]  ROT13       Encode / Decode (sama hasilnya)
    [6]  Binary      Encode / Decode
    """)

    fmt = input("[NMFS] Pilih format (1-6): ").strip()
    mode = input("[NMFS] Encode (e) atau Decode (d): ").strip().lower()
    text = input("[NMFS] Masukkan teks/data: ").strip()

    print("\n  +---------------------------------------------+")
    print("  |                  RESULT                     |")
    print("  +---------------------------------------------+")

    try:
        if fmt == '1':  # Base64
            if mode == 'e':
                result = base64.b64encode(text.encode()).decode()
                print(f"\n  [Base64 Encoded]\n  {result}")
            else:
                result = base64.b64decode(text.encode()).decode('utf-8', errors='replace')
                print(f"\n  [Base64 Decoded]\n  {result}")

        elif fmt == '2':  # URL
            if mode == 'e':
                result = urllib.parse.quote(text, safe='')
                print(f"\n  [URL Encoded]\n  {result}")
            else:
                result = urllib.parse.unquote(text)
                print(f"\n  [URL Decoded]\n  {result}")

        elif fmt == '3':  # Hex
            if mode == 'e':
                result = text.encode().hex()
                print(f"\n  [Hex Encoded]\n  {result}")
                print(f"\n  [Hex dengan spasi]\n  {' '.join(result[i:i+2] for i in range(0, len(result), 2))}")
            else:
                clean_hex = text.replace(' ', '').replace('0x', '').replace('\\x', '')
                result = bytes.fromhex(clean_hex).decode('utf-8', errors='replace')
                print(f"\n  [Hex Decoded]\n  {result}")

        elif fmt == '4':  # HTML Entity
            if mode == 'e':
                result = html.escape(text)
                print(f"\n  [HTML Encoded]\n  {result}")
            else:
                result = html.unescape(text)
                print(f"\n  [HTML Decoded]\n  {result}")

        elif fmt == '5':  # ROT13
            result = codecs.encode(text, 'rot_13')
            print(f"\n  [ROT13]\n  {result}")

        elif fmt == '6':  # Binary
            if mode == 'e':
                result = ' '.join(format(ord(c), '08b') for c in text)
                print(f"\n  [Binary Encoded]\n  {result}")
            else:
                bits = text.replace(' ', '')
                result = ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))
                print(f"\n  [Binary Decoded]\n  {result}")
        else:
            print("  [!] Format tidak valid")

    except Exception as e:
        print(f"\n  [!] Error: {e}")
        print("  [!] Pastikan input sesuai format yang dipilih.")

    print(f"\n  [*]  github: https://github.com/unknown-1110")
    input("\n[!] Tekan Enter untuk kembali...")


# ============================================================
# [OSINT 29] USERNAME LOOKUP
# Cek keberadaan username di berbagai platform publik
# ============================================================
def osint_username_lookup():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           OSINT USERNAME LOOKUP - NMFS mode")
    print("           Cek username di platform publik")
    print("="*55)

    username = input("\n[NMFS] Masukkan username yang mau dicek: ").strip()
    if not username:
        print("  [!] Username tidak boleh kosong")
        input("\n[!] Tekan Enter untuk kembali...")
        return

    platforms = {
        "GitHub"        : f"https://github.com/{username}",
        "GitLab"        : f"https://gitlab.com/{username}",
        "Twitter/X"     : f"https://twitter.com/{username}",
        "Instagram"     : f"https://instagram.com/{username}",
        "TikTok"        : f"https://tiktok.com/@{username}",
        "Reddit"        : f"https://reddit.com/user/{username}",
        "Pinterest"     : f"https://pinterest.com/{username}",
        "Tumblr"        : f"https://{username}.tumblr.com",
        "Medium"        : f"https://medium.com/@{username}",
        "Dev.to"        : f"https://dev.to/{username}",
        "Keybase"       : f"https://keybase.io/{username}",
        "Steam"         : f"https://steamcommunity.com/id/{username}",
        "Twitch"        : f"https://twitch.tv/{username}",
        "YouTube"       : f"https://youtube.com/@{username}",
        "Linktree"      : f"https://linktr.ee/{username}",
        "HackerOne"     : f"https://hackerone.com/{username}",
        "Bugcrowd"      : f"https://bugcrowd.com/{username}",
        "HackerNews"    : f"https://news.ycombinator.com/user?id={username}",
        "Product Hunt"  : f"https://producthunt.com/@{username}",
        "Replit"        : f"https://replit.com/@{username}",
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    print(f"\n[*] Mencari username '{username}' di {len(platforms)} platform...\n")
    print(f"  {'PLATFORM':<20} {'STATUS':<10}  URL")
    print("  " + "-"*70)

    found = []
    not_found = []

    for platform_name, url in platforms.items():
        try:
            r = requests.get(url, timeout=6, headers=headers, allow_redirects=True)
            # Anggap found jika 200, kecuali ada indikasi "not found" di body
            body_lower = r.text[:3000].lower()
            not_found_signals = [
                'page not found', 'user not found', '404', 'does not exist',
                'this account doesn', 'sorry, this page', 'no user found',
                'account suspended', 'that page doesn'
            ]
            is_not_found = any(sig in body_lower for sig in not_found_signals)

            if r.status_code == 200 and not is_not_found:
                print(f"  \033[92m{'[FOUND]':<10}\033[0m {platform_name:<20} {url}")
                found.append((platform_name, url))
            elif r.status_code in (301, 302) and 'login' not in r.headers.get('Location', ''):
                print(f"  \033[93m{'[MAYBE]':<10}\033[0m {platform_name:<20} {url}")
                found.append((platform_name, url))
            else:
                print(f"  \033[90m{'[---]':<10}\033[0m {platform_name:<20} {url}")
                not_found.append(platform_name)
        except requests.exceptions.Timeout:
            print(f"  \033[90m{'[TIMEOUT]':<10}\033[0m {platform_name:<20}")
        except Exception:
            print(f"  \033[90m{'[ERROR]':<10}\033[0m {platform_name:<20}")

    print(f"\n  {'='*55}")
    print(f"  [*] Total platform dicek  : {len(platforms)}")
    print(f"  [*] Kemungkinan ditemukan : {len(found)}")
    print(f"  [*] Tidak ditemukan       : {len(not_found)}")

    if found:
        print(f"\n  Akun yang ditemukan:")
        for pname, purl in found:
            print(f"    -> {pname:<20} : {purl}")

        save = input("\n[NMFS] Simpan hasil ke file? (y/n): ").lower()
        if save == 'y':
            fname = f"osint_username_{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(fname, 'w') as f:
                f.write(f"OSINT Username Lookup: {username}\n")
                f.write(f"Waktu: {datetime.now()}\n{'='*55}\n\n")
                for pname, purl in found:
                    f.write(f"[FOUND] {pname}: {purl}\n")
            print(f"  [OK] Disimpan ke: {fname}")

    print(f"\n  [*] github: https://github.com/unknown-1110")
    input("\n[!] Tekan Enter untuk kembali...")


#
def osint_email_breach():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           OSINT EMAIL BREACH CHECK - NMFS mode")
    print("           Cek email breach via Have I Been Pwned")
    print("="*55)

    print("""
  [i] Tool ini mengecek apakah email pernah ada di data breach
      yang sudah dipublikasikan secara publik oleh HIBP.
  [i] Data bersumber dari: haveibeenpwned.com (API publik)
    """)

    email = input("[NMFS] Masukkan email address: ").strip()
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        print("  [!] Format email tidak valid!")
        input("\n[!] Tekan Enter untuk kembali...")
        return

    import urllib.parse
    encoded_email = urllib.parse.quote(email)

    print(f"\n[*] Mengecek breach untuk: {email}\n")

    headers = {
        'User-Agent': 'NMFS-PentestTool/6.0',
        'hibp-api-key': '',  # Free endpoint tidak butuh API key untuk beberapa check
    }

   
    breached = False
    try:
        
        r = requests.get(
            f"https://haveibeenpwned.com/unifiedsearch/{encoded_email}",
            timeout=10,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Accept': 'application/json',
            },
            allow_redirects=True
        )

        if r.status_code == 200:
            try:
                data = r.json()
                breaches = data.get('Breaches', [])
                pastes = data.get('Pastes', [])
                breached = True

                print(f"  \033[91m[!!] EMAIL INI DITEMUKAN DI {len(breaches)} DATA BREACH!\033[0m\n")

                if breaches:
                    print(f"  {'NAMA BREACH':<30} {'TANGGAL':<15} {'AKUN BOCOR':>15}  DATA")
                    print("  " + "-"*75)
                    for b in breaches[:15]:
                        name = b.get('Name', 'N/A')[:28]
                        date = b.get('BreachDate', 'N/A')
                        count = f"{b.get('PwnCount', 0):,}"
                        data_classes = ', '.join(b.get('DataClasses', [])[:4])
                        print(f"  \033[93m{name:<30}\033[0m {date:<15} {count:>15}  {data_classes[:30]}")

                    if len(breaches) > 15:
                        print(f"\n  ... dan {len(breaches) - 15} breach lagi")

                if pastes:
                    print(f"\n  [!] Ditemukan di {len(pastes)} paste publik (pastebin, dll)")
                    for p in pastes[:5]:
                        src = p.get('Source', 'N/A')
                        title = p.get('Title', 'N/A') or 'N/A'
                        date = p.get('Date', 'N/A')
                        print(f"    -> [{src}] {title[:40]} ({date})")

            except Exception:
                print(f"  [*] Status: {r.status_code} - {r.text[:200]}")

        elif r.status_code == 404:
            print(f"  \033[92m[OK] Email tidak ditemukan di database breach publik HIBP.\033[0m")
            print(f"  [*] Bukan berarti 100% aman -- selalu gunakan password unik!")

        elif r.status_code == 429:
            print(f"  [!] Rate limited oleh HIBP. Coba lagi dalam beberapa detik.")
            print(f"  [*] Atau cek manual di: https://haveibeenpwned.com/account/{encoded_email}")

        elif r.status_code == 403:
            print(f"  [!] Endpoint ini membutuhkan API key HIBP.")
            print(f"  [*] Cek manual di: https://haveibeenpwned.com/account/{encoded_email}")
            print(f"  [*] API key gratis tersedia di: https://haveibeenpwned.com/API/Key")

        else:
            print(f"  [!] Response tidak terduga: HTTP {r.status_code}")
            print(f"  [*] Cek manual di: https://haveibeenpwned.com/account/{encoded_email}")

    except requests.exceptions.ConnectionError:
        print(f"  [!] Tidak bisa connect. Cek koneksi internet.")
    except Exception as e:
        print(f"  [!] Error: {e}")

    # Tambahan: cek password via HIBP Pwned Passwords (k-anonymity, aman)
    print(f"\n[*] Bonus: Cek apakah password kamu pernah bocor (tanpa kirim password asli)...")
    pw = input("[NMFS] Masukkan password untuk dicek (opsional, tekan Enter skip): ")
    if pw:
        pw_hash = hashlib.sha1(pw.encode()).hexdigest().upper()
        prefix = pw_hash[:5]
        suffix = pw_hash[5:]
        try:
            r2 = requests.get(
                f"https://api.pwnedpasswords.com/range/{prefix}",
                timeout=8,
                headers={'User-Agent': 'NMFS-PentestTool/6.0', 'Add-Padding': 'true'}
            )
            if r2.status_code == 200:
                hashes = {line.split(':')[0]: int(line.split(':')[1]) for line in r2.text.splitlines()}
                if suffix in hashes:
                    count = hashes[suffix]
                    print(f"  \033[91m[!!] Password ini pernah bocor {count:,} kali! JANGAN DIPAKAI!\033[0m")
                else:
                    print(f"  \033[92m[OK] Password tidak ditemukan di database breach (HIBP k-anonymity).\033[0m")
        except Exception as e:
            print(f"  [!] Error cek password: {e}")

    print(f"\n  [*] github: https://github.com/unknown-1110")
    input("\n[!] Tekan Enter untuk kembali...")



def osint_metadata_extractor():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           OSINT METADATA EXTRACTOR - NMFS mode")
    print("           Ekstrak semua metadata publik dari URL")
    print("="*55)

    url = input("\n[NMFS] Masukkan URL target (contoh: https://example.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url

    print(f"\n[*] Mengekstrak metadata dari {url}...\n")

    req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }

    try:
        r = requests.get(url, timeout=12, headers=req_headers, allow_redirects=True)
        body = r.text
        final_url = r.url
        resp_headers = r.headers
        parsed = urlparse(final_url)
        domain = parsed.netloc

        print("  " + "="*55)
        print("  [1] INFORMASI DASAR")
        print("  " + "="*55)
        print(f"  URL Asli      : {url}")
        print(f"  Final URL     : {final_url}")
        print(f"  HTTP Status   : {r.status_code}")
        print(f"  Ukuran Halaman: {len(body):,} bytes")
        print(f"  Content-Type  : {resp_headers.get('Content-Type', 'N/A')}")
        print(f"  Encoding      : {r.encoding or 'N/A'}")

        # Server info
        print(f"\n  [2] SERVER INFO")
        print("  " + "-"*45)
        server_fields = ['Server', 'X-Powered-By', 'X-Generator', 'Via',
                         'X-Cache', 'CF-Ray', 'X-Served-By', 'X-Backend-Server']
        for field in server_fields:
            val = resp_headers.get(field)
            if val:
                print(f"  {field:<25}: {val}")

        # IP & GeoIP
        print(f"\n  [3] IP & GEOLOCATION")
        print("  " + "-"*45)
        try:
            ip = socket.gethostbyname(domain)
            print(f"  IP Address    : {ip}")
            geo = requests.get(f"http://ip-api.com/json/{ip}?fields=country,regionName,city,isp,org,as", timeout=5).json()
            if geo.get('country'):
                print(f"  Negara        : {geo.get('country', 'N/A')}")
                print(f"  Region        : {geo.get('regionName', 'N/A')}")
                print(f"  Kota          : {geo.get('city', 'N/A')}")
                print(f"  ISP           : {geo.get('isp', 'N/A')}")
                print(f"  Org           : {geo.get('org', 'N/A')}")
                print(f"  AS Number     : {geo.get('as', 'N/A')}")
        except Exception as e:
            print(f"  [!] Gagal resolve IP: {e}")

        # SSL Info singkat
        try:
            if parsed.scheme == 'https':
                ctx = ssl.create_default_context()
                with socket.create_connection((domain, 443), timeout=5) as sock:
                    with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                        cert = ssock.getpeercert()
                        subject = dict(x[0] for x in cert.get('subject', []))
                        not_after = cert.get('notAfter', 'N/A')
                        print(f"\n  [4] SSL CERTIFICATE")
                        print("  " + "-"*45)
                        print(f"  CN            : {subject.get('commonName', 'N/A')}")
                        print(f"  Expires       : {not_after}")
                        try:
                            exp_dt = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
                            days_left = (exp_dt - datetime.utcnow()).days
                            print(f"  Sisa Hari     : {days_left} hari")
                        except:
                            pass
        except:
            pass

        # Meta tags
        print(f"\n  [5] META TAGS & SEO")
        print("  " + "-"*45)

        title = re.search(r'<title[^>]*>(.*?)</title>', body, re.IGNORECASE | re.DOTALL)
        if title:
            print(f"  Title         : {title.group(1).strip()[:100]}")

        meta_patterns = {
            'Description'   : r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)',
            'Keywords'      : r'<meta[^>]+name=["\']keywords["\'][^>]+content=["\']([^"\']+)',
            'Author'        : r'<meta[^>]+name=["\']author["\'][^>]+content=["\']([^"\']+)',
            'Robots'        : r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)',
            'Generator'     : r'<meta[^>]+name=["\']generator["\'][^>]+content=["\']([^"\']+)',
            'Viewport'      : r'<meta[^>]+name=["\']viewport["\'][^>]+content=["\']([^"\']+)',
            'Theme-Color'   : r'<meta[^>]+name=["\']theme-color["\'][^>]+content=["\']([^"\']+)',
            'OG:Title'      : r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)',
            'OG:Description': r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\']([^"\']+)',
            'OG:Image'      : r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)',
            'OG:Type'       : r'<meta[^>]+property=["\']og:type["\'][^>]+content=["\']([^"\']+)',
            'OG:Site Name'  : r'<meta[^>]+property=["\']og:site_name["\'][^>]+content=["\']([^"\']+)',
            'Twitter:Card'  : r'<meta[^>]+name=["\']twitter:card["\'][^>]+content=["\']([^"\']+)',
            'Twitter:Site'  : r'<meta[^>]+name=["\']twitter:site["\'][^>]+content=["\']([^"\']+)',
            'Twitter:Title' : r'<meta[^>]+name=["\']twitter:title["\'][^>]+content=["\']([^"\']+)',
            'Canonical'     : r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)',
        }

        for label, pattern in meta_patterns.items():
            m = re.search(pattern, body, re.IGNORECASE)
            if m:
                val = m.group(1).strip()[:120]
                print(f"  {label:<20}: {val}")

        # Links & Assets ringkasan
        print(f"\n  [6] RINGKASAN LINKS & ASSETS")
        print("  " + "-"*45)
        all_links = re.findall(r'href=["\']([^"\']+)["\']', body, re.IGNORECASE)
        all_scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', body, re.IGNORECASE)
        all_imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', body, re.IGNORECASE)
        emails_in_page = list(set(re.findall(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}', body)))
        phones_in_page = list(set(re.findall(r'[\+\(]?[0-9][0-9\s\-\(\)]{7,}[0-9]', body)))

        print(f"  Total href links  : {len(all_links)}")
        print(f"  Script src        : {len(all_scripts)}")
        print(f"  Images            : {len(all_imgs)}")
        print(f"  Email di halaman  : {len(emails_in_page)}")
        if emails_in_page:
            for em in emails_in_page[:5]:
                print(f"    -> {em}")
        if phones_in_page:
            print(f"  Nomor telp        : {len(phones_in_page)}")
            for ph in phones_in_page[:3]:
                print(f"    -> {ph.strip()}")

        # Social media links
        social_domains = ['facebook.com', 'twitter.com', 'instagram.com', 'linkedin.com',
                          'youtube.com', 'tiktok.com', 'github.com', 'telegram.me', 't.me']
        social_found = []
        for link in all_links:
            for sd in social_domains:
                if sd in link and link not in social_found:
                    social_found.append(link)
                    break

        if social_found:
            print(f"\n  [7] SOCIAL MEDIA LINKS DITEMUKAN")
            print("  " + "-"*45)
            for sl in social_found[:10]:
                print(f"    -> {sl[:90]}")

        # Simpan laporan
        save = input("\n[NMFS] Simpan laporan ke file? (y/n): ").lower()
        if save == 'y':
            fname = f"osint_metadata_{domain.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(f"OSINT Metadata Extractor - NMFS\n")
                f.write(f"URL     : {final_url}\n")
                f.write(f"Waktu   : {datetime.now()}\n")
                f.write(f"github  : https://github.com/unknown-1110\n")
                f.write("="*60 + "\n\n")
                f.write(f"Status  : {r.status_code}\n")
                f.write(f"Server  : {resp_headers.get('Server', 'N/A')}\n")
                f.write(f"Title   : {title.group(1).strip() if title else 'N/A'}\n\n")
                f.write("[META TAGS]\n")
                for label, pattern in meta_patterns.items():
                    m = re.search(pattern, body, re.IGNORECASE)
                    if m:
                        f.write(f"{label}: {m.group(1).strip()}\n")
                f.write(f"\n[EMAILS FOUND]\n")
                for em in emails_in_page:
                    f.write(f"{em}\n")
                f.write(f"\n[SOCIAL LINKS]\n")
                for sl in social_found:
                    f.write(f"{sl}\n")
            print(f"  [OK] Laporan disimpan ke: {fname}")

    except requests.exceptions.ConnectionError:
        print(f"  [!] Tidak bisa connect ke {url}")
    except requests.exceptions.Timeout:
        print(f"  [!] Timeout saat mengakses {url}")
    except Exception as e:
        print(f"  [!] Error: {e}")

    print(f"\n  [*] github: https://github.com/unknown-1110")
    input("\n[!] Tekan Enter untuk kembali...")


def main():
    while True:
        show_menu()
        choice = input("").strip()

        actions = {
            '1': port_scanner,
            '2': subdomain_finder,
            '3': ping_sweeper,
            '4': dns_lookup,
            '5': dir_brute,
            '6': network_info,
            '7': evil_corp_detector,
            '8': hash_cracker,
            '9': geoip_tracker,
            '10': email_validator,
            '11': password_generator,
            '12': link_extractor,
            '13': whois_lookup,
            '14': ssl_checker,
            '15': robots_sitemap_viewer,
            '16': header_analyzer,
            '17': banner_grabber,
            '18': http_response_timer,
            '19': open_redirect_checker,
            '20': reverse_ip_lookup,
            '21': url_param_fuzzer,
            '22': tech_stack_detector,
            '23': cookie_analyzer,
            '24': cors_checker,
            '25': cidr_calculator,
            '26': jwt_decoder,
            '27': http_method_tester,
            '28': encode_decode_tool,
            '29': osint_username_lookup,
            '30': osint_email_breach,
            '31': osint_metadata_extractor,
        }

        if choice in actions:
            actions[choice]()
        elif choice == '99':
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(NMFS_ASCII)
            print("  NO MERCY FOR SOCIETY.")
            print("  github: https://github.com/unknown-1110")
            print("  Stay sharp. Stay anonymous.\n")
            break
        else:
            print("\n  [!] Invalid choice, bruh!")
            input("  Tekan Enter untuk lanjut...")


if __name__ == "__main__":
    main()

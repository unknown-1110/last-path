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
from datetime import datetime
from urllib.parse import urlparse, urljoin
from html.parser import HTMLParser


def show_banner():
    banner = """
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX                                                                          XX
XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
XX   MMMMMy''                                                    ''yMMMMM   XX
XX   MMMy'                                                          'yMMM   XX
XX   Mh'                                                              'hM   XX
XX   -                                                                  -   XX
XX                                                                          XX
XX   ::                                                                ::   XX
XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +           XX
XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
XX                                oo      oo                                XX
XX           oM                 oo          oo                 Mo           XX
XX         oMMo                M              M                oMMo         XX
XX       +MMMM                 s              s                 MMMM+       XX
XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
XX   MMMMMMMM-                                                  -MMMMMMMM   XX
XX   MMMMMMMMM                                                  MMMMMMMMM   XX
XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
XX                                                                          XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `XER0'
    """
    print(banner)


def show_menu():
    menu = """
    +-------------------------------------------------------------+
    |          FSOCIETY PENTEST TOOL v4.0 [FULLY UPGRADED]        |
    |           "hello this tool only for pentesting."            |
    +-------------------------------------------------------------+
    |  [1]   Port Scanner                                         |
    |  [2]   Subdomain Finder                                     |
    |  [3]   Ping Sweeper                                         |
    |  [4]   DNS Lookup                                           |
    |  [5]   Directory Brute                                      |
    |  [6]   Network Info                                         |
    |  [7]   Evil Corp Detector                                   |
    |  [8]   Hash Cracker (MD5/SHA1/SHA256)                       |
    |  [9]   GeoIP Tracker                                        |
    |  [10]  Email Validator                                      |
    |  [11]  Password Generator (Secure)                          |
    |  [12]  Link Extractor from Website        [FIXED]           |
    |  [13]  WHOIS Lookup                                         |
    |  [14]  SSL/TLS Certificate Checker        [NEW]             |
    |  [15]  Robots.txt & Sitemap Viewer        [NEW]             |
    |  [16]  HTTP Header Analyzer               [NEW]             |
    |  [17]  Banner Grabber                     [NEW]             |
    |  [18]  HTTP Response Timer                [NEW]             |
    |  [19]  Open Redirect Checker              [NEW]             |
    |  [20]  Reverse IP Lookup                  [NEW]             |
    |  [21]  Exit                                                 |
    +-------------------------------------------------------------+

    [fsociety@kali:~]$
    """
    print(menu)


def port_scanner():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           PORT SCANNER - fsociety mode")
    print("="*55)

    target = input("\n[fsociety] Masukkan IP/Domain: ").strip()
    port_input = input("[fsociety] Port range atau list (contoh: 1-1000 atau 22,80,443): ").strip()

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

    print(f"\n  [*] Scan selesai. {len(open_ports)} port terbuka dari {len(ports_list)} port.")
    input("\n[!] Tekan Enter untuk kembali...")


def subdomain_finder():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           SUBDOMAIN FINDER - fsociety mode")
    print("="*55)

    domain = input("\n[fsociety] Masukkan domain (contoh: google.com): ")

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
    print("           PING SWEEPER - fsociety mode")
    print("="*55)

    network = input("\n[fsociety] Masukkan network (contoh: 192.168.1): ")
    start = int(input("[fsociety] Mulai dari (1-254): "))
    end = int(input("[fsociety] Sampai (1-254): "))

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
    print("           DNS LOOKUP - fsociety mode")
    print("="*55)

    target = input("\n[fsociety] Masukkan domain/IP: ")

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
    print("           DIRECTORY BRUTE - fsociety mode")
    print("="*55)

    url = input("\n[fsociety] Masukkan URL (contoh: http://example.com): ")

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
            elif response.status_code == 301 or response.status_code == 302:
                print(f"  [{response.status_code}]   {test_url}  (Redirect -> {response.headers.get('Location', '?')})")
        except:
            pass

    print(f"\n  [*] Selesai. {found_count} path ditemukan (200 OK).")
    input("\n[!] Tekan Enter untuk kembali...")


def network_info():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           NETWORK INFO - fsociety mode")
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
    |   AUTHOR:OTRISKO/LIQUORS777              |
    |                                          |
    +==========================================+
    """)

    target = input("\n[fsociety] Masukkan domain untuk diinvestigasi: ")

    evil_keywords = ['ecorp', 'e-corp', 'bank', 'evil', 'corp']

    print(f"\n[*] Investigating {target}...\n")

    is_evil = any(keyword in target.lower() for keyword in evil_keywords)

    if is_evil:
        print("  [WARNING] Target terkait dengan Evil Corp!")
        print("  fsociety: Execute operation!")
    else:
        print("  [OK] Target aman (untuk saat ini)")
        print("  fsociety: Stay vigilant, friend")

    input("\n[!] Tekan Enter untuk kembali...")


def hash_cracker():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           HASH CRACKER - fsociety mode")
    print("="*55)

    print("""
    Supported hash types:
    [1] MD5
    [2] SHA1
    [3] SHA256
    """)

    hash_type = input("\n[fsociety] Pilih tipe hash (1-3): ")
    target_hash = input("[fsociety] Masukkan hash yang mau di-crack: ").strip().lower()

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
    print("           GEOIP TRACKER - fsociety mode")
    print("="*55)

    target = input("\n[fsociety] Masukkan IP Address: ")

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
    print("           EMAIL VALIDATOR - fsociety mode")
    print("="*55)

    email = input("\n[fsociety] Masukkan email address: ")

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
    print("           PASSWORD GENERATOR - fsociety mode")
    print("="*55)

    length = int(input("\n[fsociety] Panjang password (default 16): ") or 16)
    use_upper = input("[fsociety] Pakai huruf besar? (y/n): ").lower() == 'y'
    use_lower = input("[fsociety] Pakai huruf kecil? (y/n): ").lower() == 'y'
    use_digits = input("[fsociety] Pakai angka? (y/n): ").lower() == 'y'
    use_symbols = input("[fsociety] Pakai simbol? (y/n): ").lower() == 'y'

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
            'a': 'href',
            'link': 'href',
            'script': 'src',
            'img': 'src',
            'iframe': 'src',
            'frame': 'src',
            'embed': 'src',
            'source': 'src',
            'form': 'action',
            'area': 'href',
            'base': 'href',
            'blockquote': 'cite',
            'q': 'cite',
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
        if (raw.startswith('#') or
                raw.lower().startswith('javascript:') or
                raw.lower().startswith('mailto:') or
                raw.lower().startswith('tel:') or
                raw == 'void(0)'):
            return
        resolved = urljoin(self.base_url, raw)
        if resolved.startswith('http://') or resolved.startswith('https://'):
            self.links.add(resolved)


def link_extractor():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           LINK EXTRACTOR v2 - fsociety mode")
    print("           [FIXED] Parse semua tag HTML + resolve")
    print("           relative URL dengan benar")
    print("="*55)

    url = input("\n[fsociety] Masukkan URL website: ").strip()
    if not url.startswith('http'):
        url = 'https://' + url

    show_all = input("[fsociety] Tampilkan semua link? (y/n, default n): ").lower() == 'y'
    filter_internal = input("[fsociety] Filter hanya link internal? (y/n, default n): ").lower() == 'y'

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36'
        }
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
        print(f"  External link   : {len(external)}")
        print()

        display_links = all_links if show_all else all_links[:50]

        for i, link in enumerate(display_links, 1):
            tag = "[INT]" if urlparse(link).netloc == base_domain else "[EXT]"
            display = link if len(link) <= 90 else link[:87] + "..."
            print(f"  {i:>4}. {tag} {display}")

        if not show_all and total > 50:
            print(f"\n  ... dan {total - 50} link lagi.")

        save = input("\n[fsociety] Simpan semua link ke file .txt? (y/n): ").lower()
        if save == 'y':
            filename = f"links_{base_domain.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Link Extractor Result\n")
                f.write(f"URL     : {final_url}\n")
                f.write(f"Total   : {total} links\n")
                f.write(f"Waktu   : {datetime.now()}\n")
                f.write("=" * 80 + "\n\n")
                for i, link in enumerate(all_links, 1):
                    f.write(f"{i}. {link}\n")
            print(f"  [OK] Disimpan ke: {filename}")

    except requests.exceptions.ConnectionError:
        print(f"  [!] Gagal connect ke {url}.")
    except requests.exceptions.Timeout:
        print(f"  [!] Timeout.")
    except Exception as e:
        print(f"  [!] Error: {e}")

    input("\n[!] Tekan Enter untuk kembali...")


def whois_lookup():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           WHOIS LOOKUP - fsociety mode")
    print("="*55)

    domain = input("\n[fsociety] Masukkan domain: ")

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
    print("           SSL/TLS CHECKER - fsociety mode")
    print("="*55)

    target = input("\n[fsociety] Masukkan domain (contoh: google.com): ").strip()
    target = target.replace('https://', '').replace('http://', '').split('/')[0]
    port = int(input("[fsociety] Port (default 443): ").strip() or 443)

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
        print(f"  [!] Certificate mungkin self-signed atau invalid!")
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
    print("           ROBOTS.TXT & SITEMAP VIEWER")
    print("           Cari hidden path + daftar URL")
    print("="*55)

    url = input("\n[fsociety] Masukkan base URL (contoh: https://example.com): ").strip()
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
            current_agent = "*"

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

        save = input("\n[fsociety] Simpan semua sitemap URL ke file? (y/n): ").lower()
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
    print("           HTTP HEADER ANALYZER - fsociety mode")
    print("           Analisis security headers website")
    print("="*55)

    url = input("\n[fsociety] Masukkan URL (contoh: https://example.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url

    print(f"\n[*] Fetching headers dari {url}...\n")

    try:
        req_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, timeout=10, headers=req_headers, allow_redirects=True)
        resp_headers = response.headers

        print(f"  Status Code  : {response.status_code}")
        print(f"  Final URL    : {response.url}")
        print()

        print("  All Response Headers:")
        print("  " + "-" * 46)
        for k, v in resp_headers.items():
            print(f"    {k:<35}: {v[:80]}")

        print("\n\n  Security Header Analysis:")
        print("  " + "-" * 46)

        security_headers = {
            'Strict-Transport-Security': {
                'desc': 'HSTS -- paksa HTTPS',
                'good': lambda v: 'max-age=' in v.lower()
            },
            'Content-Security-Policy': {
                'desc': 'CSP -- cegah XSS & injection',
                'good': lambda v: len(v) > 5
            },
            'X-Frame-Options': {
                'desc': 'Cegah Clickjacking',
                'good': lambda v: v.upper() in ('DENY', 'SAMEORIGIN')
            },
            'X-Content-Type-Options': {
                'desc': 'Cegah MIME sniffing',
                'good': lambda v: v.lower() == 'nosniff'
            },
            'Referrer-Policy': {
                'desc': 'Kontrol Referrer info',
                'good': lambda v: len(v) > 0
            },
            'Permissions-Policy': {
                'desc': 'Batasi browser API',
                'good': lambda v: len(v) > 0
            },
            'X-XSS-Protection': {
                'desc': 'XSS filter (legacy)',
                'good': lambda v: v.startswith('1')
            },
            'Cross-Origin-Opener-Policy': {
                'desc': 'Isolasi cross-origin',
                'good': lambda v: len(v) > 0
            },
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
            'Server': 'Web server & versi',
            'X-Powered-By': 'Backend technology',
            'X-AspNet-Version': 'ASP.NET version',
            'X-AspNetMvc-Version': 'ASP.NET MVC version',
            'X-Generator': 'CMS generator',
            'X-Drupal-Cache': 'Drupal CMS',
            'X-Pingback': 'WordPress XML-RPC',
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

        if percentage < 60:
            print("  [!] Website ini kekurangan banyak security headers!")
        elif percentage < 80:
            print("  [?] Lumayan, tapi masih bisa diimprove.")
        else:
            print("  [OK] Security headers cukup baik.")

    except requests.exceptions.ConnectionError:
        print(f"  [!] Gagal connect.")
    except Exception as e:
        print(f"  [!] Error: {e}")

    input("\n[!] Tekan Enter untuk kembali...")


def banner_grabber():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           BANNER GRABBER - fsociety mode")
    print("           Ambil banner service dari port terbuka")
    print("="*55)

    target = input("\n[fsociety] Masukkan IP/Domain: ").strip()
    port_input = input("[fsociety] Port yang mau digrab (pisah koma, contoh: 21,22,80,443,8080): ").strip()

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
                        f"{scheme}://{target}:{port}",
                        timeout=5,
                        headers={'User-Agent': 'Mozilla/5.0'},
                        verify=False
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
                        lines = banner.splitlines()
                        for line in lines[:6]:
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
    print("           HTTP RESPONSE TIMER - fsociety mode")
    print("           Ukur kecepatan respon website")
    print("="*55)

    url = input("\n[fsociety] Masukkan URL (contoh: https://example.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url

    try:
        count = int(input("[fsociety] Jumlah request (default 5): ").strip() or 5)
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

            bar_len = int(elapsed / 20)
            bar = "#" * min(bar_len, 50)
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
    print("           OPEN REDIRECT CHECKER - fsociety mode")
    print("           Deteksi kerentanan open redirect")
    print("="*55)

    url = input("\n[fsociety] Masukkan base URL (contoh: https://example.com): ").strip()
    if not url.startswith('http'):
        url = 'https://' + url
    url = url.rstrip('/')

    redirect_payloads = [
        '//evil.com',
        '///evil.com',
        'https://evil.com',
        'http://evil.com',
        '//evil.com/%2F..',
        '/\\evil.com',
        '/%09/evil.com',
        '/%2F%2Fevil.com',
        '//evil%E3%80%82com',
        'https:evil.com',
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

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    for param in common_params:
        for payload in redirect_payloads[:3]:
            test_url = f"{url}?{param}={payload}"
            tested += 1
            try:
                r = requests.get(test_url, timeout=5, headers=headers, allow_redirects=False)
                location = r.headers.get('Location', '')
                if location and ('evil.com' in location or location.startswith('//')):
                    vuln_entry = f"  [VULN] Param: {param} | Payload: {payload}"
                    print(vuln_entry)
                    print(f"         Status: {r.status_code} | Location: {location}")
                    vulnerable.append(test_url)
                else:
                    print(f"  [SAFE] ?{param}={payload[:30]}  -> {r.status_code}")
            except requests.exceptions.Timeout:
                pass
            except Exception:
                pass

    print(f"\n  [*] Tested  : {tested} kombinasi")
    print(f"  [*] Vulnerable: {len(vulnerable)}")

    if vulnerable:
        print(f"\n  VULNERABLE ENDPOINTS:")
        for v in vulnerable:
            print(f"    -> {v}")
    else:
        print("\n  [OK] Tidak ditemukan open redirect pada parameter yang diuji.")
        print("  [!] Bukan berarti 100% aman -- perlu manual testing lebih lanjut.")

    input("\n[!] Tekan Enter untuk kembali...")


def reverse_ip_lookup():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print("\n" + "="*55)
    print("           REVERSE IP LOOKUP - fsociety mode")
    print("           Cari domain lain di IP yang sama")
    print("="*55)

    target = input("\n[fsociety] Masukkan IP Address atau domain: ").strip()

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
    except socket.herror:
        print(f"  [!] Tidak ada PTR record untuk {target_ip}")
    except Exception as e:
        print(f"  [!] Error PTR: {e}")

    print(f"\n[*] Mencoba HackerTarget API (gratis)...")
    try:
        r = requests.get(
            f"https://api.hackertarget.com/reverseiplookup/?q={target_ip}",
            timeout=10,
            headers={'User-Agent': 'Mozilla/5.0'}
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

        save = input("\n[fsociety] Simpan ke file? (y/n): ").lower()
        if save == 'y':
            fname = f"reverseip_{target_ip.replace('.', '_')}.txt"
            with open(fname, 'w') as f:
                f.write(f"Reverse IP Lookup: {target_ip}\n")
                f.write(f"Waktu: {datetime.now()}\n")
                f.write("=" * 50 + "\n")
                for d in sorted(found_domains):
                    f.write(d + "\n")
            print(f"  [OK] Disimpan ke: {fname}")
    else:
        print(f"\n  [!] Tidak ada domain ditemukan untuk {target_ip}")

    input("\n[!] Tekan Enter untuk kembali...")


def main():
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        show_banner()
        show_menu()

        choice = input("[fsociety@kali:~]$ ").strip()

        if choice == '1':
            port_scanner()
        elif choice == '2':
            subdomain_finder()
        elif choice == '3':
            ping_sweeper()
        elif choice == '4':
            dns_lookup()
        elif choice == '5':
            dir_brute()
        elif choice == '6':
            network_info()
        elif choice == '7':
            evil_corp_detector()
        elif choice == '8':
            hash_cracker()
        elif choice == '9':
            geoip_tracker()
        elif choice == '10':
            email_validator()
        elif choice == '11':
            password_generator()
        elif choice == '12':
            link_extractor()
        elif choice == '13':
            whois_lookup()
        elif choice == '14':
            ssl_checker()
        elif choice == '15':
            robots_sitemap_viewer()
        elif choice == '16':
            header_analyzer()
        elif choice == '17':
            banner_grabber()
        elif choice == '18':
            http_response_timer()
        elif choice == '19':
            open_redirect_checker()
        elif choice == '20':
            reverse_ip_lookup()
        elif choice == '21':
            print("\n" + "=" * 50)
            print(" byeeee.")
            print("  byeee.")
            print("  Remember: FUCK SOCIETY.")
            print("=" * 50)
            print("""
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
                ⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀
                ⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
                ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
                ⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠁⠀
                ⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀
            """)
            break
        else:
            print("\n  [!] Invalid choice, friend!")
            input("  Tekan Enter untuk lanjut...")


if __name__ == "__main__":
    main()
import random
import requests
from fake_useragent import UserAgent
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import time
import os
from concurrent.futures import ThreadPoolExecutor

console = Console()

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def draw_ring_with_text():
    clear_console()
    ring = """
█████████████████
██                   ██
██                       ██
██                           ██
██                               ██

██████╗  ██╗ ███████╗  █████╗   █████╗   █████╗
██╔══██╗ ██║ ╚══███╔╝ ██╔══██╗ ██╔══██╗ ██╔══██╗
██║  ██║ ██║   ███╔╝  ╚██████║ ╚██████║ ╚██████║
██║  ██║ ██║  ███╔╝    ╚═══██║  ╚═══██║  ╚═══██║
██████╔╝ ██║ ███████╗  █████╔╝  █████╔╝  █████╔╝
╚═════╝  ╚═╝ ╚══════╝  ╚════╝   ╚════╝   ╚════╝

██                               ██
██                           ██
██                       ██
██                   ██
█████████████████
"""
    console.print(Text(ring, style="bold cyan"), justify="center")
    console.print("\n")
    console.print(Panel("!!! PLEASE SUBSCRIBE AND SUPPORT ME !!!", style="bold green"))
    os.system("xdg-open https://youtube.com/@dizflyze999")
    time.sleep(2)

def generate_random_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def generate_random_user_agent():
    ua = UserAgent()
    return ua.random

def generate_random_proxy():
    ip = generate_random_ip()
    port = random.randint(1024, 65535)
    return f"{ip}:{port}"

def is_proxy_active(proxy):
    url = "http://www.google.com"
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def is_ip_active(ip):
    url = "http://www.google.com"
    proxies = {
        "http": f"http://{ip}",
        "https": f"http://{ip}"
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def generate_files():
    console.print(Panel("[bold cyan]Generating 100,000 Random IPs, User-Agents, and Proxies...[/bold cyan]"))
    with ThreadPoolExecutor() as executor:
        ip_future = executor.submit(generate_and_save_ips)
        ua_future = executor.submit(generate_and_save_user_agents)
        proxy_future = executor.submit(generate_and_save_proxies)
        ip_future.result()
        ua_future.result()
        proxy_future.result()
    console.print("[bold green]100,000 IP, User-Agent, dan Proxy telah berhasil disimpan dalam file![/bold green]")

def generate_and_save_ips():
    random_ips = set()
    while len(random_ips) < 100000:
        ip = generate_random_ip()
        if is_ip_active(ip):
            random_ips.add(ip)
    with open('/sdcard/ip.txt', 'w') as ip_file:
        for ip in random_ips:
            ip_file.write(ip + '\n')
    console.print("[bold green]100,000 IP aktif telah disimpan di /sdcard/ip.txt[/bold green]")

def generate_and_save_user_agents():
    random_user_agents = set()
    while len(random_user_agents) < 100000:
        user_agent = generate_random_user_agent()
        random_user_agents.add(user_agent)
    with open('/sdcard/useragent.txt', 'w') as ua_file:
        for ua in random_user_agents:
            ua_file.write(ua + '\n')
    console.print("[bold green]100,000 User-Agent acak telah disimpan di /sdcard/useragent.txt[/bold green]")

def generate_and_save_proxies():
    random_proxies = set()
    while len(random_proxies) < 100000:
        proxy = generate_random_proxy()
        if is_proxy_active(proxy):
            random_proxies.add(proxy)
    with open('/sdcard/proxies.txt', 'w') as proxy_file:
        for proxy in random_proxies:
            proxy_file.write(proxy + '\n')
    console.print("[bold green]100,000 Proxy aktif telah disimpan di /sdcard/proxies.txt[/bold green]")

draw_ring_with_text()
generate_files()
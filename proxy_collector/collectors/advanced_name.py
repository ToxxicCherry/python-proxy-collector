import requests
import base64
from bs4 import BeautifulSoup
from proxy_collector.models import Proxy
from proxy_collector.collectors.req_data import headers

def parse_proxies(html: str) -> list[Proxy] | None:
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('tbody')
    try:
        strings = table.find_all('tr')
    except AttributeError:
        return None

    proxies = []
    for string in strings:
        ip = string.find('td', {'data-ip': True}).get('data-ip')
        ip = base64.b64decode(ip).decode()

        port = string.find('td', {'data-port': True}).get('data-port')
        port = base64.b64decode(port).decode()

        protocol = string.find_all('td')[3].find('a').text

        proxies.append(
            Proxy(
                ip=ip,
                port=port,
                protocol=protocol,
            )
        )
    return proxies

def collect_advanced_name() -> list[Proxy]:
    url = 'https://advanced.name/ru/freeproxy'
    result = []

    page = 1
    while True:
        response = requests.get(url=url, headers=headers, params={'page': page})
        proxies = parse_proxies(response.text)

        if not proxies:
            break

        result.extend(proxies)
        page += 1

    return result

collect_advanced_name()


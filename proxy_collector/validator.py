import requests

def is_alive(proxy_url: str, timeout: int = 5) -> bool:
    try:
        requests.get("https://httpbin.org/ip", proxies={"http": proxy_url, "https": proxy_url}, timeout=timeout)
        return True
    except Exception:
        return False

import requests
from stem import Signal
from stem.control import Controller

# Tor settings
TOR_CONTROL_PORT = 9051
TOR_PASSWORD = "your_tor_password"

# Function to renew Tor identity
def renew_tor_identity():
    with Controller.from_port(port=TOR_CONTROL_PORT) as controller:
        controller.authenticate(password=TOR_PASSWORD)
        controller.signal(Signal.NEWNYM)

# Make a request through Tor
def make_tor_request(url):
    session = requests.session()
    session.proxies = {
        'http': 'socks5://localhost:9050',
        'https': 'socks5://localhost:9050'
    }

    try:
        response = session.get(url)
        # Process the response as needed
        print(response.text)
    except requests.RequestException as e:
        print(f"Error: {e}")
    finally:
        session.close()

# Example usage
renew_tor_identity()
make_tor_request("https://indianexpress.com/section/india/")

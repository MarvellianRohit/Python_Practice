import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    # Try to fetch the data from the web
    response = requests.get(url)
    data = response.json()
    print(f"Live Bitcoin Price: ${data['bpi']['USD']['rate']}")

except requests.exceptions.ConnectionError:
    # If the network is down or blocked, run this instead of crashing!
    print("Error: Unable to connect to the internet. Please check your network connection or hotspot.")
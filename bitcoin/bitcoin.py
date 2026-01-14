#api: 368f8e4bc94c9202bc9cb51bccaaaba964e7078bc741847b3b2bf4484001f40d
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    sys.argv[1] = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=368f8e4bc94c9202bc9cb51bccaaaba964e7078bc741847b3b2bf4484001f40d")
except requests.RequestException:
    sys.exit("API request failed")
print(response.raise_for_status())
data = response.json()
price = float(data["data"]["priceUsd"])
total = sys.argv[1] * price
print(f"${total:,.4f}")

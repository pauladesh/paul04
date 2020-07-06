import requests

def main():
    res = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"]["EUR"]
    print(f"1 USD is equal to {rate} EUR")

if __name__ == "__main__":
    main()

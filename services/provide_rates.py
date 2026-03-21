import requests


class RatesProvider:
    def get_rates(self):
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()

        return data["rates"]

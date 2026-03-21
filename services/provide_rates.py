import requests
import time


class RatesProvider:
    def __init__(self):
        self._rates = None
        self._last_update = 0

    def get_rates(self, attempts=3):
        if self._rates and time.time() - self._last_update < 600:
            return self._rates

        for attempt in range(attempts):
            try:
                response = requests.get(
                    "https://api.exchangerate-api.com/v4/latest/USD", timeout=5
                )
                response.raise_for_status()
                data = response.json()

                self._rates = data["rates"]
                self._last_update = time.time()

                return self._rates

            except requests.RequestException:
                print(f"ERROR: Failed to fetch exchange rates, {attempt + 1} failed.")

        print("ERROR: Failed to fetch exchange rates.")
        return None

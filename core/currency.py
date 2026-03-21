class Currency:
    def __init__(self, name: str, oneusd_in_currency: float):
        self.name = name
        self.oneusd_in_currency = oneusd_in_currency

    def __repr__(self):
        return f"Currency '{self.name}', 1 dollar equals to {self.oneusd_in_currency} {self.name}"

    def get_oneusd_in_currency(self):
        return self.oneusd_in_currency

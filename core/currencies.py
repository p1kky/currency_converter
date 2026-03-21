from services.provide_rates import RatesProvider
from core.currency import Currency

provider = RatesProvider()
rates = provider.get_rates()

usd = Currency("usd", rates["USD"])
eur = Currency("eur", rates["EUR"])
rub = Currency("rub", rates["RUB"])
byn = Currency("byn", rates["BYN"])
kzt = Currency("kzt", rates["KZT"])

currencies_dict = {"usd": usd, "eur": eur, "rub": rub, "byn": byn, "kzt": kzt}

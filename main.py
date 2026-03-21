from currencies import currencies_dict


def get_converting_currencies():
    while True:
        print("\n" + "-*- " * 4 + "Currency converter" + " -*-" * 4)

        convert_from_to = (
            input("Enter currency to convert from and to (e.g. 'USD BYN')\n - ")
            .lower()
            .strip()
            .split()
        )

        if len(convert_from_to) != 2:
            print("Incorrect parameters")
            continue

        if any(i not in ("usd", "eur", "rub", "byn", "tg") for i in convert_from_to):
            print("Incorrect parameters")
            continue

        return convert_from_to


def get_amount(user_currency_from):
    while True:
        try:
            print("\n" + "-*- " * 4 + "Currency converter" + " -*-" * 4)

            amount = float(input(f"Enter amount of {user_currency_from.upper()}\n - "))

            return amount
        except (ValueError, IndexError):
            continue


def convert(amount, cur_from_to):
    cur_from = cur_from_to[0]
    cur_to = cur_from_to[1]

    cur_from_object = currencies_dict[cur_from]
    cur_to_object = currencies_dict[cur_to]

    usd_amount = amount / cur_from_object.get_oneusd_in_currency()

    result = usd_amount * cur_to_object.get_oneusd_in_currency()

    return round(result, 2)


def main():
    print("\n" + "-*- " * 4 + "Currency converter" + " -*-" * 4)
    print("Currently available currencies:\n - USD\n - EUR\n - RUB\n - BYN\n - TG ")

    currencies_from_to = get_converting_currencies()
    amount = get_amount(currencies_from_to[0])

    result = convert(amount, currencies_from_to)

    print("\n" + "-*- " * 4 + "Currency converter" + " -*-" * 4)
    print(f"Convert successful! Result = {result.upper()} {currencies_from_to[1]}")


if __name__ == "__main__":
    main()

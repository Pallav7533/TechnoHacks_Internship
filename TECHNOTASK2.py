import requests

def get_exchange_rates(base_currency):
    url = f"https://openexchangerates.org/api/latest.json?app_id=YOUR_APP_ID&base={base_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['rates']
    else:
        print("Failed to fetch exchange rates.")
        return None

def convert_currency(amount, from_currency, to_currency):
    exchange_rates = get_exchange_rates(from_currency)
    
    if exchange_rates:
        if to_currency in exchange_rates:
            converted_amount = amount * exchange_rates[to_currency]
            return converted_amount
        else:
            print(f"Exchange rate for {to_currency} not found.")
    return None

def currency_converter():
    print("Currency Converter")
    from_currency = input("Enter the source currency code (e.g., USD): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))
    
    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

currency_converter()

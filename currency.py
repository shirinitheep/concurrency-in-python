def usd_to_eur_converter(amount_usd):
    # Assuming an exchange rate of 1 USD to 0.85 EUR
    exchange_rate = 0.85
    amount_eur = amount_usd * exchange_rate
    return amount_eur

# Example usage:
usd_amount = float(input("Enter the amount in USD: "))
eur_result = usd_to_eur_converter(usd_amount)
print(f"{usd_amount} USD is equal to {eur_result:.2f} EUR.")

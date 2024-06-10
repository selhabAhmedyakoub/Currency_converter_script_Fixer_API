import requests

# List of available currencies
# List of the 170 available currencies 
available_currencies = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", 
                        "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNY", "COP", 
                        "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", 
                        "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", 
                        "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", 
                        "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", 
                        "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", 
                        "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "STD", "SVC", 
                        "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", 
                        "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMK", "ZMW", "ZWL"]

# API key
api_key = "nhvAEFQVCOQsdkqpkFd4dV6IL7e8j2Cs"

# Get initial currency from user
while True:
    init_currency = input("Enter the currency you have (options are: " + ', '.join(available_currencies) + "): ")
    if init_currency not in available_currencies:
        print("Invalid currency. Please choose from the available options.")
    else:
        break

# Get target currency from user
while True:
    target_currency = input("Enter the currency you want to change your money into (options are: " + ', '.join(available_currencies) + "): ")
    if target_currency not in available_currencies:
        print("Invalid currency. Please choose from the available options.")
    else:
        break

# Get amount from user
while True:
    try:
        amount = float(input("Tell me how much you have: "))
        if amount <= 0:
            print("The amount should be greater than 0.")
        else:
            break
    except ValueError:
        print("The user should enter a numeric value.")

# Construct the API request
url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"
headers = {"apikey": api_key}

# Send the request
response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    print("The request was successful.")
    print(response.text)
else:
    print("The request was unsuccessful.")
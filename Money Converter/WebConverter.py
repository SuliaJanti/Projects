from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'fca_live_Q45OK1K7ofgc2wfOcqFTTKBMYDUNuGF0iJkxThK9'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES =["USD", "EUR", "BRL","JPY"]

@app.route ('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    base = request.form['base'].upper()
    amount = float(request.form['amount'])
    data = convert_currency(base)
    converted_data={}
    for currency, rate in data.items():
        converted_data[currency] = round(amount*rate, 2)
    return render_template('result.html', base=base, amount=amount, data=converted_data)

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data ["data"]
    except Exception:
        print ("Invalid currency")
        return {}
    
if __name__ == '__main__':
    app.run(debug=True)
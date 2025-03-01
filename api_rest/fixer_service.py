import requests

FIXER_API_KEY = "sua_chave_de_api"
FIXER_URL = "http://data.fixer.io/api/latest"

def get_exchange_rates():
    params = {
        "access_key": FIXER_API_KEY
    }
    response = requests.get(FIXER_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Não foi possível obter taxas de câmbio"}

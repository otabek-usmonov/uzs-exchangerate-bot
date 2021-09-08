
import requests
from currency_codes import CURRENCIES


API_KEY = '82e68121413a404dc85fd537'


def get_rate(currency):
	url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

	try:
		response = requests.get(url)
		rate = response.json()['conversion_rate']
	except:
		rate = False

	return rate



def get_currency_codes():
	code_list = ""
	for curr_code in CURRENCIES:
		code_list += f"/{curr_code[0]} - {curr_code[1]}\n"

	return code_list



def is_currency_code(currency):
	return currency in dict((x, y) for x, y in CURRENCIES)


def get_ordered_rate_list(sort_in_desc=False):
	rate_dict = {}

	for code in CURRENCIES:
		rate = get_rate(code[0])
		if not (rate is False):
			rate_dict[code[0]] = rate

	sorted_tuple = sorted(rate_dict, key=rate_dict.get, reverse=sort_in_desc)

	rate_list = ""
	for code in sorted_tuple:
		rate_list += f"1 {code} = {rate_dict[code]} UZS\n"

	return rate_list




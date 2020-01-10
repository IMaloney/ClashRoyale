import requests
import json


def get_key(file):
	return open(file).read().strip('\n')

# diff_file --> different api key
def make_request(endpoint, diff_file=False):
	key = 0
	if diff_file:
		key = get_key(diff_file)
	key = get_key("./api_key.txt")
	header = {"Authorization": "Bearer %s" % key}
	base_url = "https://api.clashroyale.com/v1"
	return requests.get(base_url + endpoint, headers=header)

def get_clan_info():
	pass 

def get_clan_members():
	pass

def get_clan_warlog():
	pass

def get_clan_currentwar():
	pass


def get_player_info():
	pass

def get_player_upcomingsheets():
	pass

def get_player_battlelog():
	pass

def get_tournament_info():
	pass

def get_cards():
	info = json.loads(make_request("/cards").text)
	return info
# if __name__ == "__main__":
# 	print("hi")
print(get_cards())
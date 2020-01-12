import requests
import json

# Y0VGUUPLP --> my player id

def get_key(file):
	return open(file).read().strip('\n')

def make_request(endpoint, file):
	key = get_key(file)
	header = {"Authorization": "Bearer %s" % key}
	base_url = "https://api.clashroyale.com/v1"
	return requests.get(base_url + endpoint, headers=header)

def get_clan_info(clan_tag, file="./api_key.txt"):
	endpoint = "/clan/%23" + clan_tag
	info = json.loads(make_request(endpoint).text)
	return info

def get_clan_members(clan_tag, file="./api_key.txt"):
	endpoint = "/clan/%23" + clan_tag + "/members"
	info = json.loads(make_request(endpoint).text)
	return info

def get_clan_warlog(clan_tag, file="./api_key.txt"):
	endpoint = "/clan/%23" + clan_tag + "/warlog"
	info = json.loads(make_request(endpoint).text)
	return info

def get_clan_currentwar(clan_tag, file="./api_key.txt"):
	endpoint = "/clan/%23" + clan_tag + "/currentwar"
	info = json.loads(make_request(endpoint).text)
	return info

'''
Returns player info in json format
'''
def get_player_info(player_tag, file="./api_key.txt"):
	endpoint = "/players/%23" + player_tag
	# may do a little more with info
	info = json.loads(make_request(endpoint, file).text)
	return info

def get_player_upcomingchests(player_tag, file="./api_key.txt"):
	endpoint = "/players/%23" + player_tag + "/upcomingchests"
	info = json.loads(make_request(endpoint).text)
	return info

def get_player_battlelog(player_tag, file="./api_key.txt"):
	endpoint = "/players/%23" + player_tag + "/battlelog"
	info = json.loads(make_request(endpoint).text)
	return info

def get_tournament_info(tournament_tag, file="./api_key.txt"):
	endpoint = "/tournaments/%23" + tournament_tag
	info = json.loads(make_request(endpoint).text)
	return info

'''
Gets list of locations --> take out of json
'''
def get_locations():
	endpoint = "/locations"
	info = json.loads(make_request(endpoint, file="./api_key.txt").text)
	return info

# 57000000
def get_locations():
	endpoint = "/locations"
	info = json.loads(make_request(endpoint, file="./api_key.txt").text)
	return info

def get_cards(file="./api_key.txt"):
	info = json.loads(make_request("/cards", file).text)
	return info


# if __name__ == "__main__":
# 	print("hi")
# print(get_player_info("Y0VGUUPLP"))

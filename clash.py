import requests
import json
from errors import *

# Y0VGUUPLP --> my player id
# TODO: figure out if what's below is possible
# what if the repl connected to a server so you would never need an api key

def get_key(file):
	return open(file).read().strip('\n')

# still need to handle bad requests
def make_request(endpoint, file):
	# will ultimately have to pass in api key no matter what
	if not file:
		file = "./api_key.txt"
	key = get_key(file)
	header = {"Authorization": "Bearer %s" % key}
	base_url = "https://api.clashroyale.com/v1"
	return requests.get(base_url + endpoint, headers=header)

def get_clan_info(clan_tag, file):
	endpoint = "/clans/%23" + clan_tag
	info = json.loads(make_request(endpoint, file).text)
	return info

def get_clan_members(clan_tag, file):
	endpoint = "/clans/%23" + clan_tag + "/members"
	info = json.loads(make_request(endpoint, file).text)
	return info

def get_clan_warlog(clan_tag, file):
	endpoint = "/clans/%23" + clan_tag + "/warlog"
	info = json.loads(make_request(endpoint, file).text)
	return info

def get_clan_currentwar(clan_tag, file):
	endpoint = "/clans/%23" + clan_tag + "/currentwar"
	info = json.loads(make_request(endpoint, file).text)
	return info

'''
Returns player info in json format
'''
def get_player_info(player_tag, file):
	endpoint = "/players/%23" + player_tag
	# may do a little more with info
	info = json.loads(make_request(endpoint, file).text)
	print(info)
	return info

def get_player_upcomingchests(player_tag, file):
	endpoint = "/players/%23" + player_tag + "/upcomingchests"
	info = json.loads(make_request(endpoint, file).text)
	return info

def get_player_battlelog(player_tag, file):
	endpoint = "/players/%23" + player_tag + "/battlelog"
	info = json.loads(make_request(endpoint, file).text)
	return info

def get_tournament_info(tournament_tag, file):
	endpoint = "/tournaments/%23" + tournament_tag
	info = json.loads(make_request(endpoint, file).text)
	return info

'''
Gets list of locations --> take out of json
'''
def get_locations(file):
	endpoint = "/locations"
	info = json.loads(make_request(endpoint, file).text)
	return info

# 57000000
# def get_locations(file):
# 	endpoint = "/locations"
# 	info = json.loads(make_request(endpoint, file).text)
# 	return info

def get_cards(file):
	info = json.loads(make_request("/cards", file).text)
	return info


def format_cards(cards):
	card_dict = dict()
	for card in cards:
		level = card["level"]
		if card["maxLevel"] == 5:
			level += 8
		elif card["maxLevel"] == 8:
			level += 5
		elif card["maxLevel"] == 11:
			level += 2
		# id may be unnecessary
		card_dict[card["name"]] = (level, card["count"], card["id"])
	return card_dict


# print(get_cards("./api_key.txt"))

# print(get_player_info("Y0VGUUPLP"))
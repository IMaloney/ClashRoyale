import requests
import json
from errors import *

# Y0VGUUPLP --> my player id

def handle_error(error: str) -> None:
	if error == "accessDenied":
		raise AccessDeniedError()
	if error == "notFound":
		raise ResourceError()

def get_key(file: str) -> str:
	return open(file).read().strip('\n')

# still need to handle bad requests
def make_request(endpoint, file):
	if not file:
		file = "./keys/home_key.txt"
	key = get_key(file)
	header = {"Authorization": "Bearer %s" % key}
	base_url = "https://api.clashroyale.com/v1"
	return requests.get(base_url + endpoint, headers=header)

def get_clan_info(clan_tag, file):
	endpoint = "/clans/%23" + clan_tag
	info = json.loads(make_request(endpoint, file).text)
	if "reason" in info:
		handle_error(info['reason'])
		print(info['reason'])
	return info

def get_clan_members(clan_tag, file):
	endpoint = "/clans/%23" + clan_tag + "/members"
	info = json.loads(make_request(endpoint, file).text)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_clan_warlog(clan_tag, file):
	endpoint = "/clans/%23" + clan_tag + "/warlog"
	info = json.loads(make_request(endpoint, file).text)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_clan_currentwar(clan_tag: str, file: str):
	endpoint = "/clans/%23" + clan_tag + "/currentwar"
	info = json.loads(make_request(endpoint, file).text)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_player_info(player_tag: str, file: str, server: bool):
	endpoint = "/players/%23" + player_tag
	# may do a little more with info
	if not server:
		info = json.loads(make_request(endpoint, file).text)
	else:
		# make request to our server
		pass
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_player_upcomingchests(player_tag, file):
	endpoint = "/players/%23" + player_tag + "/upcomingchests"
	info = json.loads(make_request(endpoint, file).text)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_player_battlelog(player_tag, file):
	endpoint = "/players/%23" + player_tag + "/battlelog"
	info = json.loads(make_request(endpoint, file).text)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_tournament_info(tournament_tag, file):
	endpoint = "/tournaments/%23" + tournament_tag
	info = json.loads(make_request(endpoint, file).text)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_locations(file):
	endpoint = "/locations"
	info = json.loads(make_request(endpoint, file).text)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_cards(file):
	info = json.loads(make_request("/cards", file).text)
	if "reason" in info:
		handle_error(info['reason'])
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
		card_dict[card["name"]] = (level, card["count"], card["id"])
	return card_dict
import requests
import json
from errors import handle_error

# Y0VGUUPLP --> my player id

def get_key(api_key: str) -> str:
	return open(api_key).read().strip('\n')

def make_request(endpoint: str, api_key: str):
	if api_key:
		key = get_key(api_key)
		header = {"Authorization": "Bearer %s" % key}
		base_url = "https://api.clashroyale.com/v1"
		info = requests.get(base_url + endpoint, headers=header)
	else:
		info = requests.post("http://clash-env.eba-3wy7k7uc.us-east-2.elasticbeanstalk.com/", data={"endpoint": endpoint})
	j = json.loads(info.text)
	return j

def get_clan_info(clan_tag: str, api_key: str):
	endpoint = "/clans/%23" + clan_tag
	info = make_request(endpoint, api_key)
	if "reason" in info:
		handle_error(info['reason'])
		print(info['reason'])
	return info

def get_clan_members(clan_tag, api_key):
	endpoint = "/clans/%23" + clan_tag + "/members"
	info = make_request(endpoint, api_key)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_clan_warlog(clan_tag, api_key):
	endpoint = "/clans/%23" + clan_tag + "/warlog"
	info = make_request(endpoint, api_key)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_clan_currentwar(clan_tag: str, api_key: str):
	endpoint = "/clans/%23" + clan_tag + "/currentwar"
	info = make_request(endpoint, api_key)
	if "reason" in info:
		handle_error(info['reason'])
	if "err" in info:
		pass
	return info

def get_player_info(player_tag: str, api_key: str):
	endpoint = "/players/%23" + player_tag
	# may do a little more with info
	info = make_request(endpoint, api_key)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_player_upcomingchests(player_tag: str, api_key: str):
	endpoint = "/players/%23" + player_tag + "/upcomingchests"
	info = make_request(endpoint, api_key)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_player_battlelog(player_tag, api_key):
	endpoint = "/players/%23" + player_tag + "/battlelog"
	info = make_request(endpoint, api_key)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_tournament_info(tournament_tag, api_key):
	endpoint = "/tournaments/%23" + tournament_tag
	info = make_request(endpoint, api_key)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_locations(api_key):
	endpoint = "/locations"
	info = make_request(endpoint, api_key)
	if "reason" in info:
		handle_error(info['reason'])
	return info

def get_cards(api_key):
	info = make_request("/cards", api_key)
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
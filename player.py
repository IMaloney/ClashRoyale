import clash

def format_chests(chests):
	chests = chests["items"]
	chest_dict = dict()
	for chest in chests:
		if chest["name"] not in chest_dict:
			chest_dict[chest["name"]] = chest["index"] 
		# chest_list.append((chest["index"], chest["name"]))
	return chest_dict


class Player:
	def __init__(self, player_tag, file):
		info = clash.get_player_info(player_tag, file)
		self.name = info["name"]
		self.level = info["expLevel"]
		self.current_trophies = info["trophies"]
		self.wins = info["wins"]
		self.losses = info["losses"]
		self.three_crowns = info["threeCrownWins"]
		self.upcoming_chests = format_chests(clash.get_player_upcomingchests(player_tag, file))
		# includes 2v2 battles
		self.total_battles = info["battleCount"]
		self.current_deck = clash.format_cards(info["currentDeck"])
		# clan name, clan tag excluding #
		self.clan = (info["clan"]["name"], info["clan"]["tag"][1:])

	def get_win_ratio(self) -> int:
		return (int)((self.wins / self.losses) * 100)

	def get_curr_deck(self):
		print(self.current_deck)

	def print_upcoming_chests(self):
		print("%s has the following chests coming up:" % self.name)
		for chest, idx in self.upcoming_chests.items():
			adj = "A"
			if chest[0] == "E":
				adj = "An"
			if not idx:
				print("\t%s %s next round." % (adj, chest))
			else:
				num = idx + 1
				print("\t%s %s on round %d." % (adj, chest, num))


class Clan:
	def __init__(self, clan_tag, file):
		info = clash.get_clan_info(clan_tag, file)



player = Player("Y0VGUUPLP", "./api_key.txt")
# player.get_curr_deck()
# print(player.upcoming_chests)
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
		# some names may not be in ascii (i.e. chinese characters)
		# self.name = unicode(info["name"], "utf-8")
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
		self.file = file
		self.info = clash.get_clan_info(clan_tag, file)
		# still doesnt work for chinese characters
		self.name = self.info["name"]
		self.trophies = self.info["clanWarTrophies"]
		self.donations_per_week = self.info["donationsPerWeek"]
		self.clan_score = self.info["clanScore"]
		self.players_list = list()
		self.players_dict = dict()
		self.update_player_dict()

	def update_player_dict(self, info):
		for member in info["memberList"]:
			# currently stored by name (may switch to tag name)
			# adding both tag and name to list
			self.players_list.append((member["name"], member["tag"]))
			# keep a tuple of the player role and the player class
			self.players_dict["name"] = (member["name"]["role"], Player(member["tag"], self.file))
			# self.players_dict["name"] = dict()
			# self.players_dict["name"]["tag"] = member["name"]["tag"]
			# self.players_dict["name"]["role"] = member["name"]["role"]
			# self.players_dict[]




# clash.get_clan_info("G29Y22", "./brown_key.txt")
player = Player("8U0QGQGQ", "./brown_key.txt")
print(player.name)
# print(player.name)
# clan = Clan("9LUP8QRR", "./cit_key.txt")
# print(clan.info)
# player.get_curr_deck()
# print(player.upcoming_chests)
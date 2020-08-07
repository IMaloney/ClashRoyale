from typing import List
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
	def __init__(self, player_tag: str, api_key: str):
		info = clash.get_player_info(player_tag, api_key)
		# some names may not be in ascii (i.e. chinese characters)
		# self.name = unicode(info["name"], "utf-8")
		self.name = info["name"]
		self.level = info["expLevel"]
		self.current_trophies = info["trophies"]
		self.wins = info["wins"]
		self.losses = info["losses"]
		self.three_crowns = info["threeCrownWins"]
		self.upcoming_chests = format_chests(clash.get_player_upcomingchests(player_tag, api_key))
		# includes 2v2 battles
		self.total_battles = info["battleCount"]
		self.current_deck = clash.format_cards(info["currentDeck"])
		# clan name, clan tag excluding #
		self.clan = (info["clan"]["name"], info["clan"]["tag"][1:])
		self.arena = info["arena"]["name"]
		self.donations = (info["donations"], info["donationsReceived"])
		self.war_day = info["warDayWins"]
		self.role = info["role"] if info["role"] else None

	def get_win_ratio(self) -> int:
		return (int)((self.wins / self.losses) * 100)

	def print_current_deck(self, add_name=False):
		n = ""
		tab = "\t"
		if add_name:
			n = "f{self.name}'s "
			tab = ""
		print(f"{tab}{n}current deck:")
		for card, att in self.current_deck.items():
			ct = "max" if att[0] == 13 else att[1]
			print(f"{tab}\tCard: {card} Level: {att[0]} Count: {ct}")

	def print_upcoming_chests(self, add_name=False):
		n = ""
		tab = "\t"	
		if add_name:
			n = f"{self.name} "
			tab = ""
		print(f"{tab}{n}upcoming chests:")
		for chest, idx in self.upcoming_chests.items():
			adj = "A"
			if chest[0] == "E":
				adj = "An"
			if not idx:
				print(f"\t{tab}{adj} {chest} next round.")
			else:
				num = idx + 1
				print(f"\t{tab}{adj} {chest} on round {num}.")

leadership = {"leader": 3, "coleader": 2, "elder": 1, "member": 0}

class Clan:
	def __init__(self, clan_tag:str, api_key:str):
		self.api_key = api_key
		self.info = clash.get_clan_info(clan_tag, api_key)
		# still doesnt work for chinese characters
		self.name = self.info["name"]
		self.trophies = self.info["clanWarTrophies"]
		self.donations_per_week = self.info["donationsPerWeek"]
		self.clan_score = self.info["clanScore"]
		self.leader = None
		self.elders = list()
		self.coleaders = list()
		self.members = list()
		self.players_list, self.players_dict = self.update_player_dict()
		self.num_members = self.info["members"]

	def update_player_dict(self):
		l = list()
		d = dict()
		for member in self.info["memberList"]:
			# adding both tag and name to list
			rank = member["role"]
			# will probably be getting rid of this
			l.append((rank, member["tag"]))
			p = Player(member["tag"], self.api_key)
			if rank == "leader":
				self.leader = p
			elif rank == "coleader":
				self.coleaders.append(p)
			elif rank == "elder":
				self.elders.append(p)
			else:
				self.members.append(p)
			d[member["tag"]] = (member["role"], p)
		return l, d

	def print_members(self, amount: int = -1, add_name: bool = False, members_first: bool = False) -> None:
		amount = self.num_members if amount == -1 else amount
		amount = self.num_members if amount > self.num_members else amount
		l.sort(key=(lambda x: leadership[x[0]]), reverse=members_first)
		tab = "\t"
		if add_name:
			tab = ""
		print(f"{tab}members:")
		rn = range(amount)
		for i in rn:
			player = self.players_dict[self.players_list[i]][1]
			rank = self.players_dict[self.players_list[i]][0]
			print(f"{tab}\t{player.name} | Rank: {rank} | Level: {player.level}")

	def get_donors(self, reverse: bool = False, received: bool = False, amount: int = -1, add_name: bool = False) -> None:
		l.sort(key=(lambda x: x[0].donations[received]), reverse=members_first)
		amount = self.num_members if amount == -1 else amount
		amount = self.num_members if amount > self.num_members else amount
		rn = range(amount)
		tab = "\t"
		action = "Received: " if received else "Given: " 
		if add_name:
			tab = ""
		for i in rn:
			print(f"{tab}{l[i].name} {action}: {l[i].donations[received]}")

	def get_elders(add_name: bool = False) -> None:
		tab = "\t"
		if add_name:
			tab = ""
		if self.elders:
			print(f"{tab}elders:")
			for elder in self.elders:
				print(f"{tab}\t{elder.name}")
		else:
			print(f"{tab}No elders in the clan.")


	def get_coleaders(add_name: bool = False) -> None:
		tab = "\t"
		if add_name:
			tab = ""
		if self.coleaders:
			print(f"{tab}coleaders:")
			for coleader in self.coleaders:
				print(f"{tab}\t{coleader.name}")
		else:
			print(f"{tab}No coleaders in the clan.")

	def get_members(add_name: bool = False) -> None:
		tab = "\t"
		if add_name:
			tab = ""
		if self.members:
			print(f"{tab}members:")
			for member in self.members:
				print(f"{tab}\t{member.name}")
		else:
			print(f"{tab}No members in the clan.")

	def get_leader(self) -> str:
		return self.leader
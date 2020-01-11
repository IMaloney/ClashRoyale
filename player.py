import clash

class Player:
	def __init__(self, player_tag):
		info = clash.get_player_info(player_tag)
		self.name = info["name"]
		self.level = info["expLevel"]
		self.current_trophies = info["trophies"]
		self.wins = info["wins"]
		self.losses = info["losses"]
		self.three_crowns = info["threeCrownWins"]
		# includes 2v2 battles
		self.total_battles = info["battleCount"]
		self.curent_deck = info["currentDeck"]
		# clan name, clan tag excluding #
		self.clan = (info["clan"]["name"], info["clan"]["tag"][1:])

		def get_win_ratio(self):
			return self.wins/ self.losses


# player = Player("Y0VGUUPLP")
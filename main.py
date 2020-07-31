from typing import List, Optional
from clash import get_cards 
from player import Player, Clan
from errors import *
import getopt
import sys

def print_player_help() -> None:
	print("\nHelp: p [player tag] [options...]")
	print("\tPrints information about the player. The player tag is the set of characters\n\tfound the username in the player profile portal.\n")
	print("\tOPTIONS:")
	# if no number given, prnts all of that type (type must be supplied)
	print("\t\t-a\t\tReturn current arena")
	print("\t\t-c\t\tReturn the type of chest indexed at when the player will recieve the chest.")
	print("\t\t--lvl\t\treturn the level of the player.") 
	print("\t\t-t\t\tReturn the current trophy count of the player.")
	print("\t\t--wl\t\tReturn the singles win loss ratio of the player.")
	print("\t\t-d\t\tReturn the current deck of the player.")
	print("\t\t--clan\t\tReturn the current clan of the player.")
	print("\t\t--don\t\tReturn the number of donations given and received for the week")
	print("\t\t-w\t\tReturn war day wins")
	print("\t\t-r\t\tReturn the role of the player in the clan.")
	print("\t\t-b\t\tReturn the total number of battles (including doubles).\n")
	print("\t\tALIAS:\n\tplayer\n")
	print("\n\tARGUMENT:\n\t\tplayer tag\tfound in player profile portal under the\n\t\t\t\tusername.\n")

def print_clan_help() -> None:
	print("\nHelp: c [clan tag] [options...]\n\tPrints information about the clan. The clan tag is found under the clan profile.\n")
	print("\tOPTIONS:")
	print("\t\t-s\t\tReturn the clan score.")
	print("\t\t-t\t\tReturn the current amount of clan war trophies.")
	print("\t\t-a\t\tReturn a list of all members with their rank and level.")
	print("\t\t-d\t\tReturn a list of members with donations given and received.")
	print("\t\t-h\t\tReturn the highest donor or number of highest donors if given an integer argument greater than 0 (in descending order).")
	print("\t\t-w\t\tReturn the lowest donor or number of lowest donors if given an integer argument greater than 0 (in descending order).")
	print("\t\t-l\t\tReturn the leader.")
	print("\t\t-c\t\tReturn the clan coleaders.")
	print("\t\t-e\t\tReturn the clan elders.")
	print("\t\t-m\t\tReturn the clan members.")
	print("\n\tALIAS:\n\t\tclan\n\n\tARGUMENT:\n\t\tclan tag\t\tfound under the clan profile.\n")

def print_compare_player_help() -> None:
	print("\nHelp: cp [platyer tag] [player tag]... [options...]\n\tDisplays information on players for comparison.\n")
	print("\tOPTIONS:")
	print("\t\t-a\t\Displays arenas.")
	print("\t\t--lvl\t\tDisplays the levels of the players.") 
	print("\t\t-t\t\tDisplays the trophy counts of the players.")
	print("\t\t--wl\t\tDisplays the singles win loss ratio of the players.")
	print("\t\t--clan\t\tDisplays the current clans of the player.")
	print("\t\t--don\t\tReturn the number of donations given and received for the week")
	print("\t\t-w\t\tReturn war day wins")
	print("\t\t-b\t\tReturn the total number of battles (including doubles).")
	print("\n\tALIAS:\n\t\tcompare\n\n\tARGUMENT:\n\t\tplayer tags\t\tfound under the player profile.\n")

# api_key unnecessary, just use it to work with the switch statement
def print_help(args: List[str], api_key: str = None) -> None:
	opts, args = getopt.gnu_getopt(args, 'cp', ["cmp"])
	print(opts)
	flag = True
	for o, a in opts:
		o = o.replace('-', '')
		if o == "p":
			print_player_help()
			flag = False
			break
		elif o == "c":
			print_clan_help()
			flag = False
			break
		elif o == "cmp":
			print_compare_player_help()
	if flag:
		print('CLASH ROYALE REPL\nCommands:\n\th\tprints list of commands available.')
		print('\t-p\tprints player specific information. Enter "h -p" for more information on the p command.')
		print('\t-c\tprints clan specific information. Enter "h -c" for more information on the c command.')
		print('\t--cmp\tprints compare specific information. Enter "h --cmp" for more information on the cmp command.')

def compare_player_cmd(args: Optional[List[str]], api_key: str = None) -> None:
	opts, args = getopt.gnu_getopt(args, 'atwb', ["lvl", "wl", "clan", "don"])
	for o, a in opts:
		o = o.replace('-', '')
		if o == 'a':
			pass
		if o == 't':
			pass
		if o == 'w':
			pass
		if o == 'b':
			pass
		if o == "lvl":
			pass
		if o == "wl":
			pass
		if o == "clan":
			pass
		if o == "don":
			pass
def clan_cmd(args: Optional[List[str]], api_key: str = None) -> None:
	opts, args = getopt.gnu_getopt(args, 'stmd::h::w::leca::')
	if len(args) < 2:
		print('Missing arguments. Enter "h -c" for more information on the clan command')
		return
	tag = args[1].upper()
	try:
		c = Clan(tag, api_key) if api_key else Clan(tag, server=True)
	except ResourceError:
		print("Clan tag did not match any known clan tags")
		return
	print(f"Clan name: {c.name}")
	for o, a in opts:
		o = o.replace('-', '')
		if o == 's':
			print(f"\tClan Score: {c.clan_score}")
		if o == "t":
			print(f"\tClan Trophies: {c.trophies}")		
		if o == 'm':
			c.get_members()
		if o == "d":
			pass
		if o == 'h':
			if a:
				c.get_donors(amount=int(a))
			else:
				c.get_donors()
		if o == 'w':
			if a:
				c.get_donors(amount=int(a), reverse=True)
			else:
				c.get_donors(reverse=True)
		if o == 'l':
			print(f"\tLeader: {c.get_leader}")
		if o == 'e':
			c.get_elders()
		if o == 'c':
			c.get_coleaders()
		if o == 'a':
			c.print_members()



def player_cmd(args: Optional[List[str]], api_key: str = None) -> None:
	opts, args = getopt.gnu_getopt(args, 'ndbctawr', ["don", "lvl", "wl", "clan"])
	if len(args) < 2:
		print('Missing arguments. Enter "h -p" for more information on the player command')
		return
	tag = args[1].upper()
	# pull info from server
	try: 
		# send request to server, wait for response (sending just the tag)
		p = Player(tag, api_key) if api_key else Player(tag, server=True)
		print(f"Player {p.name}:")
		for o, a in opts:
			o = o.replace('-', '')
			if o == 'c':
				p.print_upcoming_chests()
			if o == "wl":
				print(f"\tWin Loss Ratio: {p.get_win_ratio()}")
			if o == "lvl":
				print(f"\tLevel: {p.level}")
			if o == 'd':
				p.print_current_deck()
			if o == "clan":
				print(f"\tClan: {p.clan[0]}")
			if o == 'b':
				print(f"\tTotal Number of Battles: {p.total_battles}")	
			if o == 't':
				print(f"\tTrophy Count: {p.current_trophies}")
			if o == "a":
				print(f"\tCurrent Arena: {p.arena}")
			if o == "don":
				print(f"\tDonations:")
				print(f"\t\tReceived: {p.donations[1]}")
				print(f"\t\tGiven: {p.donations[0]}")
			if o == 'w':
				print(f"\tTotal War Day Wins: {p.war_day}")
			if o == 'r':
				if p.role:
					print(f"\tRole: {p.role}")
				else:
					print("Not in Clan")
	except ResourceError:
		print("Player tag did not match any known player tags")
	# add some more excepts for different errors in errors class

# def compare_players(args, stat):
# 	pass

# compare stats between clans
# def compare_clans(args, stat):
# 	pass

commands = {
		"help":print_help, 
		'h':print_help, 
		'p':player_cmd, 
		"player":player_cmd,
		"clan" : clan_cmd,
		'c': clan_cmd,
		"cp": compare_player_cmd,
		"compare": compare_player_cmd
	}

def parse(full_cmd: List[str], api_key:str, server: bool) -> bool:
	arg = full_cmd[0]
	if arg == 'q' or arg == "quit" or arg == "exit":
		return False
	if arg not in commands:
		print('Command not recognized. Enter "h" or "help" for a list of commands.')
	else:
		if server:
			commands[arg](full_cmd)
		else:
			commands[arg](full_cmd, api_key)
	return True


def repl(api_key: str, server: bool) -> None:
	exit = True
	while exit:
		cmd = input("Clash Royale>> ")
		# command first then options
		cmd.strip()
		cmd_list = list(map(lambda x: x.lower(), cmd.split()))
		if cmd is None or not len(cmd):
			print('No command entered. Enter "h" or "help" for list of commands.')
		else:
			exit = parse(cmd_list, api_key, server)

def main() -> None:
	print("\nEnter the file for your API Key.")
	print('If you are using a pre-added key, type "default" or "d"')
	print('If you are connecting to the server, type "server" or "s"')
	print('Type "quit" or "q" to exit')
	server = False
	exit = True
	while exit:
		api_key = input("API file>> ")
		api_key.lower().strip()
		if api_key == 'd' or api_key == 'default':
			api_key = None
			exit = False
		elif api_key == 'q' or api_key == 'quit':
			print('quit')
			sys.exit(0)
		elif api_key == 's' or api_key == 'server':
			print('server')
			api_key = None
			server = True
			exit = False
		else:
			try:
				# just a quick test to see if you can access api
				print(get_cards(api_key))
			except FileNotFoundError:
				print("Please enter a txt file containing the api key.")
				print("If you do not have one, just connect to the server.")
			except AccessDeniedError:
				print("The key you entered was not a valid key.")
				print("Try again with a new key or connect to the server.")

	repl(api_key, server)


if __name__ == "__main__":
	main()
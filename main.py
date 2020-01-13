import clash
from player import Player

def print_player_help():
	# TODO: need to add -w and -l 
	# print("\nHelp: p [player tag] [options...]\n\tPrints information about the player." +
	#  "The player tag is the set of characters\n\tfound the username in the player profile portal.\n\n" + 
	#  "\tOPTIONS:\n\t\t-l[s/d][number of matches]\t\treturn the number of battles\n\t\t\t\t\t\t\tincluding" + 
	#  " details.\n\t\t-c\t\tReturn the type of chest indexed at when the player will\n\t\t\t\trecieve the" + 
	#  "chest.\n\t\t-n\t\tReturn the name of the player.\n\t\t-lvl\t\treturn the level of the player.\n" + 
	#  "\t\t-t\t\tReturn the current trophy count of the player.\n\t\t-wl\t\tReturn the singles win loss" + 
	#  " ratio of the player.\n\t\t-d\t\tReturn the current deck of the player.\n\t\t-clan\t\tReturn the" + 
	#  " current clan of the player.\n\t\t-b\t\tReturn the total number of battles (including doubles).\n" + 
	#  "\n\t\tALIAS:\n\tplayer\n\n\tARGUMENT:\n\t\tplayer tag\t\tfound in player profile portal under the" + 
	#  "\n\t\t\t\t\tusername.\n")
	print("\nHelp: p [player tag] [options...]")
	print("\tPrints information about the player. The player tag is the set of characters\n\tfound the username in the player profile portal.\n")
	print("\tOPTIONS:")
	print("\t\t-l[s/d][number of matches]\t\treturn the number of battles")
	print("\t\t\t\t\t\t\tincluding details.")
	print("\t\t-c\t\tReturn the type of chest indexed at when the player will\t\t\t\trecieve the chest.")
	print("\t\t-n\t\tReturn the name of the player.")
	print("\t\t-lvl\t\treturn the level of the player.") 
	print("\t\t-t\t\tReturn the current trophy count of the player.")
	print("\t\t-wl\t\tReturn the singles win loss ratio of the player.")
	print("\t\t-d\t\tReturn the current deck of the player.")
	print("\t\t-clan\t\tReturn the current clan of the player.")
	print("\t\t-b\t\tReturn the total number of battles (including doubles).\n") 
	print("\t\tALIAS:\n\tplayer\n")
	print("\n\tARGUMENT:\n\t\tplayer tag\t\tfound in player profile portal under the\n\t\t\t\t\tusername.\n")

def print_clan_help():
	# TODO: consolidate to one function
	print("\nHelp: c [clan tag] [options...]\n\tPrints information about the clan. The clan tag is found under the clan profile.\n")
	print("\tOPTIONS:")
	print("\t\t-s\t\tReturn the clan score.")
	print("\t\t-m\t\tReturn a list of members with their rank.")
	print("\t\t-md\t\tReturn a list of members with donation amount.")
	print("\t\t-mdr\t\tReturn a list of members with number of donations\n\t\t\t\trecieved.")
	print("\t\t-td\t\tReturn the highest donor.")
	print("\t\t-l\t\tReturn the leader.")
	print("\n\tALIAS:\n\t\tclan\n\n\tARGUMENT:\n\t\tclan tag\t\tfound under the clan profile.\n")

def print_help(arg):
	if arg:
		if arg == "p" or arg == "player":
			print_player_help()
		elif arg == "c" or arg == "clan":
			print_clan_help()
	else:
		print('CLASH ROYALE REPL\nCommands:\n\th\t\tprints list of commands available.')
		print('\tp\t\tprints player specific information. Enter "h p" for more information on the p command.')
		print('\tc\t\tprints clan specific information. Enter "h c" for more information on the c command.')

def get_player_cmd(arg, api_key):
	# handle one tag as of now
	if arg is None or len(arg) < 2: 
		print('Missing arguments. Enter "h p" for more information on the player command')
	else:
		p = Player(arg[0].upper(), api_key)
		if arg[1][0] != "-":
			print("Invalid argument.")
		else:
			if arg[1][1:].strip() == "n":
				print(p.name)
			elif arg[1][1:].strip() == "wl":
				print(p.get_win_ratio())






# compare statistics between players (if player hasn't been search for prior, needs to query api)
# def compare_players(args, stat):
# 	pass

# compare stats between clans
# def compare_clans(args, stat):
# 	pass

def parse(full_cmd, api_key):
	cmd = full_cmd[0]
	cmd.lower()
	# will either be one (full information), or specify what info you want
	arg = None
	if len(full_cmd) > 1:
		arg = full_cmd[1:]
		# this should be either clan tag or player tag
		# for arg in args:
		# 	arg.strip().lower()
	if cmd == "p" or cmd == "player":
		# loop through args again, if preceeded by -, lowercase 
		get_player_cmd(arg, api_key)
	# elif cmd == "c" or cmd == "clan":
		# format_clan_info(arg, api_key)
	# elif cmd == "cmp" or "compare":
	# need a way to distinguish between clan and player

	elif cmd == "h" or cmd == "help":
		print_help(arg)
	elif cmd == "q" or cmd == "quit" or cmd == "exit":
		return False
	else:
		print('Command not recognized. Enter "h" or "help" for a list of commands.')
	return True


def repl(api_key):
	# figure out why this creates two spaces
	print('\n')
	# keep running list in current session for comparison
	exit = True
	# players = list()
	# clans = list()
	while exit:
		cmd = input("Clash Royale>> ")
		cmd.strip()
		cmd = cmd.split()
		if cmd is None or not len(cmd):
			print('No command entered. Enter "h" or "help" for list of commands.')
		else:
			exit = parse(cmd, api_key)

def main():
	# TODO: ignore signals
	print("\nEnter the file for your API Key.")
	print('If you are using a preadded key, type "Default"')
	api_key = input("API file>> ")
	api_key.lower().strip()
	# need a check for an actual api key
	if api_key == "default" or api_key == "d":
		api_key = None
	repl(api_key)


if __name__ == "__main__":
	main()
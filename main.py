import clash

def quit(cmd):
	if cmd == "q" or cmd == "quit" or cmd == "exit":
		return True
	return False

def print_help()
	
def parse(full_cmd, api_key):
	cmd = full_cmd[0]
	cmd.lower()
	# will either be one (full information), or specify what info you want
	arg = None
	if len(full_cmd) > 1:
		arg = full_cmd[1:]
	# this should be either clan tag or player tag
	arg.strip().upper()
	if cmd == "p":
		format_player_info(arg, api_key)
	else if cmd == "c":
		format_clan_info(arg, api_key)
	else if cmd == "h" or 
	else:
		print('Command not recognized. Enter "h" or "help" for a list of commands.')


def repl(api_key):
	exit = True
	while exit:
		cmd = input(">> ")
		cmd.strip()
		cmd = cmd.split()
		if cmd is None or not len(cmd):
			print('No command entered. Enter "h" or "help" for list of commands.')
		else:
			parse(cmd, api_key)
			if quit(cmd):
				exit = False




def main():
	print("\nEnter the file for your API Key.")
	print('If you are using a preadded key, type "Default"')
	api_key = input(">> ")
	api_key.lower().strip()
	if api_key == "default":
		api_key = None
	repl(api_key)


if __name__ == "__main__":
	main()
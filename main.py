import clash

def quit(cmd):
	if cmd == "q" or cmd == "quit" or cmd == "exit":
		return True
	return False
	
def parse(cmd, api_key):
	if cmd[0] == "p":
		format_player_info()


def repl(api_key):
	exit = True
	while exit:
		cmd = input(">> ")
		cmd.lower().strip()
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
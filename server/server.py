from flask import Flask
app = Flask(__name__)

@app.route('/players', methods=['POST'])
def get_player_info():
	pass

if __name__ == '__main__':
	app.run()
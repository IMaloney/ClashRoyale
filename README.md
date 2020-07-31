# Clash Royale CLI

## Description:
A Command Line information to pull information on clans and players, allowing you to compare data. There is a website (not made by me), but I use this tool when I'm in school and can't access that site. You can keep up with your clan to see who is donating.

## Installation:
You should probably setup a virtual environment for this so the modules don't conflict with anything you already have setup. If you really don't care, then you can skip that step and just install the dependencies. To do so, type:

`pip install -r requirements.txt`

in the directory containing the project. This will install everything you need to run.

## Usage:
There are a couple of ways to use this. You can use your own api key (which is generated on the developers page) or you can connect to the server setup. To do so, when starting up the cli,  instead of supplying the location to the api key file, just type:

`s`

or 

`server`

## Commands:

## Help
`h [options]`

### Options:
	-c prints the clan command help
	-p prints the player command help
	--cmp prints the compare player command help

 ---
** All commands from this point on require the tag of a player or clan (located under object's profile in game) **
 ---

## Player
`p [player tag] [options...]`
Prints information about the player

### Options:
	-a      prints player's current arena
	-c      prints player's upcoming chests by amount of matches 
	--lvl   prints player's level
	-t      prints player's current amount of trophies
	--wl    prints player's win loss ratio
	-d      prints player's current deck
	--clan  prints player's clan
	--don   prints player's amount of received and given donations
	-w      prints player's war day wins
	-b      prints player's total number of battles
	-r      prints player's clan role

## Clan
`c [clan tag] [options...]`

### Options:
	-s      prints clan's score
	-t      prints clan's current war trophies
	-a      prints list of members with ranks and levels
	-d      prints list of members with received and given donations
	-h      prints highest donor or number of donors (with an int argument given)
	-w      prints lowest donor or number of donors (with an int argument given)
	-l      prints the leader
	-c      prints the coleaders
	-e      prints the elders
	-m      prints the members

## Compare player
`cp [player tag] [player tag]... [options]`

### Options:
	-a      prints the players' arenas
	--lvl   prints the players' levels
	-t      prints the players' trophy counts
	--wl    prints the win loss ration of each player
	--clan  prints the clan each player is in
	--don   prints the players' amount of received and given donations
	-w      prints the players' war day wins
	-b      prints the players' total battle count

### TODO:
- add clan comparison 
- set up server
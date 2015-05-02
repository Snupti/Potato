import requests
import operator
import time

self_user = "Snupti"
compats = []

page = 1

x = 0
def getFollowers():
	global page
	global x
	payload = {'followed_by':self_user, 'page': page}
	page += 1
	r = requests.get("http://hummingbird.me/users", params=payload)
	r = r.json()
	users = r['users']
	if users == []:
		return
	for user in users:
		print(user['id'])
		x = x + 1
		r = requests.get("https://hbird-cmp-node.herokuapp.com/compatibility/anime?user1=" + self_user + "&user2=" + user['id'])
		r = r.json()
		print(r)
		percent = r.get('percent')
		if percent != "Not enough in common" and percent != None:
			print(str(x) + " " + user['id'] + ": " + r['percent'])
			compat = {'id': user['id'], 'percent': r['percent']}
			compats.append(compat)
		time.sleep(1)
	getFollowers()
getFollowers()

compats.sort(key=operator.itemgetter('percent'), reverse=True)

i = 0
for user in compats:
	i = i + 1
	open("list.txt", 'a').write(str(i) + ": " + user['id'] + " -  " + user['percent'] + '\n')
	print(str(i) + ": " + user['id'] + " -  " + user['percent'])

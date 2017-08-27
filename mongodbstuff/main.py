
import random
from pymongo import MongoClient


data = {
	"user1":{
		"id":12221,
		"is_payment_complete":False,
		"counter":0,
		"team_name":"@team1"
	}
}

client = MongoClient('mongodb://:@ds161493.mlab.com:61493/dcbot')

# database
db = client.dcbot
# db collection 
users = db.user_info 
listname = ["Jake","Jim","Kim"]
# {'fb_id':{"name":x,"age":random.randint(10,25)}}
for x in listname:
	users.insert({'name':x,'food':'Pizza','counter':0})
	print("inserted ",x)

print("show Inserted users")
user = users.find({'counter':0})
for y in user:
	#users.remove(y)
	user['counter'] = 1 
	users.save(user) 

	print(y)
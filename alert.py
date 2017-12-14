import json, sched, time, urllib2
from twilio.rest import Client
import config

print('''***
Checking Coin Market Cap every %d seconds for %s.

Price Alert set to %s %s   
***''' %(config.api_interval, config.coin.capitalize(), config.minimum, config.price_type.upper()))

def sendSMS(body):
	client = Client(config.account_sid, config.auth_token)
	message = client.messages.create(
		to = config.sms_to,
		from_ = config.sms_from_,
		body = body)

	print (message.sid)

def checkPrice(sc): 
	#check API
	results = json.loads(urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/%s/" % config.coin).read())
	
	print("%f - %f " %(float(results[0]['price_btc']), float(config.minimum)))

	if float(results[0]["price_%s" %config.price_type]) < float(config.minimum):
		body = "WARNING: %s is below %s" %(config.coin, config.minimum)
		sendSMS(body)
	else:
		print("we good")

	s.enter(config.api_interval, 1, checkPrice, (sc,))

s = sched.scheduler(time.time, time.sleep)

s.enter(config.api_interval, 1, checkPrice, (s,))
s.run()



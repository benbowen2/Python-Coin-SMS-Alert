import json, sched, time, urllib2

from twilio.rest import Client

import config

s = sched.scheduler(time.time, time.sleep)

print("https://api.coinmarketcap.com/v1/ticker/%s/" % config.coin)

def checkPrice(sc): 
	#check API
	results = json.loads(urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/%s/" % config.coin).read())
	
	print("%f - %f " %(float(results[0]['price_btc']), float(config.minimum)))

	if float(results[0]['price_btc']) < float(config.minimum):
		sendSMS("WARNING: %s is below %s" %(config.coin, config.minimum))
	else:
		print("we good")

	s.enter(10, 1, checkPrice, (sc,))

s.enter(10, 1, checkPrice, (s,))
s.run()


def sendSMS(body):
	client = Client(config.account_sid, config.auth_token)
	message = client.messages.create(
		to = config.sms_to,
		from_ = config.sms_from_,
		body = body)

	print (message.sid)



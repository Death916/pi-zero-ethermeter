
from coin_api import CoinApi
import asyncio
import sys
import traceback
import time
import emailconnect

async def main(loop):
	""" main class that starts the event loop controlling the API and the display """
	usage()
	# display = CoinDisplay(loop)
	api = CoinApi(loop, get_coin(), get_market(), get_currency())
	log('using api ' + api.get_endpoint())
	calls = 0
	calls2 = 0
	calls3 = 0
	while 1:


		# display.on_load()
		try:

			log('updating value of ' + api.get_coin() + ' at ' + api.get_market())
			percent_change = await api.percent_change()
			log(api.get_coin() + 'market change in last 24hrs is ' + str(percent_change) + '%')

			if percent_change >= 3:
				if calls in range(0, 99999, 100):
					logEmail(api.get_coin() + 'market change in last 24hrs is ' + str(percent_change) + '%')
				#email = threading.Thread(target=logEmail(api.get_coin() + 'market change in last 24hrs is ' + str(percent_change) + '%'))
				#email.start()
				calls = 1
			else:
				calls = 0

			if percent_change >= -5:
				if calls2 in range(0, 99999, 100):
				#email = threading.Thread(target=logEmail(api.get_coin() + 'market change in last 24hrs is ' + str(percent_change) + '%'))
				#email.start()
					logEmail(api.get_coin() + 'market change in last 24hrs is ' + str(percent_change) + '%')
					calls2 = 1
			else:
				calls2 = 0

			if calls3 in range(0, 99999, 100):

				#email = threading.Thread(target=logEmail(api.get_coin() + 'market change in last 24hrs is ' + str(percent_change) + '%'))
				#email.start()

				logEmail(api.get_coin() + 'market change in last 24hrs is ' + str(percent_change) + '%')
				calls3 = 1

			# display.on_data(percent_change)
		except KeyError:
			log('no api data available for coin:market:currency combination.')
			# display.on_error()
		except Exception:
			print(traceback.format_exc())
			# display.on_error()
		await asyncio.sleep(api.throttle())
		calls += 1
		calls2 += 1
		calls3 += 1
def usage():
	print('================================================')
	print('|              <!> CoinEmail 0.2 <!>           |')
	print('---------with code from ethermeter 1.0----------------')
	print('-------------------------------------------------')
	print('usage: python coinEmail.py <coin> <market> <currency>')
	print('example: python coinEmail.py ETH Coinbase USD')
	print('-------------------------------------------------\n')

def get_coin():
	return get_arg(1, 'LTC')

def get_market():
	return get_arg(2, 'Coinbase')

def get_currency():
	return get_arg(3, 'BTC')


def get_arg(index, default):
	params = ['coin', 'market', 'currency']
	if (len(sys.argv) > index):
		log('using ' + sys.argv[index] + ' as ' + params[index - 1])
		return sys.argv[index]
	else:
		log('no ' + params[index - 1] + ' specified, using ' + default)
		return default


def logEmail(line):

	print(time.strftime('%H:%M:%S') + ' > ' + line + ' ..')
	email = emailconnect.SendMail()
	email.send(line)
	asyncio.sleep(240)



def log(line):
	print(time.strftime('%H:%M:%S') + ' > ' + line + ' ..')

try:
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main(loop))
	loop.run_forever()
except KeyboardInterrupt:
	log('blockchains is the future, goodnight')
	pass

#!python 3

import smtplib

class SendMail():

	def __init__(self):
		print('email server connecting')

	def send(self, msg):
		try:
			self.server = smtplib.SMTP('smtp.gmail.com', 587)
			self.server.ehlo()
			self.server.starttls()
			self.server.login('tavn1992@gmail.com', 'ikoevgbbrrjeowtr')
			print('login success')
			self.server.sendmail('tavn1992@gmail.com', 'tavn1992@gmail.com', msg)
			print('update sent')



		except:
			print('login error')



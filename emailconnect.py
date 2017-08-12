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
			# enter login info 
			self.server.login('email login', 'email pass')
			print('login success')
			# fill in to and from fields
			self.server.sendmail('from', 'to', msg)
			print('update sent')
			self.server.quit()



		except:
			print('login error')



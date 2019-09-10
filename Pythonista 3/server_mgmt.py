# coding: utf-8

import requests
import socket
import struct
import os
import sys
import re
import ui

def button_tapped(sender): # the button has been pressed
	if server_down == True: # check if server is down, then wake it
		macaddress = 'abcdef123456' # replace with your server MAC address (check $ arp -a)
# Wake-On-Lan code goes here
		data = ''.join(['FFFFFFFFFFFF', macaddress * 20])
		send_data = b''

		for i in range(0, len(data), 2):
			send_data = b''.join([send_data,
				struct.pack('B', int(data[i: i + 2], 16))])

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		sock.sendto(send_data, ('123.123.123.255', 7)) # replace to your net broadcast address

		sender.title = 'Boot will start shortly' # set UI header
		sender.action = None # disable any further actions on the button
	else: # otherwise power it off
		poweroff_req = requests.get(poweroff_url) # access the "magic" web script
		sender.action = None  # and disable further actions on the button
		if poweroff_req.status_code == 200: # if we get http code 200 - the script has run correctly
			sender.title = 'Poweroff is scheduled'
		else:
			sender.title = 'Poweroff FAILED'


# make a new UI and add some buttons
view = ui.View()
view.name = 'Server management'
view.background_color = 'white'
view.frame = (0, 0, 300, 200)

# start with a quick check
label = ui.Label(text='Checking server status... Please wait...')
label.frame = (4, 4, 200, 100)
view.add_subview(label)

button = ui.Button(title='') # make a blank button
button.center = (view.width * 0.5, view.height * 0.5)
button.flex = 'LRTB' # layout properties, see Pythonista guide
button.action = button_tapped
view.add_subview(button)

view.present('sheet')

# set to your server configuration
base_url = 'http://123.123.123.123:12345/web-scripts'

# set names of your scripts (leave these names if you haven't changed them after downloading)
checker_url = base_url + '/status.sh'
poweroff_url = base_url + '/power.sh'

# let's assume the server is up
server_down = False

try:
	# try to get status response from the web server within 0.3 sec (it is more than enough time on most configurations)
	checker_req = requests.get(checker_url, verify=False, timeout=0.3)
except:
	server_down = True # if we don't get a prompt reply, the server is down

# if it is up, let's check response: it should have an http code 200 and keyword OK
if server_down == False and checker_req.status_code == 200 and checker_req.text.rstrip() == 'OK':
	# if so, let's comment it in our UI and change the "magic button" to power off
	label.text = 'Server is up and running'
	button.title = 'Power OFF'
	server_down = False
else: # or let's advise to bring the server back
	label.text = 'Server seems to be down'
	button.title = 'Power ON'
	server_down = True

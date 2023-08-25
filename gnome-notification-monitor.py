import os
import dbus
import json
import requests

from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

url = "https://api.line.me/v2/bot/message/push"
user_id = os.getenv('LINEPUSH_USER_ID')
channel_access_token = os.getenv('LINEPUSH_CHANNEL_ACCESS_TOKEN')
last_text = None

#print(user_id, channel_access_token)

if not user_id or not channel_access_token:
	print('Please set LINEPUSH_USER_ID and LINEPUSH_CHANNEL_ACCESS_TOKEN')
	exit(1)

def linepush(text):
	payload = {
		"to": user_id,
		"messages": [{"type": "text", "text": text}]
	}
	headers = {
		"Content-Type": "application/json",
		"Authorization": f"Bearer {channel_access_token}"
	}
	response = requests.post(url, json=payload, headers=headers)
	if response.status_code != 200:
		print("Errore nell'invio del messaggio:", response.text)

def notifications(bus, message):
	args = message.get_args_list()
	if args and len(args) >= 2:
		#print(json.dumps(args, indent=4))
		title = " ".join(args[3].split())
		body = " ".join(args[4].split())
		text = title
		if last_text != text:
			last_text = text
			print("Send:", text)
			linepush(text)

DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'")
bus.add_message_filter(notifications)

mainloop = GLib.MainLoop()
mainloop.run()

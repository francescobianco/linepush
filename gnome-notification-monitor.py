import os
import dbus
import json

from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

user_id = os.getenv('LINEPUSH_USER_ID')
channel_access_token = os.getenv('LINEPUSH_CHANNEL_ACCESS_TOKEN')

if not user_id or not channel_access_token:
	print('Please set LINEPUSH_USER_ID and LINEPUSH_CHANNEL_ACCESS_TOKEN')
	exit(1)

def notifications(bus, message):
	args = message.get_args_list()
	if args and len(args) >= 2:
		print(json.dumps(args, indent=4))
		body = args[3]  # Supponiamo che il messaggio testuale sia nel quarto argomento (indice 3)
		print("Messaggio:", body)

DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'")
bus.add_message_filter(notifications)

mainloop = GLib.MainLoop()
mainloop.run()

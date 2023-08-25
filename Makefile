
-include .env
export $(shell test -f .env && cut -d= -f1 .env)

install:
	@install -m 755 linepush /usr/local/bin/

test:
	@bash linepush "Hello World!"

test-gnome-notification-monitor:
	@python3 gnome-notification-monitor.py

test-id115-display:
	#@bash linepush "1----2----3----4----5"
	@bash linepush "@"

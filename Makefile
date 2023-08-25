
-include .env
export $(shell test -f .env && cut -d= -f1 .env)

install:
	@install -m 755 linepush /usr/local/bin/

test:
	@bash linepush "Hello World!"

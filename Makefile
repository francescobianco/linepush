
-include .env
export $(shell test -f .env && cut -d= -f1 .env)

test:
	@bash linepush "Hello World!"

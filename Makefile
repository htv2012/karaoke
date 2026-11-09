.PHONY: generate add default

default: add

generate:
	./bin/clean_source.py
	./bin/generate.py

add: generate
	git add .
	git commit -m "Add songs"
	git push

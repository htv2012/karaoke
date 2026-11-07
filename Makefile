.PHONY: generate

generate:
	./bin/clean_source.py
	./bin/generate.py

add: generate
	git add .
	git commit -m "Add songs"
	git push

.PHONY: generate add default clean

default: generate

generate: clean
	./bin/generate.py

clean:
	./bin/normalize_raw.py

add: generate
	git add .
	git commit -m "Add songs"
	git push

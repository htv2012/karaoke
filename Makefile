.PHONY: generate add default clean

default: generate

generate: clean
	./bin/generate.py

clean:
	./bin/clean_source.py

add: generate
	git add .
	git commit -m "Add songs"
	git push

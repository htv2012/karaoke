.PHONY: generate add default clean check

default: check generate

generate: clean
	./bin/generate.py

clean:
	./bin/normalize_raw.py

check:
	uv tool run ruff format bin/g*.py
	uv tool run ruff check --select I --fix bin/g*.py
	uv tool run ruff check --fix bin/g*.py
	uv tool run ty check bin/g*.py
	#uv tool run ruff format bin/*.py
	#uv tool run ruff check --select I --fix bin/*.py
	#uv tool run ruff check --fix bin/*.py
	#uv tool run ty check bin/*.py

add: generate
	git add .
	git commit -m "Add songs"
	git push


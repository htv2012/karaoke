.PHONY: markdown add default clean check

default: markdown

markdown: clean check
	./bin/create_markdown.py

clean:
	./bin/normalize_raw.py

check:
	uv tool run ruff format bin/*.py
	uv tool run ruff check --select I --fix bin/*.py
	uv tool run ruff check --fix bin/*.py
	uv tool run ty check bin/*.py

add: markdown
	git add .
	git commit -m "Add songs"
	git push


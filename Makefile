env:
	cp .env.sample .env	


# INIT APPLICATION
f:
	echo 123 1> static/thunder/123.txt && rm static/thunder/* && poetry run python main.py

a:
	poetry run python main.py

or:
	open https://github.com/guimassoqueto/scrap-flask

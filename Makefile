env:
	cp .env.sample .env	


# INIT APPLICATION
a:
	echo 123 1> static/kadec/123.txt && rm static/kadec/* && echo 123 1> static/thunder/123.txt && rm static/thunder/* && poetry run python main.py

f:
	poetry run python main.py

or:
	open https://github.com/guimassoqueto/scrap-flask
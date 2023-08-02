env:
	cat .env.sample 1> .env	


# INIT APPLICATION
a:
	echo 123 1> static/fofinho/123.txt && rm static/fofinho/* && echo 123 1> static/thunder/123.txt && rm static/thunder/* && poetry run python main.py

f:
	poetry run python main.py
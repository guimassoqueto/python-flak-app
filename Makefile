env:
	cat .env.sample 1> .env	


# INIT APPLICATION
a:
	echo 123 1> static/123.txt && rm static/* && poetry run python main.py

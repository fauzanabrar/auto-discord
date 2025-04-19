lite:
	pm2 start "python lite.py ns" --name ns
	pm2 start "python lite.py af" --name af
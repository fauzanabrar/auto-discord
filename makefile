lite:
	pm2 start "python lite.py ns" --name ns
	pm2 start "python lite.py af" --name af

tm:
	tmux new-session -d -s ns 'python lite.py ns'
	tmux new-window -t ns:1 -n af 'python lite.py af'

format:
	black src
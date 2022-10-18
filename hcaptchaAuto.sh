#!/bin/bash

tmux kill-session -t 8
tmux kill-session -t 9
tmux kill-session -t 10
tmux new -d -s 8 "bash --init-file <(echo python3 BHcaptcha.py)"
sleep 3600
tmux new -d -s 9 "bash --init-file <(echo python3 FHcaptcha.py)"
sleep 3600
tmux new -d -s 7 "bash --init-file <(echo python3 AHCaptcha.py)"


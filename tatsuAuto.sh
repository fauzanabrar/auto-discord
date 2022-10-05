#!/bin/bash

tmux kill-session -t 0
tmux kill-session -t 1
tmux kill-session -t 2
tmux new -d -s 0 "bash --init-file <(echo python3 auto.py)"
sleep 10
tmux new -d -s 1 "bash --init-file <(echo python3 autoB.py)"
sleep 10
tmux new -d -s 2 "bash --init-file <(echo python3 autoF.py)"

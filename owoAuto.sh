#!/bin/bash

#tmux kill-session -t 5
tmux kill-session -t 6
tmux kill-session -t 7
#tmux new -d -s 5 "bash --init-file <(echo python3 owo.py)"
#sleep 10
tmux new -d -s 6 "bash --init-file <(echo python3 owoB.py)"
sleep 10
tmux new -d -s 7 "bash --init-file <(echo python3 owoF.py)"


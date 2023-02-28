#!/bin/bash

tmux kill-session -t 8
tmux new -d -s 9 "bash --init-file <(echo python3 vote1.py)"
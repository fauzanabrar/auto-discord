#!/bin/bash

tmux kill-session -t 4
tmux new -d -s 4 "bash --init-file <(echo python3 main2.py)"
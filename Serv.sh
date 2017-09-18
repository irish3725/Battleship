#!/bin/bash

cp blank.txt opponent_board.txt
cp board.cp own_board.txt
./server.py 5000 board.txt


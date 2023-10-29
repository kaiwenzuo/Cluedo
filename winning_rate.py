#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: winning_rate.py
@time: 2023/10/29 15:29
@project: Cluedo
@desc: 
"""

from game_core import *

def win_rate(n_player, n):
    from game_run import game_run
    win_list = [0] * n_player

    for i in range(n):
        winner = game_run(GameModel(n_player))
        win_list[winner - 1] += 1

        # Print the winning rate after each iteration
        print(f"After game {i + 1}, the win rates: {[x / (i + 1) for x in win_list]}")

    # Calculate and print the final winning rate
    final_win_rates = [x / n for x in win_list]
    print(f"Final win rates after {n} games: {final_win_rates}")

    return final_win_rates

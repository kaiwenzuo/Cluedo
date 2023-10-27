from game_core import *
from random_agent import random_policy


def game_run(model):
    state = model.state
    player = 1
    while model.state.is_terminal() is None:
        action = random_policy(state.cards)
        print('Player {} suggests {}'.format(player, action))
        state.suggest(player,action)
        state.step += 1
        state.if_accuse(player)
        player = state.next_player(player)
    if model.state.is_terminal() is not None:
        print('In the step {}, the winner is player {}'.format(state.step, model.state.is_terminal()))
        return model.state.is_terminal()

if __name__ == "__main__":
    game_run(GameModel(3))

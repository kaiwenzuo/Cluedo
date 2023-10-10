from dataclasses import dataclass
from typing import NamedTuple, Set, Tuple, List, Dict
import random


@dataclass
class GameState:
    n_players: int
    players: List[int]
    cards_dice: Dict[int, set]
    cards: Set[int]
    accusation: Dict[int, set]
    # information_set:

    def is_terminal(self):
        for i in range(1, self.n_players + 1):
            if self.accusation[i] == self.cards_dice[0]:
                return i
            else:
                return None

    # def suggest(self):


# 分发牌，先抽三张放信封里，之后每个玩家随机分三张
def chance_outcome(n_players, cards_dice=None):
    if cards_dice is None:
        cards_dice = {}
    cards_dice[0] = {random.randint(0, 5), random.randint(6, 11), random.randint(12, 20)}
    cards_left = set(list(range(21))) - cards_dice[0]
    for i in range(1, n_players + 1):
        cards_dice[i] = set(random.sample(cards_left, 3))
        cards_left -= cards_dice[i]
    # print(cards_dice,cards_left)
    return cards_dice, cards_left


class GameModel:
    def __init__(self, n_players: int):
        self.n_players = n_players
        cards_dice, cards_left = chance_outcome(n_players)
        self.state = GameState(n_players=n_players, players=list(range(1, n_players + 1)),
                               cards_dice=cards_dice, cards=set(list(range(21))) - cards_left,accusation = {})



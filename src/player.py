import game_leader
import random

class Player:

    def __init__(self, name: str):
        self.__name: str = name
        self.__decision: int = -1

    def get_name(self) -> str:
        return self.__name

    def get_decision(self) -> int:
        return self.__decision
    
    def play(self) -> int:
        choices = list(game_leader.GameLeader.rock_scissor_paper_choices.values())
        decision = random.choice(choices)
        self.__decision = decision
        return decision

    def is_player_matched(player: any, condition: int) -> bool:
        if not isinstance(player, Player):
            return False
        if player.get_decision() != condition:
            return False
        return True

    def get_players(players: list[any], condition: int):
        matched_players: list[Player] = []
        for player in players:
            if not Player.is_player_matched(player, condition):
                continue
            matched_players.append(player)
        return matched_players
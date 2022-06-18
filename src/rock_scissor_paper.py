import random

class Player:

    def __init__(self, name: str):
        self.__name = name
        self.__decision = ""

    def get_name(self) -> str:
        return self.__name

    def get_decision(self) -> str:
        return self.__decision
    
    def play(self) -> str:
        choices = RockScissorPaper.rock_scissor_paper_choices.values()
        decision = random.choice(choices)
        self.__decision = decision
        return decision

    def is_player_matched(player: any, condition: str) -> bool:
        if not isinstance(player, Player):
            return False
        if player.get_decision() != condition:
            return False
        return True

    def get_players(players: list[any], condition: str):
        matched_players: list[Player] = []
        for player in players:
            if not Player.is_player_matched(player, condition):
                continue
            matched_players.append(player)
        return matched_players

class RockScissorPaper:

    rock_scissor_paper_choices: dict[str, int] = {
            "グー": 0,
            "チョキ": 1,
            "パー": 2
    }

    def __init__(self):
        self.players: list[Player] = []
        self.winner_players: list[Player] = []
        self.play_count: int = 0

    def is_all_same(self, ai_choices: list[int]) -> bool:
        ai_choices = list(ai_choices)
        for i in range(0, len(ai_choices) - 1):
            current_choice = ai_choices[i]
            next_choice = ai_choices[i + 1]
            if current_choice != next_choice:
                return False
        return True

    def is_all_diff(self, ai_choices: list[int]) -> bool:
        ai_choices = list(ai_choices)
        rock_detected = False
        paper_detected = False
        scissor_detected = False
        for choice in ai_choices:
            if choice == self.rock_scissor_paper_choices["グー"]:
                rock_detected = True
            elif choice == self.rock_scissor_paper_choices["チョキ"]:
                scissor_detected = True
            elif choice == self.rock_scissor_paper_choices["パー"]:
                paper_detected = True
            all_detected = rock_detected and scissor_detected and paper_detected
            if all_detected:
                return True
        return False

    def generate_players(self, player_count):
        players = []
        for i in range(0, player_count):
            player_name = f"Player{i}"
            player = Player(player_name)
            player.play()
            players.append(player)
        self.players = players

    def __play(self, ai_count) -> bool:
        self.generate_players(ai_count)
        self.play_count += 1
        if self.is_all_diff(self.players.values()) or self.is_all_same(self.players.values()):
            return False
        if not self.rock_scissor_paper_choices["グー"] in self.players.values():
            self.winner_players = Player.get_players(self.players, "チョキ")
            self.last_choice = "チョキ"
            return True
        if not self.rock_scissor_paper_choices["チョキ"] in self.players.values():
            self.winner_players = Player.get_players(self.players, "パー")
            self.last_choice = "パー"
            return True
        self.winner_players = Player.get_players(self.players, "グー")
        self.last_choice = "グー"
        return True

    def play(self, ai_count):
        is_game_over = False
        while not is_game_over:
            is_game_over = self.__play(ai_count)
        print(f"ゲームのトータル回数: {self.play_count}\n勝者は{self.last_choice}のグループ: {self.winner_players}")
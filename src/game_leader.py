from player import Player

class GameLeader:

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

    def generate_players(self, player_count: int):
        players = []
        for i in range(0, player_count):
            player_name = f"Player{i}"
            player = Player(player_name)
            player.play()
            players.append(player)
        self.players = players

    def __play(self, player_count: int) -> bool:
        self.generate_players(player_count)
        self.play_count += 1
        players_decision: list[int] = [ player.get_decision() for player in self.players ]
        is_game_draw: bool = self.is_all_diff(players_decision) or self.is_all_same(players_decision)
        rock: int = self.rock_scissor_paper_choices["グー"]
        scissor: int = self.rock_scissor_paper_choices["チョキ"]
        paper: int = self.rock_scissor_paper_choices["パー"]
        if is_game_draw:
            return False
        if not rock in players_decision:
            self.winner_players = Player.get_players(self.players, scissor)
            self.last_choice = "チョキ"
            return True
        if not scissor in players_decision:
            self.winner_players = Player.get_players(self.players, paper)
            self.last_choice = "パー"
            return True
        self.winner_players = Player.get_players(self.players, rock)
        self.last_choice = "グー"
        return True

    def play(self, player_count: int):
        is_game_over = False
        while not is_game_over:
            is_game_over = self.__play(player_count)
        winner_players_name: list[str] = [ player.get_name() for player in self.winner_players ]
        print(f"ゲームのトータル回数: {self.play_count}\n勝者は{self.last_choice}のグループ: {winner_players_name}")
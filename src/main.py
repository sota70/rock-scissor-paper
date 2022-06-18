from game_leader import GameLeader

player_count: int = int(input("プレイヤーの数を入力してください: "))
game_leader: GameLeader = GameLeader()
game_leader.play(player_count)
from PracticeApps.Roboter.lib.RegisterGame import RegisterGame
from PracticeApps.Roboter.lib.RegisterName import RegisterName
from PracticeApps.Roboter.lib.RoboterCheckGame import RoboterCheckGame
from PracticeApps.Roboter.lib.RoboterCheckName import RoboterCheckName


class RoboterMain:
    def __init__(self):
        self.customer_name_csv_path = './customer_name_csv'
        self.game_name_csv_path = './game_name_csv'

        self.roboter_check_name = RoboterCheckName()
        self.register_name = RegisterName(self.customer_name_csv_path)
        self.roboter_check_game = RoboterCheckGame()
        self.game_name = RegisterGame(self.game_name_csv_path)

    def run_app(self):
        customer_name = self.roboter_check_name.check_customer_name()
        self.register_name.register_name(customer_name)
        favorite_game = self.roboter_check_game.check_favorite_game(customer_name)
        self.game_name.register_game(favorite_game)


if __name__ == "__main__":
    roboter = RoboterMain()
    roboter.run_app()

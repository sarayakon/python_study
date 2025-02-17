# Check Customer Name for Roboter App
from PracticeApps.Roboter.lib.RegisterGame import RegisterGame


class RoboterCheckGame:

    def __init__(self):
        self.game_name = ""
        self.answer = ""
        self.game_name_csv_path = './game_name_csv'

        self.register_Game = RegisterGame(self.game_name_csv_path)

    def check_favorite_game(self, name):
        answer_number = 0
        self.register_Game.check_exist_favorite_games()
        while answer_number <= 5:
            if answer_number == 0:
                print(f"{name}. What's your favorite game?")
                self.game_name = input().strip().lower()
            print(f'Thank you for your input!Is your favorite game {self.game_name}? Please answer yes or no')
            self.answer = input().strip().lower()
            if self.answer == 'yes':
                break
            elif self.answer == 'no':
                print(f'Please enter your name again.')
                answer_number = 0
            else:
                print(f'Please give the correct answer.')
                answer_number += 1
        if answer_number >= 5:
            print(f'You have exceeded the limit of incorrect answers. Please restart the app.')
        else:
            return self.game_name

# Register Customer Name for Roboter App

import csv
import os
from pathlib import Path


class RegisterGame:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
        os.makedirs(self.folder_path, exist_ok=True)
        self.filename = os.path.join(self.folder_path, "game_name.csv")

    def register_game(self, game_name):
        data = []

        if os.path.exists(self.filename):
            with open(self.filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    row['Count'] = int(row['Count'])
                    data.append(row)

        exist = False
        for row in data:
            if row['Game'] == game_name:
                row['Count'] += 1
                exist = True
                break

        if not exist:
            data.append({'Game': game_name, 'Count': 1})

        with open(self.filename, 'w', newline='') as csvfile:
            fieldnames = ['Game', 'Count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            print(f'registered your favorite game as {game_name}.')

    def check_exist_favorite_games(self):
        data = []

        # ファイルが存在するかチェック
        if os.path.exists(self.filename):
            with open(self.filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    row['Count'] = int(row['Count'])  # `Count` を整数に変換
                    data.append(row)
        else:
            return None

        # `Count` の降順でソート
        sorted_data = sorted(data, key=lambda x: x['Count'], reverse=True)

        # 上位2つを取得
        top_games = sorted_data[:2]

        # 結果を表示
        print("It's a popular game at the moment.")
        for i, game in enumerate(top_games, start=1):
            print(f"{i}. {game['Game']} - {game['Count']} Vote!")

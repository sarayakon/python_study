from PracticeApps.Roboter.lib.RoboterCheckName import RoboterCheckName
from PracticeApps.Roboter.lib.RegisterName import RegisterName


class RoboterMain:
    def __init__(self):
        self.csv_path = './csv'

        self.roboter_check_name = RoboterCheckName()
        self.register_mame = RegisterName(self.csv_path)

    def run_app(self):
        customer_name = self.roboter_check_name.check_customer_name()
        self.register_mame.register_name(customer_name)


if __name__ == "__main__":
    roboter = RoboterMain()
    roboter.run_app()

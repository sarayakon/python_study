from PracticeApps.Roboter.lib.RoboterCheckName import RoboterCheckName


class RoboterMain:
    def __init__(self):
        self.roboter_check_name = RoboterCheckName()

    def run_app(self):
        self.roboter_check_name.check_customer_name()


roboter = RoboterMain()
roboter.run_app()

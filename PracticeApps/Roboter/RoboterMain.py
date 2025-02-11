from PracticeApps.Roboter.lib.RoboterCheckName import RoboterCheckName


class RoboterMain:
    def __init__(self):
        self.roboter_check_name = RoboterCheckName()

        # set yes answers
        self.yes_words = ['yes', 'Yes', 'YES']

        # set no answers
        self.no_words = ['no', 'No', 'NO']

    def run_app(self):
        self.roboter_check_name.check_customer_name()


roboter = RoboterMain()
roboter.run_app()

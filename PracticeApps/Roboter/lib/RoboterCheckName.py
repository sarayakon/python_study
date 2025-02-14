# Check Customer Name for Roboter App


class RoboterCheckName:

    def __init__(self):
        self.customer_name = ""
        self.answer = ""

    def check_customer_name(self):
        answer_number = 0
        while answer_number <= 5:
            if answer_number == 0:
                print(f"Hello! I'm Roboko. What's your name?")
                self.customer_name = input().strip()
            print(f'Thank you for your input!Is your name {self.customer_name}? Please answer yes or no')
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
            return self.customer_name

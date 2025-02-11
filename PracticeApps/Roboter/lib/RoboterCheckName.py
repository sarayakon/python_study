# Check Customer Name for Roboter App
from PracticeApps.Roboter.config import YES_WORDS, NO_WORDS


class RoboterCheckName:

    def __init__(self):
        self.customer_name = ""
        self.answer = ""
        self.second_answer = ""

        # set yes answers
        self.yes_words = YES_WORDS

        # set no answers
        self.no_words = NO_WORDS

    def check_customer_name(self):
        answer_number = 0
        while answer_number <= 5:
            if answer_number == 0:
                print(f"Hello! I'm Roboko. What's your name?")
                self.customer_name = input().strip()
            print(f'Thank you for your input!Is your name {self.customer_name}? Please answer {self.yes_words[0]} or '
                  f'{self.no_words[0]}.')
            self.second_answer = input().strip()
            if self.second_answer in self.yes_words:
                print(f'registered your name as {self.customer_name}.')
                break
            elif self.second_answer in self.no_words:
                print(f'Please enter your name again.')
                answer_number = 0
            else:
                print(f'Please give the correct answer.')
                answer_number += 1
        if answer_number >= 5:
            print(f'You have exceeded the limit of incorrect answers. Please restart the app.')

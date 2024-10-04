
class Answer:
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list

    def question_check(self):
        return self.q_num < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1
        input(f'Q.{self.q_num}: {current_question.q_text} (True/False): ')
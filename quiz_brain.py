
class Answer:
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def question_check(self):
        return self.q_num < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1
        ans = input(f'Q.{self.q_num}: {current_question.q_text} (True/False): ')
        self.check_answer(ans, current_question.q_ans)

    def check_answer(self, ans, correct_ans):
        if ans.lower() == correct_ans.lower():
            self.score += 1
            print(f'Correct, score {self.score}/{self.q_num}')
        else:
            print(f'Wrong, {correct_ans}, score {self.score}/{self.q_num}')
        print('\n')
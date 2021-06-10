
class QuizBrain:
    def __init__(self,q_list):
        self.qustion_number = 0
        self.qustion_list = q_list
        self.score = 0

    def still_has_question(self):

        return self.qustion_number < len(self.qustion_list)
        

    def next_qustion(self):
        current_qustion = self.qustion_list[self.qustion_number]
        self.qustion_number +=1
        user_answer = input(f"Q.{self.qustion_number}: {current_qustion.text}: your answer is T/F")

        self.check_answer(user_answer,current_qustion.answer)
       
    def check_answer(self,user_answer,current_answer):

        if user_answer.lower() == current_answer.lower():
            print('you got right')
            self.score += 1
        else:
            print("that wrunge")    
            print(f"right answer is {current_answer}")    

        print(f"your current score is  {self.score}/{self.qustion_number}")
        print("\n")

        
        

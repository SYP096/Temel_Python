
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        if answer not in self.choices:
            raise ValueError("hatali bilgi")
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]              # 这里返回的是 [q1, q2, q3]   中的任意一个

    def displayQuestion(self):
        question = self.getQuestion()              # 23行 返回这里 ， 这里的question也是4行类的 实例对象

        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input('cevap: ')
        if question.checkAnswer(answer):      # 这里的question也是class Question的实例对象，用来调用Question的实例方法
            self.score += 1

        self.questionIndex += 1

        if len(self.questions) == self.questionIndex:
            print(self.score)
        else:
            self.displayQuestion()


q1 = Question("en iyi programlama dili hangisidir?", ["python", "c#", "java", "dart"], "python")
q2 = Question("en popüler programlama dili hangisidir?", ["python", "java", "c#", "dart"], "python")
q3 = Question("en çok kazandiran programlama dili hangisidir?", ["python", "java", "dart", "c#"], "python")

sorular = [q1, q2, q3]

quiz = Quiz(sorular)

quiz.displayQuestion()

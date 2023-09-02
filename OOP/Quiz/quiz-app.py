# Quiz App
# Question sinifi
#   Instance Attributes
#       - text,  choices,  answer
#   Instance Methods
#       - q1.checkAnswer('python') => True ya da False

q1 = Question("en iyi programlama dili hangisidir?", ["python", "c#", "java", "dart"], "python")
q2 = Question("en popüler programlama dili hangisidir?", ["python", "java", "c#", "dart"], "python")
q3 = Question("en çok kazandiran programlama dili hangisidir?", ["python", "java", "dart", "c#"], "python")

sorular = [q1, q2, q3]

# Quiz sinifi
#   Instance Attributes
#       - questions,  questionIndex,  score
#   Instance Methods
#       - getQuestion()         => questionIndex' e göre question nesnesi getirir.
#       - displayQuestion()     => getQuestion() ile alinan nesneyi gösterir.
#       - loadQuestion()        => Testi başlatir.
#       - displayScore()        => Score bilgisini gösterir.
#       - displayProgress()     => Testdeki ilerlemeyi gösterir. (5 sorunun 2.sorusundasiniz.)

quiz = Quiz(sorular)

# from Code import Question
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "\nWhat color are apples?\n(a) Red/Green\n(b) Magenta\n(c) Yellow\n\n",
    "What color are bananas?\n(a) Red\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Green\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),     # Creating Objects
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

# score = 0
def run_test(questions):
    score = 0
    for question in questions:
        answer = input("Enter: "+question.prompt)

        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" +str(len(questions)) + " correct")

run_test(questions)
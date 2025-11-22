name = input("Welcome! What is your name? ")
current_prize = 0
safe_prize = 0
question_1 = input(
    "Which language runs in a web browser by default?\n"
    "A) Python\n"
    "B) JavaScript\n"
    "C) C++\n"
    "D) Java\n"
    "Your answer: "
)
if question_1.lower() == 'b':
    current_prize = 50
    print('Congratulations,' ,name, 'you have successfully answered a question for £',current_prize)
else:
    print("It's ok", name, ", you still have won £", safe_prize)
    exit()
question_2 = input(
    "What is the capital city of France?\n"
    "A) Berlin\n"
    "B) London\n"
    "C) Paris\n"
    "D) Rome\n"
    "Your answer: "
)
if question_2.lower() == 'c':
    current_prize = 100
    safe_prize = 100
    print('Congratulations,' ,name, 'you have successfully answered a question for £',current_prize)
else:
    print("It's ok", name, ", you still have won £", safe_prize)
    exit()
question_3 = input(
    "What is the process of finding and fixing errors in code called?\n"
    "A) Debugging\n"
    "B) Compiling\n"
    "C) Loading\n"
    "D) Rendering\n"
    "Your answer: "
)
if question_3.lower() == 'a':
    current_prize = 500
    print('Congratulations,' ,name, 'you have successfully answered a question for £',current_prize)
else:
    print("It's ok", name, ", you still have won £", safe_prize)
    exit()
question_4 = input(
    "Which planet is known as the 'Red Planet'?\n"
    "A) Mercury\n"
    "B) Mars\n"
    "C) Venus\n"
    "D) Jupiter\n"
    "Your answer: "
)
if question_4.lower() == 'b':
    current_prize = 1000
    safe_prize = 1000
    print('Congratulations,' ,name, 'you have successfully answered a question for £',current_prize)
else:
    print("It's ok", name, ", you still have won £", safe_prize)
    exit()
question_5 = input(
    "Which of the following data types in Python is mutable?\n"
    "A) tuple\n"
    "B) string\n"
    "C) list\n"
    "D) int\n"
    "Your answer: "
)
if question_5.lower() == 'c':
    current_prize = 10000
    print('Congratulations,' ,name, 'you have successfully answered a question for £',current_prize)
else:
    print("It's ok", name, ", you still have won £", safe_prize)
    exit()
question_6 = input(
    "Who developed the theory of relativity?\n"
    "A) Isaac Newton\n"
    "B) Albert Einstein\n"
    "C) Nikola Tesla\n"
    "D) Galileo Galilei\n"
    "Your answer: "
)
if question_6.lower() == 'b':
    current_prize = 100000
    safe_prize = 100000
    print('Congratulations,' ,name, 'you have won £',current_prize)
else:
    print("It's ok", name, ", you still have won £", safe_prize)
    exit() 

import random
def game():
    correct_answers = 0
    wrong_answers = 0
    while wrong_answers < 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operation = random.choice(['+', '-', '*'])
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        else:
            result = a * b
        user_answer = input(f"{a} {operation} {b} = ")
        if user_answer.isdigit() and int(user_answer) == result:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Ответ неверный.")
            wrong_answers += 1
    print(f"Игра окончена. Правильных ответов: {correct_answers}")
game()
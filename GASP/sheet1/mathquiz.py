from random import randint

total_answers = 1
correct_answers = 0

while total_answers <= 10:
    num1 = randint(2, 10)
    num2 = randint(2, 10)

    product = num1 * num2
    question = f"What is {num1} times {num2}? "

    # Get answer
    while True:
        answer = input(question)
        try:
            answer = int(answer)
            break
        except ValueError:
            print("That's not a number. Please try again.")
    if answer == product:
        correct_answers += 1
        print("That's right -- well done.")
    else:
        print(f"No, I'm afraid the answer is {product}.")
    total_answers += 1

print(f"I asked you 10 questions. You got {correct_answers} of them right.")
print("Well done!")


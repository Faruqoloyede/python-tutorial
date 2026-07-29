questions= ("What is 2 + 2?: ",
            "What is 5 * 6?: ",
            "What is 5-3?: ",
            "What is 10 + 10?: ",
            "what is 9-3?: ")
options = (("A. 4", "B. 3", "C. 10"),
           ("A. 10", "B. 12", "C. 30"),
           ("A. 3", "B. 4", "C. 2"),
           ("A. 20", "B. 30", "C. 50"),
           ("A. 7", "B. 10", "C. 6"),)

correct_answer = ("A", "C", "C", "A", "C")
question_numbers = 0
score = 0
guesses = []

for question in questions:
    print("********************")
    print(question)
    for option in options[question_numbers]:
        print(option)
    guess = input("Enter (A, B, C): ").upper()
    if guess == correct_answer[question_numbers]:
        print("Correct!")
        score +=1
    else:
        print("Wrong!")
        print("Correct answer:", correct_answer[question_numbers])
    question_numbers +=1

print("********************")
score =  int(score/question_numbers * 100)
print(f"Total score: {score}%")
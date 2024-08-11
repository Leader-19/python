#question and answer
import random
question = ['Who is mark zuckerberge?', 'Who is elon musk?']

answer = ['facebook ceo', 'space ceo']

user_poin = 0
marchin_poin = 0

index = 1
for q in question:
    print(q)
    num = 1
    for a in answer:
        print(str(num) + " . " + a)
        num += 1
    user_answer = input("Please pick answer!: ")

    if (user_answer == str(index)):
        user_poin += 1
    else:
        marchin_pick = random.choice(answer)
        if marchin_pick == answer[index]:
            marchin_poin += 1
    index += 1
print("user_poin is =" + str(user_poin))
print("marchin_poin is =" + str(marchin_poin))
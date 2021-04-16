#SABA SYED
#03/21/2020


import sys
print ("Are You Bert or Are You Ernie?????? Answer these questions BELOW to find out!")
QuestionsList =  [
    ('How many legs on a Cat?',
    ['A) One', 'B) Two', "C) Three", 'D) Four'],
    ['d','D','4']),

    ('How many Wonders of the World are there?',
    ['A) Two', 'B) Four', "C) Six ", 'D) Twenty'],
    ['c', 'C', '3']),

    ('What is the tallest mammal?',
    ['A) Moose', 'B) Giraffe', 'C) Sea Turtle', 'D) Hyena'],
    ['B', 'b', '2', 'Giraffe', 'giraffe']),

    ('Which city is the home of Batman?',
    ['A) Newark ', 'B) New York City', "C) Pacific Ocean", 'D) Gotham'],
    ['d', 'D', '4', 'Gotham','gotham']),

    ('Spinach is high in which mineral?',
    ['A) Iron', 'B) Oxygen', 'C) Acid', 'D) Potassium'],
    ['1', 'A', 'a','Iron', 'iron']),

    ('What is the chemical symbol for Oxygen?    ',
    ['A) O2Cl', 'B) O2H2 ', "C) O", 'D) OPh'],
    ['c', 'C', '3','O']),

    ('How many wheels on a bicycle?',
    ['A) One','B) Two', 'C) Three', 'D)Four'],
    ['B','b','2']),

    ('What color is the circle on the Japanese national flag?',
    ['A) Blue', 'B) Black', "C) Red", 'D) Yellow'],
    ['c', 'C', '3', 'O']),

    ('What color is a swan in Italy?',
    ['A) White', 'B) Black', 'C) Pink', 'D) Purple'],
    ['1', 'A', 'a']),

    ('What color is not in the United States Flag?',
    ['A) Blue', 'B) White', "C) Red", 'D) Purple'],
    ['d', 'D', '4', 'Red', 'red']),

  ]
def questions():
    wrong = 0
    right = 0

right = 0
wrong = 0
for each_question, each_answer, each_correct_answer in QuestionsList:

        print(each_question + '\n' + ' '.join(each_answer))
        get_answer = input()

        if get_answer in each_correct_answer:
            print('WOW! Correct and Keep Going \n')
            right += 1
        else:
            print('YOU ARE WRONG!\n')
            wrong += 1
        print('You answered correctly to {0} questions and incorrectly to {1}.'.format(right, wrong))
if (right < 5):
    print ("You are Ernie!")
else:
    print ("You are Bert!")

# I got from stack exchange
if __name__ == '__main__':
    questions()

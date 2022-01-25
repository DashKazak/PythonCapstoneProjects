""" This is a quiz program refactored by Daria Kazak, January 23rd 2022. This program provides the user
with option to take one of 2 quizzes and go through the questions collecting points.   """

def quiz_check(Dict,topic,total_score):
    """"This is a function that checks the answers to be correct and calculates the total score. It takes eaither of the dictionaries, total_score and topic as parameter."""
    for key,value in Dict.items():
        print(key)
        user_answer = input('Enter your answer: ')   
        if value.lower() == user_answer.lower():
            print('Correct!')
            total_score += 1
                
                
        else:
            print(f'Sorry, the answer is {value} ')

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of 3.')

    if total_score == len(Dict[key]): #length of the keys in the dictionary instead on number 3
        print('You got all the answers correct!')
"""the rest of the quiz (the topics and questions) are in main. Questions and asnwers are sorted in dictionaries according to a topic."""
def main():
    total_score = 0

    topic = input('Would you like art, or space questions? Enter art for art and space for space:')

    if topic == 'art':
        Dict = {'Who painted the Mona Lisa?':'Leonardo Da Vinci','What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli','Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'Chicago'}
        #function call
        quiz_check(Dict,topic,total_score)
        

    elif topic == 'space':
        Dict = {'Which planet is closest to the sun?':'Mercury','Which planet spins in the opposite direction to all the others in the solar system?': 'Venus','How many moons does Mars have?': '2'}
        #function call
        quiz_check(Dict,topic,total_score)
        

    else:
        print('That is not a valid topic.')

main()

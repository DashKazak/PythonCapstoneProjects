""" This is a quiz program refactored by Daria Kazak, January 23rd 2022. This program provides the user
with option to take one of 2 quizzes and go through the questions collecting points.   """

def quiz_check(questions, topic, total_score):  # avoid names like 'Dict' which can be confused with built-in python names like dict, 
    # it's better to use a variable name that describes the data that is stored in the dictionary 
    """"This is a function that checks the answers to be correct and calculates the total score. It takes eaither of the dictionaries, total_score and topic as parameter."""
    
    for question, answer in questions.items():  # key, value - can you be more specfic with the names? 
        print(question)
        user_answer = input('Enter your answer: ')   
        if answer.lower() == user_answer.lower():
            print('Correct!')
            total_score += 1   
        else:
            print(f'Sorry, the answer is {answer} ')

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of 3.')

    if total_score == len(questions): # can simplify, len() works on the dictionary object and counts the number of key-value pairs in the dictionary 
        print('You got all the answers correct!')

"""the rest of the quiz (the topics and questions) are in main. Questions and asnwers are sorted in dictionaries according to a topic."""
def main():
    total_score = 0  # this is never used here and always 0 - could quiz_check set it?

    # how would you handle more topics? 
    topic = input('Would you like art, or space questions? Enter art for art and space for space:')

    if topic == 'art':
        questions = {  # can use multiple lines if preferred, can be easier to read 
            'Who painted the Mona Lisa?': 'Leonardo Da Vinci',
            'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli',
            'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'Chicago'
            }
        #function call
        quiz_check(questions, topic, total_score)  # python convention is to put a space after the comma, it's a little easier to read the individual arguments
        

    elif topic == 'space':
        Dict = {'Which planet is closest to the sun?':'Mercury','Which planet spins in the opposite direction to all the others in the solar system?': 'Venus','How many moons does Mars have?': '2'}
        #function call
        quiz_check(questions, topic, total_score)
        

    else:
        print('That is not a valid topic.')

main()

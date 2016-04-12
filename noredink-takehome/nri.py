#!/usr/bin/python

import csv
import random

def user_question_prompt():
    # prompt user for how many questions they want in the quiz,
    # accept anything more than 0, pass back out.

    question_count = int(raw_input("Please input the number of questions you would like to answer: "))
    if question_count == 0:
        print("0 is not sadly not accepted!")
        user_question_prompt()
    elif question_count == 1:
        print("Thanks! I'm putting together {0} question now.".format(question_count))
    else:
        print("Thanks! I'm putting together {0} questions now.".format(question_count))
    return(question_count)


def pull_csv_data(num_questions):
# Display question IDs based on strand values

    assigned_question_id = []
    strand_question_dict = {}
    
    with open('questions.csv', 'rb') as csv_questions:
        questions_reader = csv.DictReader(csv_questions)
        for row in questions_reader:
            strand_question_dict['question ' + row['question_id']] = row['strand_id']
    print(strand_question_dict)

    last_pick = 0 #set a value on last pick, doesn't really matter what int.

    for num in range(num_questions):
        
        picked_question = (random.sample(strand_question_dict, 1))
        while strand_question_dict[picked_question[0]] == last_pick:
            picked_question = (random.sample(strand_question_dict, 1))
        last_pick = strand_question_dict[picked_question[0]]
        assigned_question_id.append(picked_question)



    print(assigned_question_id)

'''
# This seciont will be for bonus requirements if we make it there.

    with open('usage.csv', 'rb') as csv_usage:
        usage_reader = csv.DictReader(csv_usage)
'''
    
num_questions = user_question_prompt()
pull_csv_data(num_questions)

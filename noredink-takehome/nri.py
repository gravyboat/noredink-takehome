#!/usr/bin/python

import csv
import random

def user_question_prompt():
    """
    Prompt user for how many questions they want in the quiz,
    Accept anything more than 0, pass back out.
    """

    question_count = int(raw_input("Please input the number of questions you would like to answer: "))
    # Should probably consider fixing the above to handle non int values.
    if question_count == 0:
        print("Sadly 0 is not accepted!")
        user_question_prompt()
    else:
        print("Thanks! I'm putting together {0} question(s) now.".format(question_count))
    return(question_count)


def pull_csv_data(num_questions):
    """Display question IDs based on strand values."""

    assigned_question_id = []
    strand_question_dict = {}
    
    with open('questions.csv', 'rb') as csv_questions:
        questions_reader = csv.DictReader(csv_questions)
        for row in questions_reader:
            strand_question_dict['question ' + row['question_id']] = row['strand_id']

    last_pick = random.choice([1, 2]) # Set a value on last pick randomly.

    for num in range(num_questions):
        # Set the pick to random to begin with.
        picked_question = (random.sample(strand_question_dict, 1))
        # Use a while loop to ensure we don't pick the same strand value.
        while strand_question_dict[picked_question[0]] == last_pick:
            picked_question = (random.sample(strand_question_dict, 1))
        # Assign our last_pick value so we avoid strand repetition.
        last_pick = strand_question_dict[picked_question[0]]
        assigned_question_id.append(picked_question)
        
        # Missing the standard matching an equal number of times.

    print("please complete the following questions:")
    for question in assigned_question_id:
        print(question[0])

'''
    # This section will be for bonus requirements if we make it there.

    with open('usage.csv', 'rb') as csv_usage:
        usage_reader = csv.DictReader(csv_usage)
'''


num_questions = user_question_prompt()
pull_csv_data(num_questions)

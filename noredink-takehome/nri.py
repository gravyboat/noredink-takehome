import csv

def user_question_prompt():
    # prompt user for how many questions they want in the quiz,
    # accept anything more than 0
    question_count = raw_input("Please input the number of questions you would like to answer: ")
    if question_count == 0:
        print("0 is not sadly not accepted!")
        user_question_prompt()
    elif question_count == 1:
        print("Thanks! I'm putting together {0} question now.".format(question_count))
    else:
        print("Thanks! I'm putting together {0} questions now.".format(question_count))
    return(question_count)

    # Display question IDs based on strand values

def pull_csv_data(num_questions):

    with open('questions.csv', 'rb') as csv_questions:
        questions_reader = csv.DictReader(csv_questions)


    with open('usage.csv', 'rb') as csv_usage:
        usage_reader = csv.DictReader(csv_usage)
    
num_questions = user_question_prompt()
pull_csv_data(num_questions)

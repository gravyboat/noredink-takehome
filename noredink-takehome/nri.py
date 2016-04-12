import csv


def read_in_csvs():

    with open('questions.csv', 'rb') as csv_questions:
        questions_reader = csv.reader(csv_questions, delimiter=',')
        for row in questions_reader:
            print(','.join(row))


    with open('usage.csv', 'rb') as csv_usage:
        usage_reader = csv.DictReader(csv_usage)
        for row in usage_reader:
            print(row['student_id'])

def user_question_prompt():
    # prompt user for how many questions they want in the quiz,
    # accept anything more than 0
    question_count = raw_input("Please input the number of questions: ")
    if question_count == 0:
        print("0 is not accepted!")
        user_question_prompt()
    else:
        print("Thanks! I'm putting {0} questions together now.".format(question_count))

    # Display question IDs

user_question_prompt()

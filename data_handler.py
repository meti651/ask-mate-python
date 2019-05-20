import connection


def get_story_by_id(filename, id):


def get_answers_by_question_id(filename, q_id):


def get_max_id(is_answer=True):


def sort_questions(question_list, attribute, order_direction):


def get_question_id_by_answer_id(answer_id, filename="sample_data/answer.csv"):



def delete_by_id(filename, key, delete_id, fieldnames):


def count_vote(filename, id, vote_type, fieldnames):

@connection.connection_handler
def insert_question_to_database(cursor, submission_time, view_number, vote_number, title, message, image):
    cursor.execute("""
                    INSERT INTO question
                    (submission_time, view_number, vote_number, title, message, image)
                    VALUES (%s, %s, %s, %s, %s, %s);""",
                   (submission_time, view_number, vote_number, title, message, image))

@connection.connection_handler
def insert_question_to_database(cursor, submission_time, view_number, question_id, message, image):
    cursor.execute("""
                    INSERT INTO answer
                    (submission_time, view_number, question_id message, image)
                    VALUES (%s, %s, %s, %s, %s);""",
                   (submission_time, view_number, question_id, message, image))

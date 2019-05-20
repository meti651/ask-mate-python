import connection


@connection.connection_handler
def get_last_5_questions_title(cursor, sort_by, direction):
    cursor.execute("""
                    SELECT title FROM question
                    ORDER BY %(sort_by)s %(direction)s
                    LIMIT 5;
                    """,
                   {'sort_by': sort_by, 'direction': direction})
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def get_all_questions_title(cursor, sort_by, direction):
    cursor.execute("""
                        SELECT title FROM question
                        ORDER BY %(sort_by)s %(direction)s;
                        """,
                   {'sort_by': sort_by, 'direction': direction})
    questions = cursor.fetchall()
    return questions

@connection.connection_handler
def get_question_n_answers_by_question_id(cursor, id):
    cursor.execute("""
                    SELECT * FROM question
                    JOIN answer ON question.id = answer.question_id
                    WHERE id == id;
                    """,
                   {'id': id})
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def delete_question(cursor, id):
    cursor.execute("""
                    DELETE FROM question
                    WHERE id = %(id)s
                    """,
                   {'id': id})




def get_question_id_by_answer_id(answer_id, filename="sample_data/answer.csv"):



def delete_by_id(filename, key, delete_id, fieldnames):


def count_vote(filename, id, vote_type, fieldnames):


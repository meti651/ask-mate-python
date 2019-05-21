import connection
from psycopg2 import sql


@connection.connection_handler
def get_question_by_id(cursor, id):
    cursor.execute(
        """
        SELECT * FROM question WHERE id = %(id)s;
        """, {'id':int(id)})

    question = cursor.fetchall()
    return question[0]



@connection.connection_handler
def edit_questions(cursor, id, title, message, image):
    cursor.execute(
        """
        UPDATE question
        SET title = %(title)s, message = %(message)s, image = %(image)s
        WHERE id = %(id)s;
        """, {'title': title, 'id': int(id), 'message': message, 'image': image})


@connection.connection_handler
def get_last_5_questions(cursor, sort_by, direction):
    if direction.upper() == "ASC":
        cursor.execute(sql.SQL("""
                               SELECT * FROM question
                               ORDER BY {sort_by} ASC
                               LIMIT 5;
                               """
                               ).format(sort_by=sql.Identifier(sort_by)),
                       {'sort_by': sort_by})
    else:
        cursor.execute(sql.SQL("""
                                       SELECT * FROM question
                                       ORDER BY {sort_by} DESC
                                       LIMIT 5;
                                       """
                               ).format(sort_by=sql.Identifier(sort_by)),
                       {'sort_by': sort_by})

    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def get_all_questions(cursor, sort_by, direction):
    if direction == "ASC":
        cursor.execute(sql.SQL("""
                            SELECT * FROM question
                            ORDER BY {sort_by} ASC;
                            """
                            ).format(sort_by=sql.Identifier(sort_by)),
                       {'sort_by': sort_by})
    else:
        cursor.execute(sql.SQL("""
                                    SELECT * FROM question
                                    ORDER BY {sort_by} DESC;
                                    """
                               ).format(sort_by=sql.Identifier(sort_by)),
                       {'sort_by': sort_by})

    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def get_question_by_id(cursor, id):
    cursor.execute("""
                    SELECT * FROM question
                    WHERE id = %(id)s;
                    """,
                   {'id': int(id)})
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def get_answers_by_question_id(cursor, question_id):
    cursor.execute("""
                    SELECT * FROM answer
                    WHERE question_id = %(question_id)s;
                    """,
                   {'question_id': question_id})
    answers = cursor.fetchall()
    return answers


@connection.connection_handler
def delete_question(cursor, id):
    cursor.execute("""
                    DELETE FROM question
                    WHERE id = %(id)s
                    """,
                   {'id': id})


@connection.connection_handler
def insert_data_to_question(cursor, submission_time, view_number, vote_number, title, message, image):
    cursor.execute("""
                    INSERT INTO question
                    (submission_time, view_number, vote_number, title, message, image)
                    VALUES (%s, %s, %s, %s, %s, %s);""",
                   (submission_time, view_number, vote_number, title, message, image))

@connection.connection_handler
def insert_data_to_answer(cursor, submission_time, view_number, question_id, message, image):
    cursor.execute("""
                    INSERT INTO answer
                    (submission_time, view_number, question_id message, image)
                    VALUES (%s, %s, %s, %s, %s);""",
                   (submission_time, view_number, question_id, message, image))


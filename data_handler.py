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
def get_answer_by_id(cursor, id):
    cursor.execute("""
                    SELECT * FROM question
                    WHERE id = %(id)s;
                    """,
                   {'id': int(id)})
    answers = cursor.fetchall()
    return answers


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
def delete(cursor, id, table):
    cursor.execute(sql.SQL("""
                    DELETE FROM {table}
                    WHERE id = %(id)s;
                    """).format(table=sql.Identifier(table)),
                   {'id': int(id)})


@connection.connection_handler
def insert_data_to_question(cursor, new_question):
    submission_time = new_question['submission_time']
    view_number = new_question['view_number']
    vote_number = new_question['vote_number']
    title = new_question['title']
    message = new_question['message']
    image = new_question['image']
    cursor.execute("""
                    INSERT INTO question
                    (submission_time, view_number, vote_number, title, message, image)
                    VALUES (%s, %s, %s, %s, %s, %s);""",
                   (submission_time, view_number, vote_number, title, message, image))

@connection.connection_handler
def insert_data_to_answer(cursor, answer):
    submission_time = answer['submission_time']
    vote_number = answer['vote_number']
    question_id = answer['question_id']
    message = answer['message']
    image = answer['image']
    cursor.execute("""
                    INSERT INTO answer
                    (submission_time, vote_number, question_id, message, image)
                    VALUES (%s, %s, %s, %s, %s);""",
                   (submission_time, vote_number, question_id, message, image))


@connection.connection_handler
def count_vote(cursor, story_type, id, vote_type):
    if vote_type == "vote-up":
        point = 1
    else:
        point = -1
    cursor.execute(sql.SQL("""
                    UPDATE {story_type}
                    SET vote_number = vote_number + %(point)s
                    WHERE id = %(id)s;
                   """).format(story_type = sql.Identifier(story_type)),
                   {'point': int(point),
                    'id': int(id)})
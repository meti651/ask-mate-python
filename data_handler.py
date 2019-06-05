import connection
from psycopg2 import sql


@connection.connection_handler
def get_question_by_id(cursor, id):
    cursor.execute(
        """
        SELECT * FROM question WHERE id = %(id)s;
        """, {'id':int(id)})

    question = cursor.fetchall()
    return question


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
                   {'id': id})
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def get_answer_by_id(cursor, id):
    cursor.execute("""
                    SELECT * FROM answer
                    WHERE id = %(id)s;
                    """,
                   {'id': int(id)})
    answers = cursor.fetchall()
    return answers


@connection.connection_handler
def get_answers_by_question_id(cursor, question_id):
    cursor.execute("""
                    SELECT * FROM answer
                    WHERE question_id = %(question_id)s
                    ORDER BY submission_time;
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
def insert_data_to_answer(cursor, submission_time, question_id, message, image):
    cursor.execute("""
                    INSERT INTO answer
                    (submission_time,  question_id, message, image)
                    VALUES (%s, %s, %s, %s, %s);""",
                   (submission_time, question_id, message, image))


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
def get_question_tags(cursor, q_id):
    cursor.execute("""
                    SELECT id, name FROM question_tag
                    INNER JOIN tag ON question_tag.tag_id = tag.id
                    WHERE question_id = %(q_id)s;""", {'q_id': int(q_id)})

    question_tags = cursor.fetchall()
    return question_tags

@connection.connection_handler
def add_question_tag(cursor, tag_name):
    cursor.execute("""
                    INSERT INTO tag (name)
                    VALUES (%(tag_name)s);""", {'tag_name': tag_name})


@connection.connection_handler
def get_tag_id(cursor, tag_name):
    cursor.execute("""
                    SELECT id FROM tag
                    WHERE name = %(tag_name)s;""", {'tag_name': tag_name})
    tag_id = cursor.fetchall()
    return tag_id[0]

@connection.connection_handler
def delete_tag(cursor, question_id, tag_id):
    cursor.execute("""
                    DELETE FROM question_tag
                    WHERE question_id = %(question_id)s
                    AND tag_id = %(tag_id)s;
                    """,
                   {'question_id': int(question_id), 'tag_id': int(tag_id)})


@connection.connection_handler
def add_tag_to_question(cursor, tag_id, question_id):
    cursor.execute("""
                    INSERT INTO question_tag (question_id, tag_id)
                    VALUES (%s, %s);""", (question_id, tag_id))


@connection.connection_handler
def get_all_tag(cursor):
    cursor.execute("""
                    SELECT name FROM tag;""")
    tags = cursor.fetchall()
    return tags

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


@connection.connection_handler
def increase_view_number(cursor, id):
    cursor.execute(
        """
        UPDATE question
        SET view_number = view_number + 1
        WHERE id = %(id)s;
        """, {'id': int(id)})


@connection.connection_handler
def edit_answer(cursor, id, message, image):
    cursor.execute(
        """
        UPDATE answer
        SET message = %(message)s, image = %(image)s
        WHERE id = %(id)s;
        """, {'id': int(id), 'message': message, 'image': image})


@connection.connection_handler
def get_items_by_search_result(cursor, search_data):
    cursor.execute("""
                SELECT title, id FROM question
                WHERE title LIKE %(search_data)s 
                    OR message LIKE %(search_data)s;""", {'search_data': '%' + search_data + '%'})
    datas = cursor.fetchall()
    print(datas)
    return datas


@connection.connection_handler
def mark_answer(cursor, answer_id, is_marked):
    cursor.execute(
        """
               UPDATE answer
               SET is_marked = %(is_marked)s 
               WHERE id = %(answer_id)s;
               """, {'id': int(answer_id), 'is_marked': is_marked})




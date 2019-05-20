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

"""
sql.SQL('UPDATE question SET title = {title}, message = {message}, image = {image} WHERE id = {id}')
            .format(title=sql.Identifier(title), message=sql.Identifier(message),
                    image=sql.Identifier(image), id=sql.Identifier(id))
"""


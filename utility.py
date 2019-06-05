import data_handler
import bcrypt
import datetime


def increase_view_number(question_id):
    question = data_handler.get_question_by_id(question_id)
    view_number = question[0]['view_number']
    return view_number + 1


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


def match_password(password, check):
    if password == check:
        return True
    else:
        return False


def insert_data(user):
    new_user = {}
    for key in user.keys():
        new_user[key] = user[key]
    new_user["registration_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_user["password"] = hash_password(user["password"])
    return new_user


def pw_checker(password):
    special_chars = ['@', '!', '#', '$', '%']
    valid_pw = True

    if len(password) <= 6:
        valid_pw = False
    if not any(char.isdigit() for char in password):
        valid_pw = False
    if not any(char.islower() for char in password):
        valid_pw = False
    if not any(char.isupper() for char in password):
        valid_pw = False
    if not any(char in special_chars for char in password):
        valid_pw = False

    return valid_pw


def match_question_session(session, question_id):
    question = data_handler.get_question_by_id(question_id)
    if session == question[0]['username']:
        return True
    return False


def match_answer_session(session, answer_id):
    answer = data_handler.get_question_by_id(answer_id)
    if session == answer[0]['username']:
        return True
    return False


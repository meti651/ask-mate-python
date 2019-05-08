import connection

ANSWER_KEYS = ['id','submission_time','vote_number','question_id','message','image']
QUESTION_KEYS = ['id','submission_time','view_number','vote_number','title','message','image']


def get_story_by_id(filename, id):
    datas = connection.read_data(filename)
    for data in datas:
        if data['id'] == id:
            return data

def get_answers_by_question_id(filename, q_id):
    datas = connection.read_data(filename)
    answers = []
    for data in datas:
        if data['question_id'] == q_id:
            answers.append(data)
    return answers
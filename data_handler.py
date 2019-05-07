import connection

ANSWER_KEYS = ['id','submission_time','vote_number','question_id','message','image']
QUESTION_KEYS = ['id','submission_time','view_number','vote_number','title','message','image']


def get_story_by_id(filename, id):
    datas = connection.read_data(filename)
    for data in datas:
        if data['id'] == id:
            return data
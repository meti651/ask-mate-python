import connection

ANSWER_KEYS = ['id','submission_time','vote_number','question_id','message','image']
QUESTION_KEYS = ['id','submission_time','view_number','vote_number','title','message','image']
MAX_ID_KEYS = ["question_max_id", "answer_max_id"]


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

def get_max_id(is_answer=True):
    record = connection.read_data("/sample_data/max_id_s.csv")
    if is_answer:
        max_id = int(record["answer_id"])
        max_id += 1
        record["answer_id"] = max_id
    else:
        max_id = int(record["question_id"])
        max_id += 1
        record["question_id"] = max_id


    connection.write_data("/sample_data/max_id_s.csv", MAX_ID_KEYS)
    return str(max_id)
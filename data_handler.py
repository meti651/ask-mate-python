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
    reader = connection.read_data("sample_data/max_id_s.csv")
    numbers = {}
    for row in reader:
        for key in MAX_ID_KEYS:
            numbers[key] = row[key]
    if is_answer:
        max_id = int(numbers["answer_max_id"])
        max_id += 1
        numbers["answer_max_id"] = max_id
    else:
        max_id = int(numbers["question_max_id"])
        max_id += 1
        numbers["question_max_id"] = max_id
    record = [numbers]
    connection.write_data("sample_data/max_id_s.csv", MAX_ID_KEYS, record)
    return str(max_id)

def sort_questions(question_list, attribute, order_direction):
    if order_direction == 'asc':
        sorted_questions = sorted(question_list, key=lambda k: k[attribute])
    else:
        sorted_questions = sorted(question_list, key=lambda k: k[attribute], reverse=True)
    return sorted_questions

def get_question_id_by_answer_id(answer_id, filename="sample_data/answer.csv"):
    answers = connection.read_data(filename)
    for answer in answers:
        if answer["id"] == answer_id:
            return answer["question_id"]


def delete_by_id(filename, key, delete_id, fieldnames):
    datas = connection.read_data(filename)
    results = []
    for data in datas:
        if data[key] == delete_id:
            continue
        results.append(data)
    connection.write_data(filename, fieldnames, reversed(results))
>>>>>>> db137d85a3b6ff8292668ca20c55fc4358b609e2

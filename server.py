from flask import Flask, render_template, request, redirect, url_for
import connection

ANSWER_KEYS = ['id','submission_time','vote_number','question_id','message','image']
QUESTION_KEYS = ['id','submission_time','view_number','vote_number','title','message','image']

app = Flask(__name__)

@app.route('/list')
def route_list():
    questions = connection.read_data('sample_data/question.csv')
    return render_template('list.html', questions=questions, q_keys=QUESTION_KEYS)














if __name__ == "__main__":
    app.run(debug=True)

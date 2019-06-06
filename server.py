import datetime
import utility
from flask import Flask, render_template, request, redirect, url_for, session

import data_handler

app = Flask(__name__)
app.secret_key = '�p����%aYHҀ��'


@app.route("/", methods=('GET', 'POST'))
def route_list():
    questions = data_handler.get_last_5_questions('submission_time', 'DESC')
    if 'username' in session:
        if request.method == 'POST':
            attribute = request.form['attribute']
            reverse = request.form['order_direction'].upper()
            sorted_questions = data_handler.get_last_5_questions(attribute, reverse)
            return render_template('list.html',
                                   questions=sorted_questions,
                                   attribute=attribute,
                                   reverse=reverse,
                                   method='last',
                                   session=True
                                   )
        return render_template('list.html',
                               questions=questions,
                               method='last',
                               session=session['username']
                               )
    return render_template('list.html',
                           questions=questions,
                           method='last',
                           session=False
                           )


@app.route('/list', methods=('POST', 'GET'))
def list_all_question():
    questions = data_handler.get_all_questions('submission_time', 'DESC')
    if 'username' in session:
        if request.method == 'POST':
            attribute = request.form['attribute']
            reverse = request.form['order_direction'].upper()
            sorted_questions = data_handler.get_all_questions(attribute, reverse)
            return render_template('list.html',
                                   questions=sorted_questions,
                                   attribute=attribute,
                                   reverse=reverse,
                                   method='all',
                                   session=True)
        return render_template('list.html',
                               questions=questions,
                               method='all',
                               session=session['username']
                               )
    return render_template('list.html',
                           questions=questions,
                           method='all',
                           session=False
                           )


@app.route('/question/<int:question_id>')
def display_question(question_id):
    data_handler.increase_view_number(question_id)
    displayed_question = data_handler.get_question_by_id(question_id)
    displayed_answers = data_handler.get_answers_by_question_id(question_id)
    displayed_tags = data_handler.get_question_tags(question_id)
    if 'username' in session:
        return render_template('question.html',
                               question=displayed_question[0],
                               answers=displayed_answers,
                               tags=displayed_tags,
                               session=session['username']
                               )
    return render_template('question.html',
                           question=displayed_question[0],
                           answers=displayed_answers,
                           tags=displayed_tags,
                           session=False)


@app.route('/add_question', methods=('GET', 'POST'))
def ask_question():
    if 'username' in session:
        if request.method == "POST":
            new_question = {}
            for key in request.form.keys():
                new_question[key] = request.form[key]
            new_question["view_number"] = 0
            new_question["vote_number"] = 0
            new_question["submission_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_question['user_name'] = session['username']
            data_handler.insert_data_to_question(new_question)
            return redirect("/")
        return render_template("add_question.html", mode="add-question")
    return render_template("404.html"), 404


@app.route('/question/<int:question_id>/edit', methods=('GET', 'POST'))
def edit_question(question_id):
    is_matching = utility.match_question_session(session['username'], question_id)
    if is_matching:
        question_params = data_handler.get_question_by_id(question_id)
        if request.method == "POST":
            data_handler.edit_questions(question_id,
                                        request.form['title'],
                                        request.form['message'],
                                        request.form['image'])
            return redirect('/question/' + str(question_params[0]['id']))
        return render_template('add_question.html',
                               question_params=question_params[0],
                               mode="edit-question")
    return render_template("404.html"), 404


@app.route("/question/<int:question_id>/delete")
def delete_question(question_id):
    is_matching = utility.match_question_session(question_id)
    if is_matching:
        data_handler.delete(question_id, 'question')
        return redirect("/")
    return render_template("404.html"), 404


@app.route('/question/<int:question_id>/new_answer', methods=['GET', 'POST'])
def add_new_answer(question_id):
    if 'username' in session:
        if request.method == 'POST':
            new_answer = {}
            for key in request.form.keys():
                new_answer[key] = request.form[key]
            new_answer['submission_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_answer['vote_number'] = 0
            new_answer['question_id'] = question_id
            new_answer['user_name'] = session['username']
            data_handler.insert_data_to_answer(new_answer)
            return redirect('/question/' + str(question_id))
        return render_template('answer.html', question_id=question_id, mode='add-answer')
    return render_template("404.html"), 404


@app.route('/answer/<int:answer_id>/edit', methods=['GET', 'POST'])
def edit_answer(answer_id):
    is_matching = utility.match_answer_session(session['username'], answer_id)
    if is_matching:
        answer_params = data_handler.get_answer_by_id(answer_id)
        if request.method == "POST":
            data_handler.edit_answer(answer_id, request.form['message'], request.form['image'])
            return redirect('/question/' + str(answer_params[0]['question_id']))
        return render_template('answer.html', question_params=answer_params[0], mode='edit-answer')
    return render_template("404.html"), 404


@app.route('/answer/<int:answer_id>/delete')
def delete_an_answer(answer_id):
    query_string = request.referrer
    data_handler.delete(answer_id, 'answer')
    return redirect(query_string)


@app.route('/question/<question_id>/new-tag', methods=['GET', 'POST'])
def add_new_tag(question_id):
    is_matching = utility.match_answer_session(session['username'], question_id)
    if is_matching:
        if request.method == 'POST':
            curr_link = request.referrer
            new_tag = request.form['create_tag']
            selected_tag = request.form['selected_tag']
            if new_tag:
                try:
                    data_handler.add_question_tag(new_tag)
                except:
                    pass
                return redirect(curr_link)
            else:
                try:
                    tag_id = data_handler.get_tag_id(selected_tag)['id']
                    data_handler.add_tag_to_question(tag_id, question_id)
                except:
                    return redirect(curr_link)
                return redirect(url_for('display_question', question_id=question_id))
        question_tag = data_handler.get_all_tag()
        return render_template('new_tag.html',
                               question_id=question_id,
                               tags=question_tag,
                               mode='add-tag')
    return render_template("404.html"), 404


@app.route('/<story_type>/<int:id>/<vote_type>')
def vote(story_type, id, vote_type):  # story_type: 'question' or 'answer', vote_type: 'vote-up' or 'vote-down'
    if 'username' in session:
        query_string = request.referrer
        data_handler.count_vote(story_type, id, vote_type)
        user_id = data_handler.get_user_id(id, story_type)
        data_handler.change_reputation(user_id[0]['user_id'], vote_type, story_type)
        return redirect(query_string)
    return render_template(""), 404



@app.route('/question/<int:question_id>/tag/<int:tag_id>')
def delete_tag(question_id, tag_id):
    is_matching = utility.match_answer_session(session['username'], question_id)
    if is_matching:
        data_handler.delete_tag(question_id, tag_id)
        return_route = request.referrer
        return redirect(return_route)
    return render_template("404.html"), 404


@app.route('/search', methods=['GET', 'POST'])
def get_searched_result():
    search_data = request.args.get('q')
    result = data_handler.get_items_by_search_result(search_data)
    return render_template('search.html', result=result)


@app.route("/registration", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        try:
            is_matching = utility.match_password(request.form["password"], request.form["check"])
            if is_matching:
                validate_pw = utility.pw_checker(request.form["password"])
                if validate_pw:
                    user = utility.insert_data(request.form)
                    data_handler.insert_user(user)
                    return redirect("/")
                else:
                    return render_template("registration.html",
                                           errorcode='failed_password')
            else:
                return render_template("registration.html", errorcode="Password doesn't match")
        except:
            return render_template("registration.html", errorcode="Username is already in use")
    return render_template("registration.html", errorcode='', registration='registration')


@app.route("/login", methods=("GET", "POST"))
def login_user():
    if request.method == "POST":
        user = data_handler.get_user(request.form["username"])
        is_matching = utility.verify_password(request.form["password"], user[0]["password"])
        if is_matching:
            session['username'] = request.form["username"]
            return redirect("/")
    return render_template("login.html", login='login')


@app.route("/logout")
def logout_user():
    session.pop("username", None)
    return redirect("/")


@app.route("/tags")
def list_tags():
    tags = data_handler.list_tags_and_their_usage_number()
    return render_template("tags.html", tags=tags)


@app.route("/tags/question/<tag_name>")
def list_questions_by_tag_name(tag_name):
    questions = data_handler.get_question_by_tag(tag_name)
    return render_template("tag_question.html", questions=questions)


@app.route("/users")
def show_users():
    users = data_handler.get_all_users()
    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=9992
    )

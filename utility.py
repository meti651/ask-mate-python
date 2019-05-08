import datetime


def get_submission_time():
    current_date = datetime.datetime.now()
    result = ""
    result += str(current_date.year)
    result += str(current_date.month)
    result += str(current_date.day)
    result += str(current_date.hour)
    result += str(current_date.minute)
    result += str(current_date.second)
    return result

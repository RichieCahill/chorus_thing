from flask import Blueprint

event_page = Blueprint("event_page",__name__)

@event_page.route("/event/")
def add_event():
    return "0"

@event_page.route("/event/")
def get_event():
    return "0"

@event_page.route("/event/")
def update_event():
    return "0"

@event_page.route("/event/")
def delete_event():
    return "0"
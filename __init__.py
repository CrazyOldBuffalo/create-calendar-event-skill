from mycroft import MycroftSkill, intent_file_handler


class CreateCalendarEvent(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('event.calendar.create.intent')
    def handle_event_calendar_create(self, message):
        self.speak_dialog('event.calendar.create')


def create_skill():
    return CreateCalendarEvent()


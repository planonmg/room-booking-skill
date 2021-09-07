from mycroft import MycroftSkill, intent_file_handler


class RoomBooking(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('booking.room.intent')
    def handle_booking_room(self, message):
        amount = message.data.get('amount')
        building = message.data.get('building')
        time = message.data.get('time')

        self.speak_dialog('booking.room', data={
            'time': time,
            'amount': amount,
            'building': building
        })


def create_skill():
    return RoomBooking()


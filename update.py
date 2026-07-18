from db_config import Message
from read_all import display_all_message


def update_message():
    msg = Message.get_by_id(3)
    msg.user = "Tom Cruise"
    msg.save()


if __name__ == "__main__":
    display_all_message()

    update_message()

    display_all_message()

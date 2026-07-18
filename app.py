from db_config import Message


def delete_message():
    msg_id = input("削除するメッセージのIDを入力してください > ")
    # 存在しないIDが入力された場合のエラー処理
    try:
        msg = Message.get_by_id(msg_id)
    except Message.DoesNotExist:
        print("該当するメッセージが見つかりません。IDを再度確認してください。")
        return
    msg.delete_instance()


def edit_message():
    msg_id = input("編集するメッセージのIDを入力してください > ")
    try:
        msg = Message.get_by_id(msg_id)
    except Message.DoesNotExist:
        print("該当するメッセージが見つかりません。IDを再度確認してください。")
        return
    print(f"{msg.id} {msg.user} {msg.content} {msg.pub_date}")
    msg.content = input("新しいメッセージを入力してください > ")
    msg.save()


def main():
    user_name = input("ユーザー名を入力してください > ")

    while True:
        for msg in Message.select():
            print(f"{msg.id} {msg.user} {msg.content} {msg.pub_date}")

        message = input("メッセージを入力してください > ")

        if message == "\\q":
            break  # ブロックを抜ける

        if message == "\\d":
            delete_message()
            continue  # 以降の処理をスキップして次のループに移る

        if message == "\\e":
            edit_message()
            continue

        Message.create(user=user_name, content=message)


if __name__ == "__main__":
    main()

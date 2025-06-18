import json


def moderate_messages():

    bad_words = input("Enter bad words (separated by space): ").split()
    tmp = None
    with open("messages.json", 'r') as file:
        tmp = json.load(file)

    for item in tmp:
        if item.get('message'):
            words = item.get('message').split()
            for word in words:
                if word in bad_words:
                    item['message'] = item['message'].replace(word, '***')


    with open("messages.json", 'w') as file:
        json.dump(tmp, file, indent=4)

    print("Bad words removed. File saved.")

# ✅ Задача 3: Модерация сообщений в Telegram
# Реализуй функцию moderate_messages(). Считай сообщения из файла messages.json (список словарей).
# Удали сообщения, содержащие запрещённые слова (например, 'плохой', 'spam').
# Перезапиши файл без нарушений.


if __name__ == "__main__":
    moderate_messages()

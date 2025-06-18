# Главное меню проекта Social Media Platform

from app import posts, users, messages, channels, analytics, followers, login, echo_bot, friends

def show_menu():
    print("\nДобро пожаловать в Social Media Platform!")
    print("1. Добавить пост")
    print("2. Зарегистрировать пользователя")
    print("3. Модерировать сообщения")
    print("4. Управлять подписчиками")
    print("5. Создать канал")
    print("6. Отправить сообщение")
    print("7. Войти в аккаунт")
    print("8. Поиск друзей")
    print("9. Эхо-бот")
    print("10. Аналитика по постам")
    print("0. Выход")

def main():
    while True:
        show_menu()
        choice = input("Выберите опцию: ")
        if choice == "0":
            break
        elif choice == "1":
            posts.add_post()
        elif choice == "2":
            users.register_user()
        elif choice == "3":
            messages.moderate_messages()
        elif choice == "4":
            followers.manage_followers()
        elif choice == "5":
            channels.create_channel()
        elif choice == "6":
            messages.send_message()
        elif choice == "7":
            login.log_login()
        elif choice == "8":
            friends.find_friends()
        elif choice == "9":
            echo_bot.echo_bot()
        elif choice == "10":
            analytics.analyze_posts()
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()

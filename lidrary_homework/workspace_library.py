# 2 удаление по номеру или по
# названию,# 4 поиск книги по номеру или по названию или по дате издания.
try:
    myfile = open('book.txt', 'r')
except FileNotFoundError:
    print("Файл не открыт")
    myfile = open("book.txt", "a")
books_list = {}

while True:
    print("\nМЕНЮ:")
    print("1 - Добавить")
    print("2 - Удалить")
    print("3 - Найти")
    print("4 - Показать все")
    print("5 - Удалить все")
    print("6 - Выйти")
    print("7 - Замена")

    search = int(input("Ваш выбор:"))

    if search == 1:
        try:
            year = input("Год: ")
            title = input("Название: ")
        except SyntaxError:
            print("Год не может быть набором букв, а название не может быть в цифрах")
        books_list[year] = title
        number = len(books_list)

        with open("book.txt", "a", encoding="utf-8") as myfile:
            myfile.write(f"{number}.{year}\n{title}\n\n")

        print("Добавлено.")


    elif search == 2:

        method = int(input("Удалить по: 1 - номеру, 2 - году, 3 - названию: "))
        value_to_delete = None
        if method == 1:
            value_to_delete = int(input("Введите номер книги для удаления: "))
        elif method == 2:
            value_to_delete = input("Введите год книги для удаления: ")
        elif method == 3:
            value_to_delete = input("Введите название книги для удаления: ")
        new_books_list = [
            book for book in books_list
            if not (
                    (method == 1 and book["number"] == value_to_delete) or
                    (method == 2 and book["year"] == value_to_delete) or
                    (method == 3 and book["title"].lower() == value_to_delete.lower())
            )
        ]
        with open("book.txt", "w", encoding="utf-8") as f:
            for idx, book in enumerate(new_books_list, start=1):
                f.write(f"{idx}.{book['year']}\\n{book['title']}\\n\\n")
        print("Удаление выполнено.")



    elif search == 3:

        search_choice = int(input("Искать по: 1 - номеру, 2 - году, 3 - названию: "))
        key_value = None
        if search_choice == 1:
            key_value = int(input("Введите номер книги: "))
        elif search_choice == 2:
            key_value = input("Введите год книги: ")
        elif search_choice == 3:
            key_value = input("Введите название книги: ").lower()
        found = [book for book in books_list if str(book.get("number")) == str(key_value)]
        if found:
            for book in found:
                print(f'Номер: {book["number"]}, Год: {book["year"]}, Название: {book["title"]}')
        else:
            print("Книга не найдена.")





    elif search == 4:
            with open("book.txt", "r", encoding="utf-8") as myfile:
                print(myfile.read())

    elif search == 5:
        with open("book.txt", "w", encoding="utf-8") as myfile:
            pass

    elif search == 6:
        print("Выход.")




    # elif search == 7:
        
        # NO WORK #
        
        
        
        
        # edit_choice = int(input("Изменить запись по: 1 - номеру, 2 - году, 3 - названию: "))
        # key_value = None
        # if edit_choice == 1:
        #     key_value = int(input("Введите номер книги: "))
        # elif edit_choice == 2:
        #     key_value = input("Введите год книги: ")
        # elif edit_choice == 3:
        #     key_value = input("Введите название книги: ").lower()
        # found_book = None
        # for book in books_list:
        #     if edit_choice == 1 and book["number"] == key_value:
        #         found_book = book
        #         break
        #     elif edit_choice == 2 and book["year"] == key_value:
        #         found_book = book
        #         break
        #     elif edit_choice == 3 and book["title"].lower() == key_value:
        #         found_book = book
        #         break
        # if found_book is not None:
        #     new_title = input("Введите новое название книги: ")
        #     new_year = input("Введите новый год публикации: ")
        #     found_book["title"] = new_title
        #     found_book["year"] = new_year
        #     with open("book.txt", "w", encoding="utf-8") as file:
        #         for i, book in enumerate(books_list, start=1):
        #             file.write(f"{i}. {book['year']}\n{book['title']}\n\n")
        #     print("Запись успешно изменена.")
        # else:
        #     print("Книга не найдена.")

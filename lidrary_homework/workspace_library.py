
try:
    myfile = open('book.txt', 'r')
except FileNotFoundError:
    myfile = open("book.txt", "a")
books = {}

while True:
    print("\nМЕНЮ:")
    print("1 - Добавить")
    print("2 - Удалить")
    print("3 - Найти")
    print("4 - Показать все")
    print("5 - Удалить все")
    print("6 - Выйти")

    search = int(input("Ваш выбор: "))

    if search == 1:
        year = input("Год: ")
        title = input("Название: ")
        books[year] = title
        number = len(books)

        with open("book.txt", "a", encoding="utf-8") as myfile:
            myfile.write(f"{number}.{year}\n{title}\n\n")

        print("Добавлено.")

    elif search == 2:
        method = int(input("Удалить по: 1 - номеру, 2 - году, 3 - названию: "))
        with open("book.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        books_list = []
        for i in range(0, len(lines), 3):
            if i + 1 < len(lines):
                number_year = lines[i].strip()
                title = lines[i + 1].strip()
                number, year = number_year.split(".")
                books_list.append({"number": int(number), "year": year, "title": title})

        if method == 1:
            num = int(input("Введите номер книги для удаления: "))
            books_list = [b for b in books_list if b["number"] != num]

        elif method == 2:
            year_del = input("Введите год книги для удаления: ")
            books_list = [b for b in books_list if b["year"] != year_del]

        elif method == 3:
            title_del = input("Введите название книги для удаления: ")
            books_list = [b for b in books_list if b["title"] != title_del]


        for index, book in enumerate(books_list, 1):
            book["number"] = index

        with open("book.txt", "w", encoding="utf-8") as f:
            for book in books_list:
                f.write(f"{book['number']}.{book['year']}\n{book['title']}\n\n")

        print("Удаление выполнено.")



    elif search == 3:
        method_search = int(input("Искать по: 1 - номеру, 2 - году, 3 - названию: "))
        with open("book.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        books_list = []
        for i in range(0, len(lines), 3):
            if i + 1 < len(lines):
                number_year = lines[i].strip()
                title = lines[i + 1].strip()
                number, year = number_year.split(".")
                books_list.append({"number": int(number), "year": year, "title": title})

        found = []
        if method_search == 1:
            num = int(input("Введите номер книги: "))
            found = [b for b in books_list if b["number"] == num]

        elif method_search == 2:
            year_find = input("Введите год книги: ")
            found = [b for b in books_list if b["year"] == year_find]

        elif method_search == 3:
            title_find = input("Введите название книги: ").lower()
            found = [b for b in books_list if title_find in b["title"].lower()]

        if found:
            for book in found:
                print(f"{book['number']}. {book['year']} - {book['title']}")
        else:
            print("Книги по заданным условиям не найдены.")



    elif search == 4:
            with open("book.txt", "r", encoding="utf-8") as myfile:
                print(myfile.read())

    elif search == 5:
        with open("book.txt", "w", encoding="utf-8") as myfile:
            pass

    elif search == 6:
        print("Выход.")

    else:
        print("Неверный выбор.")
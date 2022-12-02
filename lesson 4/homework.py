# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser Chrome"
# или "Open Browser [Chrome]"
# на ваш выбор.


def show_name_function(func, *args):
    printable_name = func.__name__.title().replace("_", " ")
    print(printable_name, *args)


def open_browser(browser_name):
    show_name_function(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    show_name_function(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    show_name_function(find_registration_button_on_login_page, page_url,button_text)

open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="www.forbes.com/")
find_registration_button_on_login_page(page_url="www.forbes.com/", button_text="login")
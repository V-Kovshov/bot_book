BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050
# BOOK_PATH = 'bot_book/services/book.txt'  # VS Code

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end = min(start + size, len(text))
    text = text[start:end]
    if len(text) <= 1:
        return text, len(text)
    if text[-1] in ',.!:;?' and text[-2] in ',.!:;?':
        text = text[:len(text) - 2]
    while text[-1] not in ',.!:;?':
        text = text[:len(text) - 1]

    return text, len(text)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path) as file:
        book_txt = file.read()
    page_num = 1
    while len(book_txt) >= 2:
        page_text, char = _get_part_text(book_txt, 0, PAGE_SIZE)
        book[page_num] = page_text.lstrip()
        book_txt = book_txt[char:]
        page_num += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)


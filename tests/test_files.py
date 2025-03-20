import pytest
from helpers import FileNames, SiteUrls
from config import RECOURSE_DIR
import os

from parser.Exceptions import LanguageError
from parser.pdf_processor import extract_text_from_pdf
from parser.text_analyzer import analyze_text
from parser.html_parser import parse_html
from parser.doc_processor import extract_text_from_doc
from parser.docx_processor import extract_text_from_docx
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


def test_encoding():
    file_path = os.path.join(RECOURSE_DIR, FileNames.error_encoding)
    text = extract_text_from_pdf(file_path=file_path)

    with pytest.raises(LanguageError) as e:
        analyze_text(text)

    assert e.typename == 'LanguageError', 'Неверный класс исключения при обработке ошибочного языка'

    assert "Язык не найден" == e.value.message, 'При обработке файла с ошибочной кодировка не выведена ошибка с неизвестным языком'
def test_not_found_url():
    url = SiteUrls.not_found
    html_content = parse_html(url)

    assert html_content is None,'Выводится текст по несуществующ еуему url'

def test_unknown_language():
    file_path = os.path.join(RECOURSE_DIR, FileNames.error_encoding)
    text = extract_text_from_pdf(file_path=file_path)

    with pytest.raises(LanguageError) as e:
        analyze_text(text)

    assert e.typename == 'LanguageError', 'Неверный класс исключения при обработке ошибочного языка'

    assert "Язык не найден" == e.value.message, 'При обработке файла с ошибочной кодировка не выведена ошибка с неизвестным языком'

# def test_empty_file():
#     file_path = os.path.join(RECOURSE_DIR, FileNames.empty_file)
#     print(file_path)
#     text = extract_text_from_doc(file_path)

def test_not_exist():
    file_path = os.path.join(RECOURSE_DIR,FileNames.not_exits)
    text = extract_text_from_docx(file_path)

    assert not text
def test_undefined_format():
    file_path = os.path.join(RECOURSE_DIR,FileNames.undefined_format)
    text = extract_text_from_docx(file_path)
    assert text is None

    text = extract_text_from_doc(file_path)
    assert text is None

    text = extract_text_from_pdf(file_path)

    assert text is None, 'Считан файл pdf хотя на вХоде zip'

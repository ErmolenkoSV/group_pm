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
from parser.djvu_processor import extract_text_from_djvu

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


def test_encoding():
    file_path = os.path.join(RECOURSE_DIR, FileNames.error_encoding)
    text = extract_text_from_pdf(file_path=file_path)

    with pytest.raises(LanguageError) as e:
        analyze_text(text)

    assert e.typename == 'LanguageError', 'При обработке файла с ошибочной кодировкой не выведена ошибка с неизвестным языком'


def test_not_found_url():
    url = SiteUrls.not_found
    html_content = parse_html(url)

    assert html_content is None, 'Выводится текст при вводе некорректного url'


def test_unknown_language():
    file_path = os.path.join(RECOURSE_DIR, FileNames.error_encoding)
    text = extract_text_from_pdf(file_path=file_path)

    with pytest.raises(LanguageError) as e:
        analyze_text(text)

    assert e.typename == 'LanguageError', 'При обработке файла с иностранным языком не выведена ошибка с неизвестным языком'


def test_empty_file():
    file_path = os.path.join(RECOURSE_DIR, FileNames.empty_file)
    print(file_path)
    text = extract_text_from_doc(file_path)

    assert text is None or len(text) == 0

def test_not_exist():
    file_path = os.path.join(RECOURSE_DIR, FileNames.not_exists)
    text = extract_text_from_docx(file_path)

    assert not text, 'При вводе несуществующего пути до файла программа не вывела сообщение об ошибке'


def test_undefined_format():
    file_path = os.path.join(RECOURSE_DIR, FileNames.undefined_format)
    text = extract_text_from_docx(file_path)
    assert text is None, 'При вводе пути до файла zip программа считывает текст .docx'

    text = extract_text_from_doc(file_path)
    assert text is None, 'При вводе пути до файла zip программа считывает текст .doc'

    text = extract_text_from_pdf(file_path)
    assert text is None, 'При вводе пути до файла zip программа считывает текст .pdf'

    text = extract_text_from_djvu(file_path)
    assert text is None, 'При вводе пути до файла zip программа считывает текст .djvu'


def test_basic_doc():
    file_path = os.path.join(RECOURSE_DIR, FileNames.basic_docs['doc'])
    text = extract_text_from_doc(file_path)

    assert text is not None


def test_basic_docx():
    file_path = os.path.join(RECOURSE_DIR, FileNames.basic_docs['docx'])
    text = extract_text_from_docx(file_path)

    assert text is not None


def test_basic_pdf():
    file_path = os.path.join(RECOURSE_DIR, FileNames.basic_docs['pdf'])
    text = extract_text_from_pdf(file_path)

    assert text is not None


def test_basic_djvu():
    file_path = os.path.join(RECOURSE_DIR, FileNames.basic_docs['djvu'])
    text = extract_text_from_djvu(file_path)

    assert text is not None


def test_abbreviation_doc():
    file_path = os.path.join(RECOURSE_DIR, FileNames.abbreviation['doc'])
    text = extract_text_from_doc(file_path)
    analyze = analyze_text(text)

    nasa = [analiz for analiz in analyze][0]

    assert nasa['text'] == 'NASA' and nasa['position'] == 'PROPN'


def test_abbreviation_docx():
    file_path = os.path.join(RECOURSE_DIR, FileNames.abbreviation['docx'])
    text = extract_text_from_docx(file_path)
    analyze = analyze_text(text)

    nasa = [analiz for analiz in analyze][0]

    assert nasa['text'] == 'NASA' and nasa['position'] == 'PROPN'


def test_abbreviation_pdf():
    file_path = os.path.join(RECOURSE_DIR, FileNames.abbreviation['pdf'])
    text = extract_text_from_pdf(file_path)
    analyze = analyze_text(text)

    nasa = [analiz for analiz in analyze][0]

    assert nasa['text'] == 'NASA' and nasa['position'] == 'PROPN'


def test_abbreviation_djvu():
    file_path = os.path.join(RECOURSE_DIR, FileNames.abbreviation['djvu'])
    text = extract_text_from_djvu(file_path)
    analyze = analyze_text(text)

    nasa = [analiz for analiz in analyze][0]

    assert nasa['text'] == 'NASA' and nasa['position'] == 'PROPN'

def test_big_file():
    file_path = os.path.join(RECOURSE_DIR, FileNames.big_file)

    with pytest.raises(Exception) as e:
        text = extract_text_from_pdf(file_path)
        analyze = analyze_text(text)
    assert e.value is None or analyze is not None
import spacy
from langdetect import detect

from parser.Exceptions import LanguageError


def analyze_text(text):

    nlp = None

    try:
        text = ' '.join(text.split())
        language = detect(text)
        if language == 'en':
            nlp = spacy.load("en_core_web_sm")
        elif language == 'ru':
            nlp = spacy.load("ru_core_news_sm")

    except Exception as e:
        print(f"Ошибка при анализе текста: {e}")

    if nlp is None:
        raise LanguageError(message='Язык не найден')

    doc = nlp(text)
    analyze = []
    for token in doc:
        analyze.append({'text': token.text, 'lemma': token.lemma_, 'position': token.pos_, 'dependency': token.dep_})
    print(analyze)
    return analyze


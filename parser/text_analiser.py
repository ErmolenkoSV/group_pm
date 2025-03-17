import spacy
from langdetect import detect

def analyze_text(text):
    try:
        text = ' '.join(text.split())
        language = detect(text)
        if language == 'en':
            nlp = spacy.load("en_core_web_sm")
        elif language == 'ru':
            nlp = spacy.load("ru_core_news_sm")
        else:
            print(f"Модель для языка {language} не найдена. Используется модель по умолчанию (английский).")
            nlp = spacy.load("en_core_web_sm")

        doc = nlp(text)
        for token in doc:
            print(f"{token.text} ({token.lemma_}) --> {token.pos_} [{token.dep_}]")
    except Exception as e:
        print(f"Ошибка при анализе текста: {e}")

# group_pm
# Text Analyzer

Этот проект позволяет извлекать текст из различных форматов файлов (PDF, DOCX, DOC, DJVU) и HTML-страниц, а также выполнять синтаксический анализ текста с использованием библиотеки `spaCy`.

## Требования

- Python 3.9 или выше
- Утилиты `antiword` и `djvulibre` для обработки DOC и DJVU файлов

## Установка

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/ErmolenkoSV/group_pm/blob/main/LAB1_AC.ipynb
   cd LAB1_AC.ipynb
Установите необходимые Python-библиотеки:

Copy
pip install -r requirements.txt
Установите системные зависимости:

Для Debian/Ubuntu:
Copy
sudo apt-get update
sudo apt-get install antiword djvulibre-bin
Для других систем: установите antiword и djvulibre с помощью соответствующего пакетного менеджера.
Скачайте модели для spaCy:

Copy
python -m spacy download en_core_web_sm
python -m spacy download ru_core_news_sm
Использование
Запустите скрипт, следуя инструкциям на экране для ввода путей к файлам или URL-адресов:

Copy
python app/main.py
Функциональность
Извлечение текста: Поддерживаются форматы PDF, DOCX, DOC и DJVU.
Синтаксический анализ: Анализирует текст на английском и русском языках.
Парсинг HTML: Извлекает текст из HTML-страниц.
Пример использования
Введите путь к PDF файлу, когда будет предложено.
Введите URL веб-страницы для извлечения и анализа текста.

from bs4 import BeautifulSoup
import requests

from parser.text_analyzer import analyze_text


def parse_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            encoding = response.apparent_encoding
            html_content = response.content.decode(encoding)
            soup = BeautifulSoup(html_content, 'html.parser')
            paragraphs = soup.find_all('p')
            full_text = ' '.join(paragraph.text.strip() for paragraph in paragraphs)

            return full_text
    except Exception as e:
        print(f"Ошибка при парсинге HTML: {e}")
        return None

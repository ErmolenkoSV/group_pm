from parser.pdf_processor import extract_text_from_pdf
from parser.docx_processor import extract_text_from_docx
from parser.doc_processor import extract_text_from_doc
from parser.djvu_processor import extract_text_from_djvu
from parser.html_parser import parse_html
from parser.text_analyzer import analyze_text

def main():

    
    # Запрос путей к файлам и URL у пользователя
    pdf_path = input("Введите путь к PDF файлу (или нажмите Enter, чтобы пропустить): ")
    docx_path = input("Введите путь к DOCX файлу (или нажмите Enter, чтобы пропустить): ")
    doc_path = input("Введите путь к DOC файлу (или нажмите Enter, чтобы пропустить): ")
    djvu_path = input("Введите путь к DJVU файлу (или нажмите Enter, чтобы пропустить): ")
    url = input("Введите URL веб-страницы (или нажмите Enter, чтобы пропустить): ")

    # Извлечение и анализ текста
    if pdf_path:
        pdf_text = extract_text_from_pdf(pdf_path)
        analyze_text(pdf_text)

    if docx_path:
        docx_text = extract_text_from_docx(docx_path)
        analyze_text(docx_text)

    if doc_path:
        doc_text = extract_text_from_doc(doc_path)
        analyze_text(doc_text)

    if djvu_path:
        djvu_text = extract_text_from_djvu(djvu_path)
        analyze_text(djvu_text)

    if url:
        html_text = parse_html(url)
        analyze_text(html_text)

if __name__ == "__main__":
    main()

import subprocess

def extract_text_from_doc(file_path):
    try:
        # result = subprocess.run(['antiword', file_path], stdout=subprocess.PIPE, check=True)
        with open(file_path,'rb') as f:
            result = f.read()
        print(result.decode())
        return result.stdout.decode('utf-8')
    except Exception as e:
        print(f"Ошибка при чтении DOC: {e}")
        return None
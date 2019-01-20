import nltk

def main():
    file_path = input("Path to the file to use --> ")
    with open(file_path, 'r', encoding="utf-8") as f:
        f = f.read()

main()
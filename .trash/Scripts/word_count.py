import glob

def read_file(src: str):
    file = open(src, 'r', encoding="utf-8")
    return file.read()

books = {}

for file in glob.glob("Chapters\**\*.md", recursive=True):

    lines = read_file(file).split("----")[1].replace("◇", "").strip().split("\n")
    content = ""
    for line in lines:
        t = line.strip()
        if t == '': continue
        content += t + "\n"
        
    content = content.split()
    if content == []: continue
    
    book_name = file.split("\\")[1]
    if book_name not in books:
        books[book_name] = 0
    books[book_name] += len(content)

print("\n\n")
for book in books:
    print(book + ": {:,} words".format(books[book]) )
print("\n\n")
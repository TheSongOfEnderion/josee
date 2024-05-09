import glob, os
import re
import copy
print("\n"*2)
def read_file(src: str):
    file = open(src, 'r', encoding="utf-8")
    return file.read()

def write_file(src: str, content: str):
    file = open(src, 'w', encoding="utf-8")
    file.write(content)
    file.close()

def replace(content: str):
    result = re.sub("“|”", '"', content)
    result = re.sub("‘|’", "'", result)
    result = result.replace("◇◇◇◇◇", "◇ ◇ ◇ ◇ ◇")
    return result

def clean(file):
    content = read_file(file).strip()
    content = replace(content)

    content_lines = content.strip().split("\n")
    processed_content = ""
    for line in content_lines:
        t = line.replace(" ", "").strip()
        if t == '': continue
        
        if "◇" in t:
            processed_content += "\n◇ ◇ ◇ ◇ ◇\n\n\n"
            continue
        
        # Replace apostrophes
        for a in apos:
            line = line.replace(a, (apos.index(a)*"|") + "|||")

        apos_lines = re.findall("('.*?')", line)
        if apos_lines == []:
            # Cleans it
            for a in reversed(apos):
                line = line.replace((apos.index(a)*"|") + "|||", a)
            processed_content += line + "\n\n"
            continue
        
        # Covers text with '_ {text} _'
        for apos_line in apos_lines:
            new_line = copy.copy(apos_line).strip()
            if not apos_line.startswith("'_"):
                new_line = new_line.replace(new_line[0:3], "'_" + new_line[0:3].replace("'", ""))
            new_line = new_line.replace("_ '", "_'")
            if not apos_line.endswith("_'") and not apos_line.endswith("_.'"):
                new_line = new_line.replace(new_line[-3:], new_line[-3:].replace("'", "") + "_'")
            line = line.replace(apos_line, new_line)

        # Cleans it
        for a in reversed(apos):
            line = line.replace((apos.index(a)*"|") + "|||", a)
        processed_content += line + "\n\n"
    
    write_file(file, processed_content.replace("...", "…"))
    print(file + "  Done!")


apos = [
    "'s",
    "'t",
    "'m",
    "'ll",
    "'ve",
    "'re",
]

apos_reversed = reversed(apos)

for file in glob.glob("Chapters\**\*.md", recursive=True):
    clean(file)
    

# for file in glob.glob("**\*.md", recursive=True):
#     clean(file)
import subprocess


mapping = {
    "ଦେଖାନ୍ତୁ": "print", "dekhantu": "print",
    "ନେଅନ୍ତୁ": "input", "neantu": "input",
    "ଜୋଡି": "if", "jodi": "if",
    "ନହିଲେଜୋଡି": "elif", "nahilejodi": "elif",
    "ନହିଲେ": "else", "nahile": "else",
    "ପାଇଁ": "for", "pain": "for",
    "ଜେପୋରି": "while", "jepori": "while",
    "ପରିଭାଷକାର": "def", "paribhasakara": "def",
    "ଶ୍ରେଣୀ": "class", "sreni": "class",
    "ଫେରିଦାନ୍ତୁ": "return", "pheridianthu": "return",
    "ଭଙ୍ଗିଦା": "break", "bhangida": "break",
    "ଜରିରଖ": "continue", "jarirakh": "continue",
    "ଆୟାତକାର": "import", "aayatkara": "import",
    "ରୁ": "from", "ru": "from",
    "ରୂପେ": "as", "rupe": "as",
    "ସହିତ": "with", "sahita": "with",
    "ଚେଷ୍ଟାକରା": "try", "chestakara": "try",
    "ଛାଡ": "except", "chhada": "except",
    "ସେସାରେ": "finally", "sesare": "finally",
    "ସତ୍ୟ": "True", "satya": "True",
    "ମିଥ୍ୟା": "False", "mithya": "False",
    "କିଛିନାହିଁ": "None", "kichhinahi": "None",
    "କିମ୍ବା": "or", "kimba": "or"
}

def translate(code: str) -> str:

    for od_word, py_word in mapping.items():
        code = code.replace(od_word, py_word)
    return code

with open("test.od", "r", encoding="utf-8") as f:
    od_code = f.read()


python_code = translate(od_code)
with open("temp.py", "w", encoding="utf-8") as f:
    f.write(python_code)

subprocess.run(["python3", "temp.py"])

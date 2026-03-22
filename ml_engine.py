import re

SKILLS = [
    "python","machine learning","deep learning","nlp",
    "sql","pandas","numpy","tensorflow","pytorch",
    "docker","api","statistics"
]

def clean(text):
    return re.sub(r"[^a-zA-Z0-9+#. ]", " ", text.lower())

def extract(text):
    return [s for s in SKILLS if s in clean(text)]

def calculate_score(resume, job):
    r = extract(resume)
    j = extract(job)

    matched = set(r) & set(j)
    missing = set(j) - set(r)

    score = (len(matched)/len(j))*100 if j else 0

    return round(score,2), list(matched), list(missing)
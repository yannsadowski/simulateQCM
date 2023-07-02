import json
import re

# Ouvrir et lire le fichier
with open('machine-learning-quiz.md', 'r') as f:
    txt = f.read()

# Sépare les questions
questions = re.split(r'#### Q\d+', txt)[1:] # Ignore le premier élément vide
data = []

for idx, q in enumerate(questions, start=1):
    q = q.strip()
    # sépare la question, les réponses, et la référence s'il y en a
    parts = q.split('\n- ')
    question = parts[0].strip()
    answers = [ a for a in parts[1:]]  # adds back the part that was removed by the split
    correct_answers = [i for i, a in enumerate(answers) if '[x]' in a]
    if not correct_answers:
        print(answers)
        raise ValueError(f"Pas de réponse correcte trouvée pour la question {idx}")
    correct_answer = correct_answers[0]
    answers = [re.sub(r'\[.\]', '', a) for a in answers] # retire les [x] et [ ] des réponses
    # Ajoute les informations dans le format désiré
    data.append({
        'question': question,
        'answers': answers,
        'correct_answer': correct_answer
    })

# Convertit la liste en JSON et l'écrit dans un fichier
with open('questions.json', 'w') as f:
    json.dump(data, f)

import json
import re

# Open and read the file
with open('machine-learning-quiz.md', 'r') as f:
    txt = f.read()

# Separate the questions
questions = re.split(r'#### Q\d+', txt)[1:] # Ignore the first empty element
data = []

for idx, q in enumerate(questions, start=1):
    q = q.strip()
    # Separate the question, the answers, and the reference if there is one
    parts = q.split('\n- ')
    question = parts[0].strip()
    answers = [a for a in parts[1:]]  # adds back the part that was removed by the split
    correct_answers = [i for i, a in enumerate(answers) if '[x]' in a]
    if not correct_answers:
        print(answers)
        raise ValueError(f"No correct answer found for question {idx}")
    correct_answer = correct_answers[0]
    answers = [re.sub(r'\[.\]', '', a) for a in answers] # removes the [x] and [ ] from the answers
    # Add the information in the desired format
    data.append({
        'question': question,
        'answers': answers,
        'correct_answer': correct_answer
    })

# Convert the list into JSON and write it into a file
with open('questions.json', 'w') as f:
    json.dump(data, f)

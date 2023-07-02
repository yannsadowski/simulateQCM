import json
import re
import requests
import base64

def get_quiz_files(quiz_folder):
    # Use the GitHub API to get the file list in the folder
    response = requests.get(f'https://api.github.com/repos/Ebazhanov/linkedin-skill-assessments-quizzes/contents/{quiz_folder}')
    response.raise_for_status()  # raise an exception if the request fails
    files = response.json()

    # Filter out the .md files
    md_files = [file['name'] for file in files if file['name'].endswith('.md')]

    return md_files

def convert_quiz_to_json(quiz_folder):
    # Get the .md files in the folder
    md_files = get_quiz_files(quiz_folder)

    # If no .md file is found, raise an exception
    if not md_files:
        raise ValueError(f"No .md file found in folder {quiz_folder}")

    # If multiple .md files are found, ask the user to choose one
    if len(md_files) > 1:
        print("Multiple .md files found. Please choose one:")
        for i, file in enumerate(md_files, start=1):
            print(f"{i}. {file}")
        file_num = int(input("Enter the number of the file you want to choose: "))
        quiz_file = md_files[file_num - 1]
    else:
        quiz_file = md_files[0]

    # Use the GitHub API to get the file content
    response = requests.get(f'https://api.github.com/repos/Ebazhanov/linkedin-skill-assessments-quizzes/contents/{quiz_folder}/{quiz_file}')
    response.raise_for_status()  # raise an exception if the request fails
    file_content = base64.b64decode(response.json()['content']).decode('utf-8')

    # Separate the questions
    questions = re.split(r'#### Q\d+', file_content)[1:] # Ignore the first empty element
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
    with open('JSON/'+quiz_folder+'.json', 'w') as f:
        json.dump(data, f)

# Call the function with the desired quiz folder
convert_quiz_to_json('python')

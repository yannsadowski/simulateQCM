import requests

def get_quiz_folders():
    # Use the GitHub API to get the file list in the root directory of the repository
    response = requests.get('https://api.github.com/repos/Ebazhanov/linkedin-skill-assessments-quizzes/contents')
    response.raise_for_status()  # raise an exception if the request fails
    files = response.json()

    # Filter out the directories
    directories = [file['name'] for file in files if file['type'] == 'dir']

    return directories

def choose_quiz_folder():
    # Get the list of directories in the repository
    directories = get_quiz_folders()

    # Print the list and ask the user to choose one
    print("Please choose a competency from the list:")
    for i, directory in enumerate(directories, start=1):
        print(f"{i}. {directory}")
    folder_num = int(input("Enter the number of the competency you want to choose: "))
    quiz_folder = directories[folder_num - 1]

    return quiz_folder

# Call the function
quiz_folder = choose_quiz_folder()
print(f"You chose {quiz_folder}")

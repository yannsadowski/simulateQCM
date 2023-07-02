# simulateQCM

## Project Description

The `simulateQCM` project is a tool designed for simulating multiple-choice quizzes (MCQs) based on LinkedIn's skill assessment quizzes. This tool aims to aid users in preparing for LinkedIn's skill assessments by providing a platform to practice these quizzes. The project directly utilizes quizzes from the [linkedin-skill-assessments-quizzes/tree/main/machine-learning](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/tree/main/machine-learning) repository as the source for the MCQ simulations.

The questions are sourced from the quizzes file in the `linkedin-skill-assessments-quizzes` repository which is then converted into a JSON format by the Python script "qcmMLtoJSON.py". This script generates a "questions.json" file containing all quiz questions in a readily usable format. The "test.html" file serves as the user interface for taking the quiz.

## Link
You can use the following link for try with the machine learning [quizz](https://yannsadowski.github.io/simulateQCM/test.html)

## Usage 

To use this project, you need to deploy it to a GitHub Pages website. This is necessary because the project uses fetch API which does not work with local files due to security reasons. Here are the steps:

1. Fork this repository to your own GitHub account.
2. Navigate to the repository settings.
3. In the GitHub Pages section, select the main branch as the source.
4. Click on "Save" to deploy your site. GitHub will provide a link to your live site.

Now, you can access the quiz interface by opening the "test.html" file from your GitHub Pages website.

## About

This project was created by Yann Sadowski. For further information, feel free to contact me.


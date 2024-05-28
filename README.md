# Movie Recommender

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation And Requirements](#installation-and-requirements)
5. [Usage](#usage)
6. [Folder Structure](#folder-structure)
7. [Authors And Additional Info](#authors-and-additional-information)

## Introduction

Movie Recommender is a web application that helps users discover the best films based on a given title. Leveraging the power of machine learning, the application utilizes a recommendation system trained on a dataset of over 5000 movies from The Movie Database (TMDb). Users can input the title of a movie they enjoyed, and the system will analyze its characteristics to suggest similar films that they might like.

## Features

- **Film Recommendation**: Users can input the title of a movie they enjoyed, and the application will provide a list of recommended films based on similar themes, genres, and audience preferences.
- **Interactive Interface**: The web interface allows users to easily navigate through the recommendations and explore additional details about each suggested film. The site displays posters of recommended movies. When hovering over the selected film, its title is displayed, and when clicked, it redirects to the TMDB page with information about the selected film.

## Technologies Used:

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Machine Learning**: Python, Scikit-learn, Pandas
- **Data Source**: The Movie Database (TMDB) API, TMDB 5000 Movie Dataset

## Installation And Requirements

To start the service:

1. Run the `backend.py` file:
    1. Make sure you have python version 3.12 or newer installed
    2. Install the required libraries to run the script:
        - flask
        - flask_cors
        - joblib
        - requests
    3. Use the commands below to run the script:
        - Windows: ``python backend.py``
        - Linux: ``python3 backend.py``
    4. Provide the API key for the TMDB service in the `backend.py` file. The recommended way to pass the key is to create an `env.py` file with the **TMDB_API_KEY** variable in it.
    5. Configure request addresses. When running locally, change the addresses to which requests are sent (from 127.0.0.1) in files `website/static/appearance.js` and `website/request/request.js` to the address of the device from which the script is run.
2. Enter the device address in your browser
3. You can use the website

To create model files:

1. Make sure you have python version 3.12 or newer installed
2. Install the required libraries to run the script:
    - ast
    - pandas
    - sklearn
    - joblib
3. Use the commands below to run the script:
    - Windows: ``python model_script.py``
    - Linux: ``python3 model_script.py``

After running the script, the files should appear in the **model/components** folder

## Usage

In the text box, enter the title of the movie you wish to find similar titles for. As you begin typing, the available options will appear. The title of the film must be in English.

## Folder Structure

**/input**  
A folder containing data to create the model

**/model**  
A folder containing the script for creating the model and a jupyter notebook with the steps for creating the model described.

**/website**  
A folder containing files responsible for the appearance and operation of the website.

## Authors And Additional Information

**Authors**: Jakub Magiera, Konrad Wójcik

Project created as part of the "Team Project" course in the summer semester 2024.

The model was created based on the model from the Ibtesam Ahmed notebook "Getting Started with a Movie Recommendation System"  
https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system
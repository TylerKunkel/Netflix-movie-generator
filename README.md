# Netflix-movie-generator

The goal of this project is to create a movie picker application that uses the uNoGS (unofficial Netflix online Global Search) API to retrieve the current list of movies on Netflix. The project will be written in Python, and it will utilize the requests library to make HTTP requests to the uNoGS API.

Here's a high-level overview of the steps we'll need to take to create the Netflix movie picker:

Install requests: We'll need to install the requests library if we haven't already. We can do this by running pip install requests in the terminal.

Retrieve the list of movies on Netflix: We'll make an HTTP request to the uNoGS API to retrieve the list of movies currently available on Netflix. The API returns data in JSON format, which we can parse using the json library in Python.

Randomly select a movie: We'll randomly select a movie from the list of movies on Netflix that we retrieved in step 2. We can use the random library in Python to do this.

Display the selected movie: We'll display the selected movie to the user, along with some information about the movie such as its title, synopsis, and rating.

Allow the user to select another movie: We'll ask the user if they want to select another movie. If they do, we'll repeat steps 3 and 4. If they don't, we'll exit the program.

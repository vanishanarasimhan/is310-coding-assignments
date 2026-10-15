# Supernatural Stories Across Cultures

This project is about collecting different jinn (spirit) stories from cultures around the world. Users can enter the name of a story, where it comes from, a short description, and the source.

## Python CLI

The Python script allows users to add stories through the terminal. It first shows a few example stories and then asks users to enter their own. Once they confirm that everything is correct, the information is saved in a JSON file.

## How to Run

1. Install the requirements:
   `pip install -r requirements.txt`

2. Run the Python script:
   `python cli_data_entry.py`

## HTML Interface

To use the HTML version, open `index.html` in a browser. Users can fill out the fields to add their stories and see what they entered. They can also download their stories as a JSON file.

## Comparing the Interfaces

The Python version is pretty simple to use, but you have to answer each question one at a time in the terminal. The HTML version feels a little easier because you can see all the fields at once and fill them out in any order.

Both versions collect the same information, but they work a little differently. The HTML version makes sure users don't leave any required fields empty, while the Python version asks users to check their answers before saving them.

I used ChatGPT to help me write the Python and HTML code and figure out how to organize the files. I also used it to help understand how to save the information as a JSON file.

Overall, I think the HTML version works better for this project because it's easier to see all the information and look over the stories before downloading them.
#!/usr/bin/python3

# -*- Author: Ali -*-
# -*- Info: Chatbot with Natural Language Processing for Detecting Negative and Positive Texts using Python -*-
# -*- Description: This script provides a chatbot that detects the sentiment of a given text using the Natural Language Toolkit (NLTK) library and the VADER sentiment analysis tool. The chatbot can detect sentiment from a file, user input, or a default message. -*-

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tkinter import filedialog
import tkinter as tk

# Download the necessary NLTK data
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()


def detect_sentiment(text):
    """
    Detects the sentiment of a given text using the SentimentIntensityAnalyzer.
    Returns a dictionary with the scores for positive, negative, neutral, and compound sentiment.
    """
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores


def handle_message(message):
    """
    Handles a user message by detecting its sentiment and returning an appropriate response.
    """
    sentiment_scores = detect_sentiment(message)

    if sentiment_scores['compound'] > 0.05:
        response = "I'm pleased to hear that! How may I assist you with your tasks today?"
    elif sentiment_scores['compound'] < -0.05:
        response = "I'm sorry to hear that. Is there anything I can do to help you feel better?"
    else:
        response = "I understand. How can I assist you with your tasks today?"

    return response


def detect_sentiment_from_file():
    """
    Detects sentiment from a file chosen by the user.
    """
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        message = file.read()
    response = handle_message(message)
    print(response)


def detect_sentiment_from_input():
    """
    Detects sentiment from user input.
    """
    message = input("Please enter a message: ")
    response = handle_message(message)
    print(response)


def detect_sentiment_from_default_message():
    """
    Detects sentiment from the default message.
    """
    message = "I'm feeling really happy today!"
    response = handle_message(message)
    print(response)


if __name__ == '__main__':
    # Add options to the main menu
    print("1. Detect sentiment from file")
    print("2. Detect sentiment from user input")
    print("3. Detect sentiment from default message")

    option = int(input("Please enter the option number: "))

    if option == 1:
        detect_sentiment_from_file()
    elif option == 2:
        detect_sentiment_from_input()
    elif option == 3:
        detect_sentiment_from_default_message()
    else:
        print("Invalid option. Please try again.")

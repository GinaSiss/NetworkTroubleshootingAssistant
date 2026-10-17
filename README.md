The project files Network Troubleshooting Assistant is a Python program designed to help users identify and troubleshoot common internet connection problems. The program asks the user a series of questions and provides suggestions based on their answers. The goal is to make basic network troubleshooting easier for people who may not have much technical experience. This project demonstrates how Python can be used to solve everyday technology problems through simple programming logic.
## Project Purpose
Internet connection problems can happen for several reasons. Sometimes the problem is with the computer, while other times it may be related to a router, modem, or internet service interruption. It can be difficult for users to know where to start when their internet stops working. This program helps narrow down the possible cause by asking questions about the connection and whether other devices can access the internet.
## Technologies Used
This project was created using Python. The program uses the built-in input() function to ask questions and collect answers from the user. It uses the print() function to display messages and troubleshooting recommendations. Conditional statements, including if and else, allow the program to make decisions based on the user’s responses. Functions help organize the code and separate different parts of the program. These features make the program easier to understand, test, and maintain.
## How the Program Works
When the program starts, it displays a welcome message explaining that it will help troubleshoot common internet connection problems. It then asks whether the user can access the internet. If the user answers yes, the program confirms that the internet connection is working.
If the user answers no, the program asks whether other devices can connect to the internet. If other devices can connect, the program suggests that the problem may be with the user’s computer and recommends restarting it. If other devices cannot connect either, the program suggests that the issue may involve the router or modem and recommends restarting the network equipment.
These questions help guide the user toward a possible solution without requiring advanced networking knowledge.
## Main Features
The main features include interactive questions, decision-making based on user responses, and troubleshooting suggestions. The program is designed to be straightforward so users can follow the questions and understand the recommendations. It also provides a simple example of how conditional logic can be used to create a useful troubleshooting tool.
Project Files
The GitHub repository contains three main files. TermProject.py contains the Python source code for the Network Troubleshooting Assistant. README.md explains the project’s purpose, features, setup, and testing. requirements.txt documents the project’s software dependencies. Keeping these files organized makes it easier for another person to understand and run the project.
How to Run the Program
Python must be installed on the computer before running the program. Download or clone the project repository and open Command Prompt in the project folder. Enter the following command:
py TermProject.py
The program will display its welcome message and begin asking questions. Answer the prompts using yes or no. The program will then provide recommendations based on the answers entered.
Testing
I tested the program using different internet connection scenarios. The first scenario involved a working internet connection. The second scenario involved an internet connection that was not working on the computer even though other devices could connect. The third scenario involved a situation where neither the computer nor other devices could connect. Testing these scenarios helped verify that the program followed the expected decision paths and displayed the appropriate troubleshooting recommendations.
Limitations and Future Improvements
This program provides basic troubleshooting suggestions and does not automatically test the computer’s network connection. Future improvements could include additional questions about Wi-Fi signals, network cables, IP addresses, and DNS problems. Another improvement would be creating a graphical user interface with buttons and menus instead of requiring users to type answers. The program could also provide more detailed instructions for different operating systems.
Demonstration Video
The following video demonstrates the Network Troubleshooting Assistant running in Command Prompt.
https://www.youtube.com/watch?v=8jeoo91PFJI
Conclusion
Developing this project provided practical experience with Python functions, user input, conditional statements, testing, and troubleshooting logic. It also demonstrated how a simple program can help users work through common technology problems. The project can serve as a starting point for a more advanced troubleshooting application with additional features and a graphical interface.

***Multi-Client Word Typing Application***

**Overview**

This project is a word typing program that enables two users to connect to a server via the TCP protocol.
It uses a combination of classes, modules, threading, and UI through the use of tkinter in order to create
an interactive window where the user can type and alongside another user and measure certain typing 
statistics such as their WPM (Words per minute) and their accuracy (determined by the number of words they get wrong).
Once the issued sentence is completed, the data is sent to the other user and compared with their most recent statistics
and their best, if it exists.

**Contents**

There are 7 files which constitute the application.

**1. GenerateStringClass:** This module contains 50 sentences where one of which can be provided at random using the *yieldString()*
method. It also contains some methods that provide information on a sentence like the word count in a sentence and the 
location of spaces in the sentence.

**2. SocketServer:** The socket server module should be run on the device that is intended to host the connection to the two clients.
It accepts a connection request from the client and generates a User ID to keep track of the client to whom it will be sending the information
to at the end of each session. At the first client's connection, they will send a request to the server for a sentence which will prompt the
server to generate a sentence using *GenerateStringClass* it will then retain the sentence for the second client to retrieve once its request is
sent. At the end of the session, the other client's statistics are sent to the current user.

**3. Userclass:** The Userclass provides many user-oriented methods that might be used in communication with the server, such as *openconnection()*, *askfornewsen()*, 
*getID()*, *terminateconnection()*, etc. In its initialization, the object will instantiate a timer, and when an instance of the Userclass itself iis created, it needs
a stats object to function properly. 

**4. Stats:** Statistical information is stored and calculated using the methods provided in the class. The primary operations serve to keep track of words per minute, 
and accuracy.

**5. Timerclass:** The timerclass instantiates an object that stores and keeps track of the time elapsed for the purposes of functioning as a stopwatch and to enable calculations 
necessary for words per minute. This class imports the time library in order to accomplish this.

**6. Typingclass:** This provides methods that get fired by a key event and check whether each letter typed was accurate, keeps track of the location of the user along the sentence
and keeps track of other data for typing data to be extracted and acted upon based on whether the user finishes a word, the sentence, and whether or not they've done it correctly or 
incorrectly. It needs a sentence and user to be passed through in the constructor.

**7. GUI:** This module is the primary script for the application, and should be run once the server has run *SocketServer*. It instantiates a user, then establishes a connection between the server
and the client by sending out various requests for an id, the sentence, and so forth. Once the sentence is returned, a GUI opens with the sentence on top, an input box at the bottom, and statistics like
timing and accuracy to the sides. Once the first key is pressed the session for the the user begins and will continue until the last character. Due to the need to check the input, and updating the time to
the screen at the same time, threading is done within this file to handle these processes concurrently. Once the session is finished, the client will notify the server and ask for the other user's stats
which will either return a "N/A" or a list of values. If N/A is recieved, then the client assumes the other user has not completed yet, and will periodically request for their statistics again until it is recieved.
At this point it will open a new window with all relevant statistics listed.

**Screenshots**

![Screenshot 2025-06-11 233555](https://github.com/user-attachments/assets/a3a1f1f4-edb7-4219-b9f4-9d59b0eaabab)

![wtg ss results](https://github.com/user-attachments/assets/de648b41-bf30-4c60-9a25-cbc1e45639ff)

# Login_Sucess-or-Fail
# Login Attempt Analyzer

## Overview

The Login Attempt Analyzer is a simple Python program that reads a text log containing login attempts and reports how many were successful and how many failed. After analyzing the file, it prints every login attempt back to the terminal.

This project was created to practice working with files, loops, conditional statements, and basic data processing in Python.

## Features

* Reads a text file containing login attempts.
* Counts failed login attempts.
* Counts successful login attempts.
* Displays a summary of the results.
* Prints each login attempt after the analysis.

## Concepts Learned

This project helped reinforce several core Python concepts, including:

* Opening and reading files with `with open()`.
* Using `for` loops to process text files line by line.
* Using conditional statements (`if`/`else`) to classify data.
* Creating and updating counters.
* Storing file contents in a list for later use.
* Formatting output using Python f-strings.
* Making searches more reliable with the `.lower()` string method.

## Improvements Made

While I was developing this project, an issue appeared when I tried to loop through the file a second time. Once Python reaches the end of a file, it cannot continue reading unless the file pointer is reset.

To solve this, I imporved the program by storing each line in a list while reading the file. This allows the program to:

1. Read the file only once.
2. Count successful and failed login attempts.
3. Print the complete log afterward without reopening the file.

This approach is both cleaner and more efficient than reading the file multiple times.

## Example Output

```text
There were 3 failed logins.
There were 5 successful logins.

Login attempt: successful
Login attempt: failed
Login attempt: successful
...
```

## Future Improvements

Possible additions include:

* Displaying the percentage of successful and failed logins.
* Detecting repeated failed login attempts from the same user.
* Reading timestamps and usernames from more realistic log files.
* Exporting the analysis to a new report file.
* Creating graphs or charts to visualize login activity.

## Requirements

* Python 3.x
* A `log.txt` file located in the same directory as the program.

## Purpose

This project served to me as a beginner-friendly exercise in Python file handling and log analysis. Although simple, I have seen while diving into the code of websites that it demonstrates many of the programming techniques used when processing real-world log files in cybersecurity and system administration such as login requirements for websites or subscriber information on streaming services.

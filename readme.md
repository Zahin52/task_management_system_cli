# Please Readme:
<b>
    All the feature implementations, bug fixing, refactoring, and task details are given below 
</b>

# Task Management System

This is a simple command-line (CLI) task management system implemented in Python.

## Functional Requirements

The application should allow users to do the following:

1. Add a new task
2. Complete a task
3. List all tasks (with an option to show only incomplete tasks)
4. Generate a report of task statistics, which should include:
   - Total number of tasks
   - Number of completed tasks
   - Number of pending tasks
   - Average time taken to complete a task
5. The application must persist user data across sessions, ensuring that all information remains intact and accessible upon returning, without resetting or losing any previously entered tasks

## Key Missing Features and Issues
1. <b>Persistence:</b> The task list does not persist between sessions (critical missing functionality).

2. <b>Task Completion Timing:</b> Task objects need to store completed_at timestamp to calculate the average time to complete tasks.

3. <b>Error Handling:</b> Minimal error handling is implemented, especially around task completion, file read/write operations, or input validation.

4. <b>Testing:</b> Proper tests should be written for all functions.

## Suggested and Implemented Fixes
1. <b>Persistence:</b> Used a JSON file to store and load tasks between sessions in the Storage class.
Added file read/write operations to save the tasks when the app is closed and load them when the app starts.

2. <b>Task Completion Timing:</b> Modified the Task class to store the completed_at timestamp.
Calculate the average time for completed tasks in the report.

3. <b>Error Handling:</b> Added input validation and error handling for file operations and invalid commands.

4. <b>Unit Testing:</b> Created unit tests to validate task addition, completion, listing, and reporting. Additionally, add few more unit test.

5. <b>CLI user interface modification: </b> Gave an interactive feel to command-line (CLI) task management system


## Setup

1. Ensure you have Python 3.7 or higher installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Install Poetry if you don't have it installed:
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```
5. Install dependencies
    ```
    poetry install
    ```
6.  Running the application
    ```
    poetry run python main.py
    ```

## Running Tests

To run all the unit tests, use the following command:

```
python -m unittest discover tests
```

## My Task

**Ensure and validate with tests that the app meets the required functionality** and addresses any bugs. Enhance performance and do optimisations to the best of your knowledge, while refactoring the code for better readability and maintainability. Feel free to make necessary assumptions where applicable.

## Submission

Once you are done, please:

1. Push your code to a **public** GitHub repository with at least **read** access
2. Reply to our email with the repository link to complete your submission within the deadline

Good luck!

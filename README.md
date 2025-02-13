# To-Do List GUI App

A simple Python GUI application for managing to-do lists, built with Tkinter. This app allows you to add, edit, delete, and mark tasks as completed. It saves tasks to a JSON file so they persist between app sessions.

## Features:
- Add, Edit, Delete, and Mark tasks as completed.
- Persistent storage using JSON files.
- Simple and intuitive GUI interface with Tkinter.

## Requirements:
- Python 3.x
- Tkinter (comes pre-installed with Python)
- JSON (comes pre-installed with Python)

## Installation:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/todo-list.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd todo-list
    ```

3. **Run the app**:
    ```bash
    python todo_list_app.py
    ```

## Usage:

1. **Add a Task**:
    - Enter the task description in the input field and click **Add Task**.

2. **Edit a Task**:
    - Select a task from the list, edit its description in the input field, and click **Edit Task**.

3. **Delete a Task**:
    - Select a task from the list and click **Delete Task** to remove it.

4. **Mark a Task as Completed**:
    - Select a task from the list and click **Mark as Completed**. The task will be displayed as completed.

## File Structure:

- `todo_list_app.py`: The main Python script containing the application logic.
- `tasks.json`: The file where tasks are saved (persistent storage).

## License:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


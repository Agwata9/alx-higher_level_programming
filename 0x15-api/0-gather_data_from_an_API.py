import requests

def get_employee_todo_list(employee_id):
    # API endpoint to get employee information
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee = response.json()

    # API endpoint to get employee tasks
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    tasks = response.json()

    completed_tasks = [task for task in tasks if task["completed"]]
    completed_count = len(completed_tasks)
    total_count = len(tasks)

    # Display employee task progress
    print(f"Employee {employee['name']} is done with tasks({completed_count}/{total_count}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

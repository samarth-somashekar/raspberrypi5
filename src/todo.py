def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        file.write("\n".join(tasks))
def show_tasks(tasks):
    if not tasks:
        print("🎉 No tasks! You're all caught up.")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def main():
    tasks = load_tasks()
    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Quit")
        choice = input("Enter choice (1-4): ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added!")
        elif choice == "3":
            show_tasks(tasks)
            done = int(input("Enter task number to mark done: "))
            if 1 <= done <= len(tasks):
                print(f"✅ Marked '{tasks[done-1]}' as done.")
                tasks.pop(done - 1)
                save_tasks(tasks)
            else:
                print("❌ Invalid task number.")
        elif choice == "4":
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid choice.")
if __name__ == "__main__":
    main()



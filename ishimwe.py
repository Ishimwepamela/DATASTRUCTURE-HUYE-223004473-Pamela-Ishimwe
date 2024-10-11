recent_entries_stack = []
pending_plans_queue = []
history_list = []

def add_entry(workout):
    recent_entries_stack.append(workout)
    history_list.append(workout)
    print(f"Added workout entry: {workout}")
    save_data()

def undo_last_entry():
    if recent_entries_stack:
        last_entry = recent_entries_stack.pop()
        history_list.remove(last_entry)
        print(f"Undo last entry: {last_entry}")
        save_data()
    else:
        print("No entries to undo.")

def add_workout_plan(workout_plan):
    pending_plans_queue.append(workout_plan)
    print(f"Added pending workout plan: {workout_plan}")
    save_data()

def complete_pending_plan():
    if pending_plans_queue:
        completed_plan = pending_plans_queue.pop(0)
        print(f"Completed workout plan: {completed_plan}")
        add_entry(completed_plan)
    else:
        print("No pending plans to complete.")

def view_history():
    if history_list:
        print("\nWorkout History:")
        for workout in history_list:
            print(f"- {workout}")
    else:
        print("No workout history available.")

def view_pending_plans():
    if pending_plans_queue:
        print("\nPending Workout Plans:")
        for plan in pending_plans_queue:
            print(f"- {plan}")
    else:
        print("No pending workout plans.")

def save_data():
    data = {
        'recent_entries_stack': recent_entries_stack,
        'pending_plans_queue': pending_plans_queue,
        'history_list': history_list
    }
    with open('fitness_tracker_data.txt', 'w') as file:
        file.write(str(data))
    print("Data saved successfully.")

def load_data():
    global recent_entries_stack, pending_plans_queue, history_list
    try:
        with open('fitness_tracker_data.txt', 'r') as file:
            data = eval(file.read())
            recent_entries_stack = data['recent_entries_stack']
            pending_plans_queue = data['pending_plans_queue']
            history_list = data['history_list']
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("No previous data found. Starting fresh.")

def menu():
    load_data()

    while True:
        print("\nFitness Tracker Menu:")
        print("1. Add workout entry")
        print("2. Undo last entry")
        print("3. Add workout plan")
        print("4. Complete pending workout plan")
        print("5. View workout history")
        print("6. View pending workout plans")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            workout = input("Enter workout (e.g., Push-ups - 20 reps): ")
            add_entry(workout)

        elif choice == '2':
            undo_last_entry()

        elif choice == '3':
            plan = input("Enter pending workout plan: ")
            add_workout_plan(plan)

        elif choice == '4':
            complete_pending_plan()

        elif choice == '5':
            view_history()

        elif choice == '6':
            view_pending_plans()

        elif choice == '7':
            print("Exiting the Fitness Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()


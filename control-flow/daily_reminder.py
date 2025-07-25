task = input("Enter your task: ").strip().lower()

priority = input("Priority (high/medium/low): ").strip().lower()

time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high priority task. Please ensure it is completed soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: You have a medium priority task '{task}' that is time-bound. Please complete it in a timely manner.")
        else:
            print(f"Reminder: You have a medium priority task '{task}'. Please try to complete it soon.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: You have a low priority task '{task}' that is time-bound. Please complete it when you can.")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
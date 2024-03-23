def job_scheduling_with_profit(jobs):
    # Sort jobs based on their profit in descending order
    jobs.sort(key = lambda x: x[2], reverse = True)
    # Initialize schedule, count of jobs scheduled, and total profit
    schedule = []
    count = 0
    total_profit = 0

    # Greedy scheduling considering deadlines
    for job in jobs:
        deadline = job[1]
        profit = job[2]
        # Find available time slot before deadline
        for i in range(deadline, 0, -1):
            if i not in schedule:
                schedule.append(i)
                count += 1
                total_profit += profit
                break
    
    return count, total_profit, schedule
    

# Example usage
jobs = [("Job1", 2, 20), ("Job2", 2, 15), ("Job3", 1, 10), ("Job4", 3, 5), ("Job5", 3, 1)]
max_jobs_completed, total_profit, schedule = job_scheduling_with_profit(jobs)
print("Maximum number of jobs completed:", max_jobs_completed)
print("Total profit:", total_profit)
print("Scheduled time slots:", schedule)

# Output:
# Maximum number of jobs completed: 3
# Total profit: 40
# Scheduled time slots: [2, 1, 3]

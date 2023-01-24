# Offline Nanosatellite Task Scheduling (ONTS) data for 97 time units and 9 tasks.
T = 97 # Units of time
J = 9 # Number of tasks
resource = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0] # Power available for tasks consumption for each unit of time 
priority = [5, 2, 1, 4, 1, 3, 1, 1, 1] # Priority of each task 
consumption = [3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0] # Power consumption of each task 
min_startup = [2, 2, 3, 1, 1, 1, 2, 1, 1] # Minimum startups required for each task 
max_startup = [4, 6, 5, 7, 5, 6, 7, 8, 9] # Maximum startups required for each task 
min_cpu_time = [10, 5, 7, 6, 8, 4, 6, 7, 4] # Minimum execution time units required for each task 
max_cpu_time = [15, 24, 20, 28, 18, 34, 21, 20, 20] # Maximum execution time units required for each task 
min_periodo_job = [30, 28, 24, 32, 24, 28, 24, 24, 24] # Minimum period required for each task 
max_periodo_job = [78, 50, 100, 90, 60, 87, 60, 97, 40] # Maximum period required for each task 
win_min = [30, 0, 0, 0, 0, 40, 0, 0, 0] # Execution window start point for each task 
win_max = [81, 98, 98, 98, 61, 81, 98, 98, 98] # Execution window finish point for each task 

# Offline Nanosatellite Task Scheduling (ONTS) data for 120 time units and 9 tasks.
T = 120 # Units of time
J = 9 # Number of tasks
resource = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0] # Power available for tasks consumption for each unit of time 
priority = [6, 5, 2, 1, 4, 1, 3, 1, 2] # Priority of each task 
consumption = [3, 3, 3, 3, 3, 3, 3, 3, 3] # Power consumption of each task 
min_startup = [1, 2, 1, 2, 1, 4, 1, 2, 4] # Minimum startups required for each task 
max_startup = [1, 4, 5, 4, 9, 12, 10, 4, 19] # Maximum startups required for each task 
min_cpu_time = [111, 12, 2, 4, 7, 1, 2, 5, 2] # Minimum execution time units required for each task 
max_cpu_time = [118, 15, 62, 99, 80, 87, 124, 124, 9] # Maximum execution time units required for each task 
min_periodo_job = [5, 19, 7, 10, 10, 9, 5, 7, 19] # Minimum period required for each task 
max_periodo_job = [120, 96, 62, 124, 111, 74, 108, 74, 148] # Maximum period required for each task 
win_min = [0, 0, 0, 0, 0, 0, 0, 0, 0] # Execution window start point for each task 
win_max = [148, 148, 148, 148, 148, 148, 148, 148, 148] # Execution window finish point for each task 


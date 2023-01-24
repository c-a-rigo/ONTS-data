# Offline Nanosatellite Task Scheduling (ONTS) data for 97 time units and 24 tasks.
T = 97 # Units of time
J = 24 # Number of tasks
resource = [7.711445718, 7.861054014, 7.933549392, 7.926930918, 7.840275084, 7.674043644, 7.429929696, 7.110703764, 6.720521634, 6.909994692, 7.21644543, 7.467793524, 7.67204271, 8.068227642, 8.394841638, 8.648806338, 8.827659054, 8.930938032, 8.958643272, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.76238733, 7.128866088, 7.455172248, 7.733763828, 7.957714518, 8.12148327, 8.337276306, 8.63864775, 8.866908144, 9.019286964, 9.094706784, 9.093013686, 9.015285096, 8.863983702, 8.642803536, 8.356362138, 8.01066231, 7.612168608, 7.168423014, 6.6877371, 6.178884192, 5.650945452, 5.113309878, 4.662637974, 4.536117378, 4.329405504, 4.04650422, 3.692031066, 3.272142762, 2.7936117, 2.653700238, 2.88134496, 3.070356264, 3.652320222, 4.23120582, 4.797316224, 5.341262436, 5.853655458, 6.325721964, 6.749458218, 7.11716832, 7.422387714, 7.659113598] # Power available for tasks consumption for each unit of time
priority = [8, 14, 19, 6, 15, 10, 22, 2, 12, 1, 4, 11, 18, 9, 24, 7, 16, 3, 20, 13, 5, 17, 23, 21] # Priority of each task
consumption = [0.72, 1.38, 0.19, 1.15, 0.9, 1.06, 1.02, 0.65, 1.04, 1.25, 0.3, 0.76, 1.03, 1.1, 0.63, 1.2, 0.35, 0.97, 0.68, 1.09, 0.91, 0.53, 1.45, 1.16] # Power consumption of each task   
min_startup = [3, 1, 2, 3, 3, 3, 1, 3, 3, 1, 3, 1, 3, 1, 1, 1, 2, 2, 3, 3, 2, 1, 3, 3] # Minimum startups required for each task
max_startup = [3, 4, 2, 4, 5, 4, 5, 3, 3, 5, 5, 5, 4, 3, 5, 4, 6, 7, 5, 7, 4, 4, 5, 4] # Maximum startups required for each task
min_cpu_time = [3, 7, 5, 8, 4, 6, 6, 2, 6, 3, 2, 9, 3, 7, 4, 10, 9, 9, 9, 8, 1, 9, 7, 4] # Minimum execution time units required for each task
max_cpu_time = [5, 16, 18, 22, 10, 15, 22, 10, 22, 23, 9, 14, 9, 17, 15, 24, 15, 17, 13, 15, 13, 18, 10, 22] # Maximum execution time units required for each task
min_periodo_job = [16, 15, 23, 19, 4, 21, 24, 11, 23, 17, 12, 11, 13, 19, 22, 24, 9, 21, 17, 24, 22, 9, 12, 14] # Minimum period required for each task
max_periodo_job = [87, 46, 57, 46, 29, 73, 49, 53, 25, 58, 37, 46, 85, 87, 55, 78, 51, 51, 81, 66, 72, 38, 54, 64] # Maximum period required for each task
win_min = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0] # Execution window start point for each task
win_max = [97, 97, 97, 97, 97, 80, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97] # Execution window finish point for each task
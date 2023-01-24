# Offline Nanosatellite Task Scheduling (ONTS) data for 120 time units and 20 tasks.
T = 120 # Units of time
J = 20 # Number of tasks
resource = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.76238733, 7.128866088, 7.455172248, 7.733763828, 7.957714518, 8.12148327, 8.337276306, 8.63864775, 8.866908144, 9.019286964, 9.094706784, 9.093013686, 9.015285096, 8.863983702, 8.642803536, 8.356362138, 8.01066231, 7.612168608, 7.168423014, 6.6877371, 6.178884192, 5.650945452, 5.113309878, 4.662637974, 4.536117378, 4.329405504, 4.04650422, 3.692031066, 3.272142762, 2.7936117, 2.653700238, 2.88134496, 3.070356264, 3.652320222, 4.23120582, 4.797316224, 5.341262436, 5.853655458, 6.325721964, 6.749458218, 7.11716832, 7.422387714, 7.659113598, 7.823036268, 7.910461692, 7.918927182, 7.847663148, 7.696515672, 7.467023934, 7.161650622, 6.784551522, 6.86397321, 7.179966864, 7.442089218, 7.644645306, 8.005429098, 8.34543396, 8.613405198, 8.806572288, 8.92416564, 8.966031336, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.691123296, 7.065144036, 7.40037744] # Power available for tasks consumption for each unit of time
priority = [15, 13, 11, 1, 10, 18, 8, 6, 16, 12, 4, 3, 7, 17, 9, 5, 20, 14, 2, 19] # Priority of each task
consumption = [1.2, 0.44, 0.4, 0.63, 0.41, 0.15, 0.78, 1.17, 1.29, 0.82, 0.29, 1.01, 0.8, 0.22, 0.76, 0.6, 0.17, 0.65, 0.55, 0.57] # Power consumption of each task
min_startup = [1, 3, 1, 1, 1, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 2, 2, 1, 1] # Minimum startups required for each task
max_startup = [4, 8, 5, 5, 8, 7, 8, 6, 4, 8, 8, 5, 3, 7, 6, 6, 6, 5, 3, 4] # Maximum startups required for each task
min_cpu_time = [2, 2, 6, 12, 2, 6, 1, 8, 5, 2, 11, 1, 11, 10, 8, 5, 6, 4, 8, 12] # Minimum execution time units required for each task
max_cpu_time = [15, 29, 10, 25, 4, 29, 16, 29, 28, 17, 28, 11, 20, 26, 14, 9, 16, 15, 26, 23] # Maximum execution time units required for each task
min_periodo_job = [27, 23, 21, 27, 22, 12, 12, 29, 12, 26, 21, 1, 18, 21, 20, 17, 28, 24, 16, 23] # Minimum period required for each task
max_periodo_job = [89, 44, 114, 29, 91, 120, 19, 112, 95, 117, 104, 38, 95, 77, 118, 38, 103, 102, 43, 96] # Maximum period required for each task
win_min = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23] # Execution window start point for each task
win_max = [120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 96, 120, 120, 120, 120, 120, 120, 120, 120] # Execution window finish point for each task
# Offline Nanosatellite Task Scheduling (ONTS) data for 170 time units and 24 tasks.
T = 170 # Units of time
J = 24 # Number of tasks
resource = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.76238733, 7.128866088, 7.455172248, 7.733763828, 7.957714518, 8.12148327, 8.337276306, 8.63864775, 8.866908144, 9.019286964, 9.094706784, 9.093013686, 9.015285096, 8.863983702, 8.642803536, 8.356362138, 8.01066231, 7.612168608, 7.168423014, 6.6877371, 6.178884192, 5.650945452, 5.113309878, 4.662637974, 4.536117378, 4.329405504, 4.04650422, 3.692031066, 3.272142762, 2.7936117, 2.653700238, 2.88134496, 3.070356264, 3.652320222, 4.23120582, 4.797316224, 5.341262436, 5.853655458, 6.325721964, 6.749458218, 7.11716832, 7.422387714, 7.659113598, 7.823036268, 7.910461692, 7.918927182, 7.847663148, 7.696515672, 7.467023934, 7.161650622, 6.784551522, 6.86397321, 7.179966864, 7.442089218, 7.644645306, 8.005429098, 8.34543396, 8.613405198, 8.806572288, 8.92416564, 8.966031336, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.691123296, 7.065144036, 7.40037744, 7.689435444, 7.925083902, 8.101627848, 8.26924455, 8.585084286, 8.828582562, 8.996661018, 9.087780474, 9.101633094, 9.039450222, 8.902924956, 8.695905246, 8.422700796, 8.088698736, 7.700825376, 7.266007026, 6.792709176, 6.289551234, 5.765306526, 5.229671886, 4.691882394, 4.573827288, 4.383276804, 4.115459484, 3.775300704, 3.368341512, 2.901508218, 2.583821466, 2.827011906, 2.989549314, 3.527338806, 4.10730183, 4.676336676, 5.224900428, 5.743911924, 6.224136084, 6.657569172, 7.036515288, 7.354048122, 7.604164872, 7.782247998, 7.88444955, 7.908152922, 7.851972852, 7.71590934] # Power available for tasks consumption for each unit of time
priority = [10, 12, 4, 17, 2, 6, 20, 24, 13, 7, 19, 1, 18, 5, 8, 15, 22, 11, 14, 16, 21, 9, 3, 23] # Priority of each task
consumption = [1.09, 0.27, 0.71, 0.47, 0.22, 1.36, 0.25, 0.34, 1.31, 0.45, 0.57, 0.24, 1.09, 1.46, 0.96, 0.51, 1.2, 0.96, 0.58, 0.62, 0.9, 0.43, 1.48, 0.58] # Power consumption of each task 
min_startup = [4, 2, 2, 2, 2, 1, 1, 2, 1, 4, 3, 3, 1, 4, 4, 2, 1, 4, 4, 2, 3, 1, 2, 2] # Minimum startups required for each task
max_startup = [11, 10, 6, 12, 9, 8, 4, 3, 6, 9, 9, 12, 3, 4, 10, 10, 5, 5, 5, 9, 4, 9, 10, 2] # Maximum startups required for each task
min_cpu_time = [3, 14, 10, 11, 1, 3, 5, 12, 6, 11, 7, 6, 17, 12, 9, 15, 3, 8, 5, 5, 10, 12, 17, 5] # Minimum execution time units required for each task
max_cpu_time = [40, 36, 24, 15, 8, 11, 33, 21, 29, 18, 16, 31, 19, 20, 25, 41, 30, 11, 19, 33, 14, 19, 39, 12] # Maximum execution time units required for each task
min_periodo_job = [12, 27, 43, 16, 5, 41, 24, 15, 15, 33, 25, 17, 17, 26, 18, 15, 31, 27, 7, 36, 34, 19, 30, 14] # Minimum period required for each task
max_periodo_job = [102, 99, 132, 96, 73, 110, 93, 133, 88, 46, 124, 142, 110, 129, 164, 100, 70, 84, 49, 42, 98, 36, 47, 113] # Maximum period required for each task
win_min = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13] # Execution window start point for each task
win_max = [170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 143, 170, 170, 170, 170] # Execution window finish point for each task
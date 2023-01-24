# Offline Nanosatellite Task Scheduling (ONTS) data for 154 time units and 18 tasks.
T = 154 # Units of time
J = 18 # Number of tasks
resource = [7.840275084, 7.674043644, 7.429929696, 7.110703764, 6.720521634, 6.909994692, 7.21644543, 7.467793524, 7.67204271, 8.068227642, 8.394841638, 8.648806338, 8.827659054, 8.930938032, 8.958643272, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.76238733, 7.128866088, 7.455172248, 7.733763828, 7.957714518, 8.12148327, 8.337276306, 8.63864775, 8.866908144, 9.019286964, 9.094706784, 9.093013686, 9.015285096, 8.863983702, 8.642803536, 8.356362138, 8.01066231, 7.612168608, 7.168423014, 6.6877371, 6.178884192, 5.650945452, 5.113309878, 4.662637974, 4.536117378, 4.329405504, 4.04650422, 3.692031066, 3.272142762, 2.7936117, 2.653700238, 2.88134496, 3.070356264, 3.652320222, 4.23120582, 4.797316224, 5.341262436, 5.853655458, 6.325721964, 6.749458218, 7.11716832, 7.422387714, 7.659113598, 7.823036268, 7.910461692, 7.918927182, 7.847663148, 7.696515672, 7.467023934, 7.161650622, 6.784551522, 6.86397321, 7.179966864, 7.442089218, 7.644645306, 8.005429098, 8.34543396, 8.613405198, 8.806572288, 8.92416564, 8.966031336, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.691123296, 7.065144036, 7.40037744, 7.689435444, 7.925083902, 8.101627848, 8.26924455] # Power available for tasks consumption for each unit of time
priority = [10, 8, 9, 12, 2, 11, 15, 17, 5, 4, 1, 16, 6, 13, 18, 3, 14, 7] # Priority of each task
consumption = [0.02, 0.45386, 0.09231, 0.38155, 0.30924, 0.45386, 0.23693, 0.02, 0.2377848, 0.6, 0.75093, 1.715323, 0.826186, 1.223478, 0.92186, 1.44558, 1.65651, 1.20465] # Power consumption of each task
min_startup = [15, 20, 13, 21, 12, 20, 13, 12, 18, 4, 6, 3, 6, 5, 8, 5, 3, 4] # Minimum startups required for each task
max_startup = [34, 99, 81, 63, 111, 25, 20, 77, 69, 10, 11, 16, 26, 31, 40, 24, 29, 5] # Maximum startups required for each task
min_cpu_time = [5, 5, 3, 3, 4, 4, 2, 3, 2, 10, 13, 13, 15, 14, 12, 15, 13, 14] # Minimum execution time units required for each task
max_cpu_time = [7, 7, 4, 7, 6, 5, 5, 3, 3, 79, 15, 80, 94, 31, 39, 37, 24, 91] # Maximum execution time units required for each task
min_periodo_job = [5, 5, 8, 5, 6, 7, 7, 3, 7, 18, 15, 15, 19, 15, 14, 17, 16, 14] # Minimum period required for each task
max_periodo_job = [13, 18, 22, 13, 19, 24, 29, 21, 17, 69, 58, 106, 133, 48, 15, 110, 76, 35] # Maximum period required for each task
win_min = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Execution window start point for each task
win_max = [155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155, 155] # Execution window finish point for each task
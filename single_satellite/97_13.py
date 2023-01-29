# Offline Nanosatellite Task Scheduling (ONTS) data for 97 time units and 13 tasks.
T = 97 # Units of time
J = 13 # Number of tasks
resource = [9.055149858, 9.09886257, 9.0657702, 8.957411928, 8.776866114, 8.527980708, 8.21614284, 7.847355312, 7.428698352, 6.96786786, 6.473637162, 5.954625666, 5.42022237, 4.879816272, 4.610305854, 4.450846806, 4.212581742, 3.899666448, 3.517488054, 3.07220328, 2.571354108, 2.784530538, 2.980929906, 3.319857342, 3.902283054, 4.477782456, 5.03696655, 5.57029242, 6.068678904, 6.523506594, 6.926771754, 7.271548074, 7.551370998, 7.761007314, 7.896147318, 7.95371265, 7.931856294, 7.829962578, 7.648801092, 7.390218852, 7.0571403, 6.654029058, 6.954323076, 7.250923062, 7.49118906, 7.744999842, 8.128255662, 8.441478792, 8.681283036, 8.845975296, 8.9349399, 8.948638602, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.809794074, 6.832112184, 7.190895042, 7.507966122, 7.775783442, 7.987882446, 8.138722086, 8.40238362, 8.689132854, 8.902155366, 9.03883455] # Power available for tasks consumption for each unit of time
priority = [7, 10, 13, 9, 11, 12, 1, 6, 5, 2, 8, 4, 3] # Priority of each task
consumption = [0.30924, 0.23693, 0.23693, 0.16462, 0.45386, 0.09231, 0.45386, 0.30924, 0.30924, 0.6, 0.6, 0.7093, 0.8186] # Power consumption of each task
min_startup = [13, 10, 9, 8, 8, 13, 9, 12, 11, 5, 2, 5, 5] # Minimum startups required for each task
max_startup = [54, 45, 71, 55, 74, 64, 50, 52, 71, 6, 3, 16, 21] # Maximum startups required for each task
min_cpu_time = [2, 2, 1, 3, 2, 3, 1, 2, 2, 5, 7, 10, 7] # Minimum execution time units required for each task
max_cpu_time = [5, 4, 5, 4, 3, 4, 5, 5, 4, 30, 22, 43, 24] # Maximum execution time units required for each task
min_periodo_job = [5, 6, 2, 3, 4, 4, 2, 4, 5, 9, 9, 11, 11] # Minimum period required for each task
max_periodo_job = [10, 7, 2, 10, 5, 10, 9, 8, 6, 45, 57, 36, 87] # Maximum period required for each task
win_min = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Execution window start point for each task
win_max = [97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97] # Execution window finish point for each task
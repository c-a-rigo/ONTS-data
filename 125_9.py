# Offline Nanosatellite Task Scheduling (ONTS) data for 125 time units and 9 tasks.
T = 125 # Units of time
J = 9 # Number of tasks
resource = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.754383594, 6.900297858, 7.25107698, 7.558451226, 7.815340368, 8.015433768, 8.153190378, 8.464566492, 8.736539598, 8.934016392, 9.055149858, 9.09886257, 9.0657702, 8.957411928, 8.776866114, 8.527980708, 8.21614284, 7.847355312, 7.428698352, 6.96786786, 6.473637162, 5.954625666, 5.42022237, 4.879816272, 4.610305854, 4.450846806, 4.212581742, 3.899666448, 3.517488054, 3.07220328, 2.571354108, 2.784530538, 2.980929906, 3.319857342, 3.902283054, 4.477782456, 5.03696655, 5.57029242, 6.068678904, 6.523506594, 6.926771754, 7.271548074, 7.551370998, 7.761007314, 7.896147318, 7.95371265, 7.931856294, 7.829962578, 7.648801092, 7.390218852, 7.0571403, 6.654029058, 6.954323076, 7.250923062, 7.49118906, 7.744999842, 8.128255662, 8.441478792, 8.681283036, 8.845975296, 8.9349399, 8.948638602, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.809794074, 6.832112184, 7.190895042] # Power available for tasks consumption for each unit of time
priority = [5, 9, 5, 3, 3, 4, 1, 3, 2] # Priority of each task
consumption = [2.4, 2.4, 2.4, 3.4, 3.4, 1.4, 1.4, 2.4, 2.4] # Power consumption of each task
min_startup = [1, 2, 2, 2, 2, 1, 2, 2, 2] # Minimum startups required for each task
max_startup = [12, 9, 11, 9, 13, 12, 3, 15, 13] # Maximum startups required for each task
min_cpu_time = [60, 8, 31, 24, 34, 11, 91, 29, 75] # Minimum execution time units required for each task
max_cpu_time = [90, 48, 111, 79, 52, 115, 107, 67, 104] # Maximum execution time units required for each task
min_periodo_job = [74, 12, 86, 40, 46, 62, 101, 84, 83] # Minimum period required for each task
max_periodo_job = [105, 113, 92, 87, 109, 66, 113, 115, 98] # Maximum period required for each task
win_min = [0, 0, 0, 0, 0, 8, 0, 0, 0] # Execution window start point for each task
win_max = [126, 221, 126, 126, 126, 98, 126, 126, 126] # Execution window finish point for each task
subs = 5
J = 10
T = 96

constellation = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0] # Flag to indicate if job is constellation job or not
sincronous = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0] # Flag to indicate if job should run sincronously in all spacecrafts

# Global number of startups 
min_startup_g = [2, 2, 3, 3, 2, 1, 1, 1, 1, 2] 
max_startup_g = [40, 23, 18, 37, 40, 35, 37, 30, 38, 32]

consumption = [[2.81, 0.59, 1.51, 2.44, 2.88, 0.68, 1.46, 2.95, 1.95, 2.34], [2.81, 0.59, 1.51, 2.44, 2.88, 2.47, 2.26, 1.69, 1.18, 2.29], [2.81, 0.59, 1.51, 2.44, 2.88, 1.74, 3.0, 0.92, 2.43, 2.15], [2.81, 0.59, 1.51, 2.44, 2.88, 2.4, 2.99, 1.71, 1.25, 1.88], [2.81, 0.59, 1.51, 2.44, 2.88, 1.32, 2.38, 1.87, 1.81, 0.94]]
resource = [[8.214103503, 8.097469133, 7.974593102, 7.844128107, 7.704448717, 7.553694502, 7.389818793, 7.210642167, 7.013909687, 6.797350827, 6.65902188, 6.783656439, 7.0317728, 7.276791468, 7.516515919, 7.748406332, 7.969616133, 8.177035556, 8.367341486, 8.537052757, 8.682589961, 8.800338756, 8.886715568, 8.938234573, 8.93128945, 8.927497444, 8.972869206, 8.932053307, 8.837944403, 8.69090514, 8.489853233, 8.234285124, 7.924300238, 7.560616383, 7.144576015, 6.678143174, 6.702589141, 7.181057673, 7.612506009, 7.992377758, 8.316541862, 8.581352043, 8.783699942, 8.921061147, 8.991533353, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.11588341, 7.583410583, 7.993868524, 8.34451899, 8.633256824, 8.858629221, 9.01984578, 9.116779215, 9.129723666, 9.049480412, 8.910340298, 8.715101188, 8.467053387, 8.169924949, 7.827821553, 7.445161928, 7.026609864, 6.57700392, 6.421086959, 6.661483349, 7.019358017, 7.409194026, 7.755678783, 8.059289558, 8.320979449, 8.542136675, 8.724537694, 8.870294995, 8.981800537, 9.061665839, 9.112659815, 9.137645452, 9.125485882, 9.092349434, 9.043928891, 8.982682467, 8.910827593, 8.830298524, 8.742710577, 8.649331618, 8.551061311, 8.448418473, 8.341536771], [8.537052757, 8.682589961, 8.800338756, 8.886715568, 8.938234573, 8.93128945, 8.927497444, 8.972869206, 8.932053307, 8.837944403, 8.69090514, 8.489853233, 8.234285124, 7.924300238, 7.560616383, 7.144576015, 6.678143174, 6.702589141, 7.181057673, 7.612506009, 7.992377758, 8.316541862, 8.581352043, 8.783699942, 8.921061147, 8.991533353, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.11588341, 7.583410583, 7.993868524, 8.34451899, 8.633256824, 8.858629221, 9.01984578, 9.116779215, 9.129723666, 9.049480412, 8.910340298, 8.715101188, 8.467053387, 8.169924949, 7.827821553, 7.445161928, 7.026609864, 6.57700392, 6.421086959, 6.661483349, 7.019358017, 7.409194026, 7.755678783, 8.059289558, 8.320979449, 8.542136675, 8.724537694, 8.870294995, 8.981800537, 9.061665839, 9.112659815, 9.137645452, 9.125485882, 9.092349434, 9.043928891, 8.982682467, 8.910827593, 8.830298524, 8.742710577, 8.649331618, 8.551061311, 8.448418473, 8.341536771, 8.230168797, 8.113698475, 7.991161534, 7.861273689, 7.722466002, 7.572926785, 7.410649259, 7.23348412, 7.039196017, 6.825522928, 6.668823064, 6.751801046, 6.999793839, 7.244963624, 7.485185344, 7.717985805, 7.940578794, 8.149907297, 8.342692137], [7.612506009, 7.992377758, 8.316541862, 8.581352043, 8.783699942, 8.921061147, 8.991533353, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.11588341, 7.583410583, 7.993868524, 8.34451899, 8.633256824, 8.858629221, 9.01984578, 9.116779215, 9.129723666, 9.049480412, 8.910340298, 8.715101188, 8.467053387, 8.169924949, 7.827821553, 7.445161928, 7.026609864, 6.57700392, 6.421086959, 6.661483349, 7.019358017, 7.409194026, 7.755678783, 8.059289558, 8.320979449, 8.542136675, 8.724537694, 8.870294995, 8.981800537, 9.061665839, 9.112659815, 9.137645452, 9.125485882, 9.092349434, 9.043928891, 8.982682467, 8.910827593, 8.830298524, 8.742710577, 8.649331618, 8.551061311, 8.448418473, 8.341536771, 8.230168797, 8.113698475, 7.991161534, 7.861273689, 7.722466002, 7.572926785, 7.410649259, 7.23348412, 7.039196017, 6.825522928, 6.668823064, 6.751801046, 6.999793839, 7.244963624, 7.485185344, 7.717985805, 7.940578794, 8.149907297, 8.342692137, 8.515486221, 8.664733456, 8.786831357, 8.878196244, 8.935329929, 8.94021539, 8.926053278, 8.966032775, 8.939650498, 8.854042377, 8.715837243, 8.523857084, 8.277496167, 7.976746799, 7.622216334, 7.215135105, 6.757355064, 6.676293496, 7.105308387], [8.34451899, 8.633256824, 8.858629221, 9.01984578, 9.116779215, 9.129723666, 9.049480412, 8.910340298, 8.715101188, 8.467053387, 8.169924949, 7.827821553, 7.445161928, 7.026609864, 6.57700392, 6.421086959, 6.661483349, 7.019358017, 7.409194026, 7.755678783, 8.059289558, 8.320979449, 8.542136675, 8.724537694, 8.870294995, 8.981800537, 9.061665839, 9.112659815, 9.137645452, 9.125485882, 9.092349434, 9.043928891, 8.982682467, 8.910827593, 8.830298524, 8.742710577, 8.649331618, 8.551061311, 8.448418473, 8.341536771, 8.230168797, 8.113698475, 7.991161534, 7.861273689, 7.722466002, 7.572926785, 7.410649259, 7.23348412, 7.039196017, 6.825522928, 6.668823064, 6.751801046, 6.999793839, 7.244963624, 7.485185344, 7.717985805, 7.940578794, 8.149907297, 8.342692137, 8.515486221, 8.664733456, 8.786831357, 8.878196244, 8.935329929, 8.94021539, 8.926053278, 8.966032775, 8.939650498, 8.854042377, 8.715837243, 8.523857084, 8.277496167, 7.976746799, 7.622216334, 7.215135105, 6.757355064, 6.676293496, 7.105308387, 7.54476926, 7.933478548, 8.267231388, 8.542296561, 8.755470758, 8.904125876, 8.986248592, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.026149734, 7.503462416, 7.924301254], [7.755678783, 8.059289558, 8.320979449, 8.542136675, 8.724537694, 8.870294995, 8.981800537, 9.061665839, 9.112659815, 9.137645452, 9.125485882, 9.092349434, 9.043928891, 8.982682467, 8.910827593, 8.830298524, 8.742710577, 8.649331618, 8.551061311, 8.448418473, 8.341536771, 8.230168797, 8.113698475, 7.991161534, 7.861273689, 7.722466002, 7.572926785, 7.410649259, 7.23348412, 7.039196017, 6.825522928, 6.668823064, 6.751801046, 6.999793839, 7.244963624, 7.485185344, 7.717985805, 7.940578794, 8.149907297, 8.342692137, 8.515486221, 8.664733456, 8.786831357, 8.878196244, 8.935329929, 8.94021539, 8.926053278, 8.966032775, 8.939650498, 8.854042377, 8.715837243, 8.523857084, 8.277496167, 7.976746799, 7.622216334, 7.215135105, 6.757355064, 6.676293496, 7.105308387, 7.54476926, 7.933478548, 8.267231388, 8.542296561, 8.755470758, 8.904125876, 8.986248592, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.026149734, 7.503462416, 7.924301254, 8.285817624, 8.585790555, 8.822647652, 8.995476839, 9.104028802, 9.137890854, 9.068638877, 8.940055409, 8.754838004, 8.516185484, 8.227744452, 7.893550212, 7.517963049, 7.10560092, 6.661269625, 6.42279104, 6.601231242, 6.943343233, 7.341237467]]

min_cpu_time = [[8, 1, 5, 10, 2, 8, 8, 8, 9, 6], [8, 1, 5, 10, 2, 10, 10, 5, 4, 9], [8, 1, 5, 10, 2, 9, 6, 7, 8, 5], [8, 1, 5, 10, 2, 2, 1, 1, 7, 3], [8, 1, 5, 10, 2, 10, 2, 5, 5, 5]]
max_cpu_time = [[19, 6, 21, 14, 3, 8, 17, 23, 21, 23], [19, 6, 21, 14, 3, 18, 11, 21, 4, 14], [19, 6, 21, 14, 3, 21, 13, 11, 14, 6], [19, 6, 21, 14, 3, 23, 14, 11, 7, 9], [19, 6, 21, 14, 3, 18, 17, 22, 7, 18]]
min_periodo_job = [[22, 9, 23, 17, 18, 17, 22, 24, 24, 24], [22, 9, 23, 17, 18, 24, 16, 22, 9, 24], [22, 9, 23, 17, 18, 23, 24, 24, 22, 23], [22, 9, 23, 17, 18, 24, 20, 19, 9, 14], [22, 9, 23, 17, 18, 22, 20, 23, 21, 24]]
max_periodo_job = [[72, 30, 88, 59, 82, 83, 37, 79, 40, 80], [72, 30, 88, 59, 82, 31, 27, 86, 71, 43], [72, 30, 88, 59, 82, 94, 71, 82, 68, 46], [72, 30, 88, 59, 82, 52, 21, 36, 40, 68], [72, 30, 88, 59, 82, 86, 63, 81, 60, 84]]
min_statup = [[0, 2, 0, 2, 2, 1, 2, 2, 2, 2], [0, 2, 0, 2, 2, 3, 1, 3, 3, 2], [0, 2, 0, 2, 2, 2, 1, 3, 3, 3], [0, 2, 0, 2, 2, 2, 2, 2, 2, 3], [0, 2, 0, 2, 2, 2, 2, 3, 3, 2]]
max_statup = [[9, 5, 4, 8, 8, 3, 9, 5, 4, 5], [9, 5, 4, 8, 8, 5, 8, 5, 8, 6], [9, 5, 4, 8, 8, 9, 4, 5, 9, 5], [9, 5, 4, 8, 8, 9, 5, 6, 9, 5], [9, 5, 4, 8, 8, 8, 9, 8, 6, 9]]

win_max = [[100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]]
win_min = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
priority = [[1, 10, 4, 8, 2, 3, 9, 6, 5, 1, 10],[1, 10, 4, 8, 2, 3, 9, 6, 5, 1, 10],[1, 10, 4, 8, 2, 3, 9, 6, 5, 1, 10],[1, 10, 4, 8, 2, 3, 9, 6, 5, 1, 10],[1, 10, 4, 8, 2, 3, 9, 6, 5, 1, 10]]

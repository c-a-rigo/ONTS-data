# ONTS-data
This data set comprises examples of the Offline Nanosatellite Task Scheduling (ONTS) problem, which was generated based on the FloripaSat-I CubeSat project. The instances provide information time set, tasks . The resource variable provides the power available for each time unit and is calculated using the FloripaSat-I mission orbital parameters and realistic power harvesting calculations. The instances in this data set are intended to be scalable in difficulty and may be used to compare the performance of various ONTS solution techniques. The data is delivered in the form of a Python list, which may be readily imported and utilized in other Python scripts.

The data is freely available to other researchers, who may use it to assess their own methodologies and compare their findings to those described in the journal. The information is supplied "as is" and may have restrictions or assumptions. By providing a common starting point for future investigations, we urge researchers to use the data and report any concerns or feedback to improve the field's research.

Please cite the following paper when using this data set:

#### BibTex
```bibtex
@misc{ONTS-data,
title = {Title},
author = {Authors},
url = {https://github.com/c-a-rigo/ONTS-data}
}
```
To use this data set, you will need to have python installed on your computer. 

Each example in the single satellite folder contains the following keys:

### Example file
The (T)\_(jobs).py file is a Python file containing the following data defining an instance:

| Variable (Code) 	| Variable (Paper)	| Definition		|
|-------------------|-------------------|-------------------|
| J 				| $J$				| number of jobs
| T 				| $T$				| time horizon
| resource 		| $r_t$				| vector containing the available resource for each time instant
| min_cpu_time 		| $t_j^{\min}$		| vector containing the minimum duration of each job
| max_cpu_time 		| $t_j^{\max}$		| vector containing the maximum duration of each job
| min_period_job 	| $p_j^{\min}$		| vector containing the minimum period for each job
| max_period_job 	| $p_j^{\max}$		| vector containing the maximum period for each job
| min_startup 		| $y_j^{\min}$		| vector containing the minimum number of startups for each job
| max_startup 		| $y_j^{\max}$		| vector containing the maximum number of startups for each job
| win_min 			| $w_j^{\min}$		| minimum time window for each job
| win_max 			| $w_j^{\max}$		| maximum time window for each job
| priority 			| $u_j$				| vector containing the priority of each job
| consumption 			| $q_j$				| vector containing the power usage of each job



### Battery parameters file
The battery parameters contains the following definitions:

| Variable (Code) 	| Variable (Paper)	| Definition		|
|-------------------|-------------------|-------------------|
| q 				| $Q$				| nominal battery capacity (in Ah) 
| soc0		 		| $SoC_1$			| initial battery SoC
| lower_bound		| $\rho$			| minimum accepted battery SoC
| bat_usage 		| $\gamma$			| maximum charge/discharge battery current (in Ampéres)
| ef 				| $e$				| battery charge/discharge efficiency
| v_bat 			| $V_b$				| battery voltage

Please make sure to read the paper and understand the data format and usage before using this data in your research.

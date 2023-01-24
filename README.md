# ONTS-data
This data set comprises examples of the Offline Nanosatellite Task Scheduling (ONTS) problem, which was generated based on the FloripaSat-I CubeSat project. The instances provide information time set, tasks . The resource variable provides the power available for each time unit and is calculated using the FloripaSat-I mission orbital parameters and realistic power harvesting calculations. The instances in this data set are intended to be scalable in difficulty and may be used to compare the performance of various ONTS solution techniques. The data is delivered in the form of a Python list, which may be readily imported and utilized in other Python scripts.

The data is freely available to other researchers, who may use it to assess their own methodologies and compare their findings to those described in the journal. The information is supplied "as is" and may have restrictions or assumptions. By providing a common starting point for future investigations, we urge researchers to use the data and report any concerns or feedback to improve the field's research.

Please cite the following paper when using this data set:

**[Name of the Paper and authors]**

To use this data set, you will need to have python installed on your computer. 

Each example the following keys:

+ T : an integer, representing the number of time units
+ J: an integer representing the number of tasks
+ resource: a list of T elements, representing the power availability for each time unit
+


Please make sure to read the paper and understand the data format and usage before using this data in your research.

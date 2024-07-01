Objective: Develop a web application to facilitate digitalizing the hospitality process for group accommodation. The application should allow users to upload two CSV files to efficiently allocate rooms in hostels while ensuring group members with the same ID stay together and adhere to hostel capacities and gender-specific accommodations.
Instructions and Guidelines
Technical Details:
1. CSV File 1 (Group Information):
Contains information about groups with a common ID.
Each row represents a group, specifying the group ID, the number of members, and the gender (boys or girls).
There can be various scenarios under the same registration ID: groups of different sizes such as 2, 3, 4, 5, 6, or 7 people or more; groups consisting only of boys or girls; and groups containing both boys and girls under the same registration ID.

Group ID	Members	Gender
101	               3	             Boys
102	               4	              Girls
103	               2	              Boys
104	               5	             Girls
105                     8               5 Boys & 3 Girls


2. CSV File 2 (Hostel Information)
Contains information about the hostels and their room capacities.
Each row represents a hostel room, specifying the hostel name, room number, room capacity, and gender accommodation (boys or girls).
Example
              Hostel Name	    Room Number	Capacity	Gender
            Boys Hostel A	           101	                  3	             Boys
           Boys Hostel A	          102	                  4	             Boys
            Girls Hostel B	          201	                  2	             Girls
            Girls Hostel B	           202	                  5	              Girls


3. Frontend Requirements:
User-friendly interface to upload two CSV files.
An algorithm to allocate rooms based on the following criteria:
Members of the same group (same ID) should stay in the same room as much as possible.
Boys and girls should stay in their respective hostels.
Room capacity should not be exceeded.
4. Output:
A display of the allocated rooms indicating which group members are in which room.
A downloadable CSV file with the allocation details.
Example output

Group ID	   Hostel Nam          Room Number       Members Allocated
 101	              Boys Hostel A	         101	                    3
102	             Girls Hostel B                    202	                    4
103	             Boys Hostel A	          102	                    2
104	             Girls Hostel B	           202	                     5


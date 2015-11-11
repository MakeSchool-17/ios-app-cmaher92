#App Design Document
Groundflow - Irrigation workflow and customer management software.

##Objective
The objective of Groundflow is to sync the office staff with the technicians in the field by handling scheduling, inventory usage, time tracking, and data collection.


##Audience
Our audience is specific to the residential irrigation industry, targetting their core issues in the office & the field.


##Experience
The typical workflow is as follows.
- The office receives a call from a client and then schedules the new job into the calendar.
- The technician then looks at his device on the day of the job and can see all jobs for that day.
- The technician can select his first job and route to the job.
- The technician then can TIME - IN once arrived at the job.
- The technician can note parts that he uses as he works on the job, allowing for extremely accurate parts usage.
- The technician then can time out, mark as complete if done, flag if needs to be finished at a later date.
- The office can then invoice based on accurate information, and if needed call the customer to schedule additional needed time.


##Technical
The current planned stack is as follows:
iOS:
Realm (data persistance to local device)
Swift 2.0

Back-end:
Django
Python
MariaDB

Web:
Django
HTML / CSS

####External Services
Potential google calendar integration.

####Screens
9 screens, will post shortly.

####Views / View Controllers/ Classes

####Data Models
Objects:
Company
Customer
Job
Employee (user):
Time

Will post a web version of the data-model once finalized.

##MVP Milestones
11/11/2015 - MVP object-model finalized (as close as possible).
11/11/2015 - Database created.
11/13/2015 - Basic UI done with data persistance using dummy data and Realm.


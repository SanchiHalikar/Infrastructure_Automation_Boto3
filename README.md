#Automate Infrastructure Using Boto3
Wrote a python script in AWS lambda to automate the Start and Stop of EC2 instances.
The lambda function is triggered using CloudWatch Events. Cloud Watch Events are scheduled at 12 a.m night to stop the instance and Start(Spin up) again in 9a.m
Created two other functions to create a snapshot and delete a snapshot.
These functions are also triggered using AWS CloudWatch Events.
If the snapshot is older than 30days the lambda function will go ahead and delete that particular snapshot.
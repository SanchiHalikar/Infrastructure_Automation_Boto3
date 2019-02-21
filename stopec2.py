import boto3
import collections
import datetime
client=boto3.client('ec2')                                #every Ec2 instance is considered as client

def lambda_handler(event, context):


    #We can have describe instance, since before stopping an instance you need to know what instance are running

    response=client.describe_instances()                 
    
     #Each description (response) has a reservation (looping through reservation)
     #For instance in reservation (for each reservation loop through the instance id to find the instanceID)



    for reservation in response["Reservations"]:        
    
        for instance in reservation["Instances"]:          
        
            print(instance["InstanceId"]+ "stopping")
            
            
            #take the instance id of the instance and storing in variable id
            #instances has to be list so making id as list
    
            id=[instance["InstanceId"]]
            
            response2 = client.stop_instances(InstanceIds=id)
            print response2
  
            
           
    return("Success")
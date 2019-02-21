import boto3
client=boto3.client('ec2')                                

#every Ec2 instance is taken as client

def lambda_handler(event, context):
    
    response=client.describe_instances()                 
    #We can have describe instance, since before stopping an instance you need to know what instance are running
	#Each description (response) has a reservation (looping through reservation)
    #for instance in reservation (for each reservation loop through the instance id to find the instanceID)
	
    for reservation in response["Reservations"]:         
	
    
        for instance in reservation["Instances"]:          
        
            print(instance["InstanceId"]+ "starting")
		
            #instances has to be list so making id as list
    
            id=[instance["InstanceId"]]   
            
            client.start_instances(InstanceIds=id)

            
            
           
    return("Success")
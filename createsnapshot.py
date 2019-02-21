import boto3 
import collections
import datetime

ec2 = boto3.client('ec2')
def lambda_handler(event, context): 
    reservations = ec2.describe_volumes()
    print(reservations)

    for volume in reservations['Volumes']:
        

        reservations = ec2.create_snapshot(VolumeId=volume['VolumeId'])
        result = reservations["SnapshotId"]
        print(result)
        print('Snapshot with ID {} was created' .format(result))
        ec2.create_tags(
        Resources=[result],Tags=[{'Key': 'Name', 'Value': 'snapshot' },])
        

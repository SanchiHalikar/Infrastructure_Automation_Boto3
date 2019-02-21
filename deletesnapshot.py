import boto3 
import collections 
import datetime
ec2 = boto3.client('ec2')
 
 
def lambda_handler(event, context): 
    reservations = ec2.describe_snapshots( Filters=[ {'Name': 'tag-key', 'Values': ['Name', 'snapshot']},] ) #specifing only specific tagged snapshots
    print(reservations)
 
    current_time= datetime.datetime.today().strftime('%Y%m%d')
    print current_time
    current_time = int(current_time)
    
 
    retention = 30
 
    for snapshot in reservations['Snapshots']:
        print "Checking snapshot %s which was created on %s" % (snapshot['SnapshotId'],snapshot['StartTime'])
 

        x = snapshot['StartTime'].strftime('%Y%m%d')
        print(x)
        snaptime = int(x)
        print snaptime 
        Difference = current_time - snaptime
        print Difference
        if Difference > retention:
            print "The snapshot older than thirty days. Deleting Now"
            ec2.delete_snapshot(SnapshotId= snapshot['SnapshotId'])
        else:
            print "Snapshot is newer than configured retention of %d days so we keep it" % (retention)
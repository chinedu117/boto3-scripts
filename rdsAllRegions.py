import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv(".env")

boto3.setup_default_session(profile_name=os.environ.get("AWS_PROFILE"))
def main():
    # Pre requisite - ensure you have RDS Read Access
    available_regions = boto3.Session().get_available_regions('rds')
    # Loop through all regions
    for region in available_regions:
        try:
            rdsClient = boto3.client('rds', region_name=region)
            allDatabases = rdsClient.describe_db_instances()
            for db in allDatabases['DBInstances']:
                print('%s: %s' % (region, db['DBInstanceIdentifier']))
            # Save all regions file for all databases
            fileName = 'rds_regions/%s.json' % region
            with open(fileName, 'w') as f:
                json.dump(allDatabases, f, indent=4, default=str)
        except Exception as e:
            print(e)
            if 'InvalidClientTokenId' in e.response['Error']['Code']:
                pass
            else:
                print(e)

if __name__ == '__main__':
    main()

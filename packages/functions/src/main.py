import boto3
import logging

logger = logging.getLogger("function-s3-empty")
logger.setLevel(logging.INFO)

def empty_bucket(bucket_name):
    s3 = boto3.client('s3')
    try:
        object_list = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in object_list:
            for obj in object_list['Contents']:
                logger.info(f"Deleting object: {obj['Key']}")
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
        else:
            pass
            
        versioning = s3.get_bucket_versioning(Bucket=bucket_name)
        if versioning.get('Status') == 'Enabled':
            version_list = s3.list_object_versions(Bucket=bucket_name)
            if 'Versions' in version_list:
                for version in version_list['Versions']:
                    logger.info(f"Deleting object version: {version['Key']} VersionId: {version['VersionId']}")
                    s3.delete_object(Bucket=bucket_name, Key=version['Key'], VersionId=version['VersionId'])     
            if 'DeleteMarkers' in version_list:
                for delete_marker in version_list['DeleteMarkers']:
                    logger.info(f"Deleting delete marker: {delete_marker['Key']} VersionId: {delete_marker['VersionId']}")
                    s3.delete_object(Bucket=bucket_name, Key=delete_marker['Key'], VersionId=delete_marker['VersionId'])

    except Exception as e:
        logger.error(f"An error occurred: {e}")

def handler(event, context):
    bucket_list = ['cdk-hnb659fds-assets-457733617380-us-east-1']
    for bucket in bucket_list:
        empty_bucket(bucket)

import boto3
import click

aws = boto3.Session(profile_name='default')
s3 = aws.resource('s3')

@click.group()

def cli():
    "this is a CLICK group for calling function"
    pass


@cli.command('list-buckets')

def list_buckets():
    "List all the buckets in the S3"
    for bucket in s3.buckets.all():
        print(bucket)
        for file in bucket.objects.all():
            print('  files  in this bucket : ' + str(file))


@cli.command('list-bucket-objects')
@click.argument('bucket')

def list_bucket_objects(bucket):
    "List all the objects in the bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)
        key = obj.key
        body = obj.get()['Body'].read()
        print(body)

if __name__ == '__main__':
    cli()

import configparser
import boto3
import botocore
import re
import string

config = configparser.RawConfigParser()
config.read('ConfigFile.properties')
bucketname = config.get('s3Credentials', 's3.bucketname')
secretkey = config.get('s3Credentials', 's3.secretaccesskey');
accessid = config.get('s3Credentials', 's3.accesskeyid');
filename = config.get('s3Credentials', 's3.filename');

def downloadFile():
    s3 = boto3.resource('s3', aws_access_key_id=accessid, aws_secret_access_key=secretkey)

    try:
        s3.Bucket(bucketname).download_file(filename, 'F:\\sandy.txt')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

def findTopFive():
    frequency = {}
    document_text = open('F:\\sandy.txt', 'r')
    text_string = document_text.read().lower()
    match_pattern = re.findall(r'\b[a-z\']{1,15}\b', text_string)

    for word in match_pattern:
        if word in frequency:
            freq = frequency[word]
            frequency[word] = freq + 1
        else:
            frequency[word] = 1

    keys = list(frequency.keys())
    values = list(frequency.values())

    for i in range(len(values)):
        for j in range(len(values)):
            if (values[i] > values[j]):
                values[i], values[j] = values[j], values[i]
                keys[i], keys[j] = keys[j], keys[i]

    for i in range(5):
        print(keys[i], " ", values[i])

downloadFile()
findTopFive()
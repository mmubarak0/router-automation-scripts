#!/usr/bin/env python3
"""
Example code on how to remove a SMS, you can try it by running:
python3 remove_sms.py http://admin:PASSWORD@192.168.8.1/ --query 'your query'
"""
from argparse import ArgumentParser
from huawei_lte_api.Connection import Connection
from huawei_lte_api.Client import Client


parser = ArgumentParser()
parser.add_argument('url', type=str)
parser.add_argument('--query', type=str, required=True)
parser.add_argument('--username', type=str)
parser.add_argument('--password', type=str)
args = parser.parse_args()

with Connection(
    args.url, username=args.username, password=args.password
) as connection:
    client = Client(connection)
    sms_list = client.sms.get_sms_list()['Messages']['Message']
    sms_list_filtered = []
    if args.query:
        sms_list_filtered = [
            sms for sms in sms_list if args.query in sms['Content']
        ]
    if not sms_list_filtered:
        print("No messages found matching the query.")
        exit(1)
    else:
        print(f"Found {len(sms_list_filtered)} messages matching the query.")

    confirmation = input(
        "Press Enter to delete the messages or Ctrl+C to cancel..."
    )
    if confirmation != '':
        print("Operation cancelled.")
        exit(1)
    print("Deleting messages...")
    for sms in sms_list_filtered:
        index = sms['Index']
        phone = sms['Phone']
        content = sms['Content']
        message = f"ID: {index}, From: {phone}, Text: {content[:10]}..."
        client.sms.delete_sms(index)
        print(f"Deleted message: {message}")

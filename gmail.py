import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError 

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
flow = InstalledAppFlow.from_client_secrets_file('creds.json', SCOPES)
creds = flow.run_local_server(port=0)
service = build('gmail', 'v1', credentials=creds)
message = MIMEText("Hello! Test.")
message['to'] = 'btrent@email.com'
message['subject'] = 'New Part Number'
create_message =  {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

try:
    message = (service.users().messages().send(userId="me", body=create_message).execute())
    print(F'sent message!')
except HTTPError as error:
    print(F'An error occured {error}')
    message = None

# #part_number = last_non_empty_row['New Part Number']
# new_item_description = last_non_empty_row['Item Description']

# email_body = f"""
# New PN: {part_number}
# Desc: {new_item_description}

# Request: {request}

# Vnd Name: {vnd_name}
# Vnd ID: {vnd_id}
# SKU: {sku} 
# Detail: {detail} 
# TPP: ${tpp.value} 
# Site: {site}

# Thanks,
# .py"""

# SCOPES = [ "https://www.googleapis.com/auth/gmail.send"]
# flow = InstalledAppFlow.from_client_secrets_file(r'C:/Users/btrent//creds.json', SCOPES)
# creds = flow.run_local_server(port=0)
# service = build('gmail', 'v1', credentials=creds)

# message = MIMEText(email_body)
# message['to'] = 'btrent@email.com'
# message['subject'] = '@email.noreply'

# create_message =  {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

# try:
#     result = (service.users().messages().send(userId="me", body=create_message).execute())
#     print(f'sent message!')
# except HTTPError as error:
#     print(f'An error occured {error}')
#     result = None    
    
# #Print Vendor Name & Item Description
# print(f"New PN: {part_number}")
# print(f"Item Description: " + str(new_item_description.upper()))
# print(f"TPP Price: {tpp.value}")
# print(f"List Price: {list_Price}")
# print(f"Site: " + str(site.upper()))

import json
import pandas as pd
import requests

PI_open = open('API_key.txt')
API_read = API_open.read()
# Your API key goes here.
API_KEY = API_read

raw_df = pd.read_csv('indeed_edin.csv', encoding='utf-8',
                     error_bad_lines=False)
#turnstilelink_link_1/_text

df = raw_df[['location_value', 'turnstilelink_link_1/_text', 
'summary_description']]
df.columns = ['location', 'title', 'description']

content_df = list(df.title + ' ' + df.description)

categories = []
step = 150
for start in xrange(0, len(content_df), step):
    end = start + step

    response = requests.post(
        
"https://api.monkeylearn.com/v2/classifiers/cl_4PFzSWVR/classify/",
        data=json.dumps({'text_list': content_df[start:end]}),
    	headers={'Authorization': 'Token {}'.format(API_KEY),
            'Content-Type': 'application/json'}).json()

    # We go through the results of the API call, storing the result on a list.
    for category in response['result']:
        categories.append(category[0]['label'])
        
augmented_df = df.join(pd.DataFrame(categories, columns=['category']))
augmented_df.to_csv('indeed_aug.csv', encoding='utf-8', index=False, 
header=False)        
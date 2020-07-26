import requests
import pandas as pd
from pandas.io.json import json_normalize

credentials = 'amellia@indonesiaindicator.com', 'rahasia123'
session = requests.Session()
session.auth = credentials
zendesk = 'https://indonesiaindicator.zendesk.com'

topic_id = 123456
url = zendesk + '/api/v2/tickets.json'
response = session.get(url)
if response.status_code != 200:
    print('Error with status code {}'.format(response.status_code))
    exit()
data = response.json()
df = pd.DataFrame.from_dict(json_normalize(data, 'tickets', ['next_page', 'previous_page', 'count'], 
                    record_prefix='tickets.'))
print(df)

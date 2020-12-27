import pandas as pd
from sodapy import Socrata
from datetime import datetime, timedelta
from creds import api_key
from func import send_email

seven_days_ago = "'" + str((datetime.today() - timedelta(days=7)).isoformat()) + "'"
output_path = file_path
today = datetime.today().strftime('%m%d%Y')
# Enter the information from those sections here
socrata_domain = "data.colorado.gov"
socrata_dataset_identifier = '4ykn-tg5h'
client = Socrata(socrata_domain, api_key)
results = client.get(socrata_dataset_identifier, limit=10000, where="entityformdate >= " + seven_days_ago)
results_df = pd.DataFrame.from_records(results)
results_df.to_excel(output_path + 'co_bu_data' + today + '.xlsx', index=False)

text = """<p style='margin:0in;font-size:15px;font-family:"Calibri",sans-serif;'>Hey Brian,</p>
<p style='margin:0in;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:15px;font-family:"Calibri",sans-serif;'>This is an automated email.</p>
<p style='margin:0in;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:15px;font-family:"Calibri",sans-serif;'>Attached is an excel file with the Colorado Business Entities who registered with the Colorado Department of State (CDOS) in the last seven days.</p>
<p style='margin:0in;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin:0in;font-size:15px;font-family:"Calibri",sans-serif;'>Thanks,</p>
<p style='margin:0in;font-size:15px;font-family:"Calibri",sans-serif;'>Jacob</p>"""

send_email(outgoing_email,
           'Automated Email: Colorado Business Entities ' + today,
           text,
           incoming_email,
           attachment_location=output_path + 'co_bu_data' + today + '.xlsx')

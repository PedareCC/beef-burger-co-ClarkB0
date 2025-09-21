from datetime import datetime
from pytz import timezone

date_format = '%Y-%m-%d %H:%M:%S'

datetime_utc = datetime.now()

datetime_local = datetime_utc.astimezone(timezone('Australia/Adelaide'))

print(datetime_utc.strftime(date_format))
print(datetime_local.strftime(date_format))
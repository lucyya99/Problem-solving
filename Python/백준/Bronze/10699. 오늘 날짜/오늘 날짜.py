# 백준허브
from datetime import datetime, timezone, timedelta
print(datetime.now(tz=timezone(timedelta(hours=9))).strftime('%Y-%m-%d'))
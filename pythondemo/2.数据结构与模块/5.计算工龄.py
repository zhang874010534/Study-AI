from datetime import datetime
from math import ceil
company_in = datetime(2020, 1, 1)
now = datetime.now()
print(now)
print(now - company_in)
year = (now - company_in).days / 365
print(year)
print(int(year))
print(ceil(year))
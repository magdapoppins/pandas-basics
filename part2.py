import json
import pandas as pd

records = [
    ('Math', 'Chemistry', 'Physics'),
    ('Crafts','Art', 'Electronics')]

pd.DataFrame.from_records(records)


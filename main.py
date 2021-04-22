import pandas as pd
from korea import korea
from china import china

korea_xlsx = "korea.xlsx"
china_xlsx = "china.xlsx"
indonesia_xlsx = "indonesia.xlsx"

korea(korea_xlsx).to_excel("korea_filter.xlsx", index=False)
china(china_xlsx).to_excel("china_filter.xlsx", index=False)

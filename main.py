import pandas as pd
from korea import korea
from china import china
from indonesia import indonesia

korea_xlsx = "korea.xlsx"
china_xlsx = "china.xlsx"
indonesia_xlsx = "indonesia.xlsx"

# korea(korea_xlsx).to_excel("korea_filter.xlsx", index=False)
# china(china_xlsx).to_excel("china_filter.xlsx", index=False)
# indonesia(indonesia_xlsx).to_excel("indonesia_filter.xlsx", index=False)

korea_status = korea(korea_xlsx)
china_status = china(china_xlsx)
indonesia_status = indonesia(indonesia_xlsx)

order_status = korea_status.append([china_status, indonesia_status])

# order_status.to_excel("order_status.xlsx", index=False)

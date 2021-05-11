import pandas as pd
from korea import korea
from china import china
from indonesia import indonesia

korea_xlsx = "korea.XLSX"
china_xlsx = "china.XLSX"
indonesia_xlsx = "indonesia.XLSX"

# korea(korea_xlsx).to_excel("korea_filter.xlsx", index=False)
# china(china_xlsx).to_excel("china_filter.xlsx", index=False)
# indonesia(indonesia_xlsx).to_excel("indonesia_filter.xlsx", index=False)

korea_status = korea(korea_xlsx)
china_status = china(china_xlsx)
indonesia_status = indonesia(indonesia_xlsx)

order_status = korea_status.append([china_status, indonesia_status])

order_status["Customer"] = (
    order_status["Customer"]
    .replace(["Agrohim", "AGROHIM&KEMOIMPEX DOO BEOGRAD"], "AGROHIM")
    .replace(["PRIMEX LTD", "PRIMEX LTD."], "PRIMEX")
)

order_status["Line"] = (
    order_status["Line"]
    .replace(["TBR/L", "TBR/M", "TBR/S", "USS"], "TBR")
    .replace(["UHP", "HP", "LS", "LV", "SP"], "PCLT")
)

order_status.to_excel("order_status.xlsx", index=False)

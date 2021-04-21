import pandas as pd


korea = "korea.xlsx"

df = pd.read_excel(korea, engine="openpyxl")

filtered = df[
    [
        "Sold-to-party name",
        "Customer PO no.",
        "Sales order no",
        "Material",
        "Size",
        "Pattern",
        "Brand",
        "F.Dest text",
        "R.EPC date",
        "CY date",
        "On-board date",
        "ETA date",
        "SO qty",
        "Confirm qty",
        "CTR measure",
    ]
]

filtered["Origin"] = "Korea"

filtered.to_excel("korea_pivot.xlsx")

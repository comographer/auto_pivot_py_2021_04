import pandas as pd


korea = "korea.xlsx"

df = pd.read_excel(korea, engine="openpyxl")

pivoted = df.pivot(
    columns=[
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
    ],
    values=["SO qty", "Confirm qty", "CTR measure"],
)

pivoted.to_excel("korea_pivot.xlsx")

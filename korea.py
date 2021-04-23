import pandas as pd


def korea(korea):
    df = pd.read_excel(korea, engine="openpyxl")
    korea_filter = df[
        [
            "Sold-to-party name",
            "Customer PO no.",
            "Sales order no",
            "Material",
            "Size",
            "Pattern",
            "Brand",
            "Prod.hier text",
            "F.Dest text",
            "R.EPC date",
            "CY date",
            "On-board date",
            "ETA date",
            "SO qty",
            "Confirm qty",
            "Net amount",
            "CTR measure",
        ]
    ]

    korea_filter.columns = [
        "Customer",
        "PO",
        "SO",
        "Material",
        "Size",
        "Pattern",
        "Brand",
        "Line",
        "Destination",
        "R.EPC",
        "CY",
        "ETD",
        "ETA",
        "Order QTY",
        "Confirm QTY",
        "Net Value",
        "CTR Measure",
    ]

    korea_filter["Origin"] = "Korea"
    return korea_filter

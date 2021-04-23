import pandas as pd


def china(china):
    df = pd.read_excel(china, engine="openpyxl")
    china_filter = df[
        [
            "Sold Name",
            "Cust. PO No.",
            "Sales Document",
            "Material",
            "Size",
            "Pattern",
            "Brand",
            "Line",
            "Unloading Point",
            "ReEPC Date",
            "CY Date",
            "ETD Date",
            "ETA Date",
            "Order Qty.",
            "Confirmed Qty.",
            "Net value",
        ]
    ]

    china_filter.columns = [
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
    ]

    china_filter["CTR Measure"] = ""
    china_filter["Origin"] = "China"
    return china_filter

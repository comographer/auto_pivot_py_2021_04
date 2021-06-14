import pandas as pd


def indonesia(indonesia):
    df = pd.read_excel(indonesia, engine="openpyxl")
    df.rename(columns={df.columns[48]: "Pattern"}, inplace=True)

    indonesia_filter = df[
        [
            "Ship-to party name",
            "Customer PO no.",
            "Sales Doc.",
            "Material",
            "Size",
            "Pattern",
            "Brand",
            "Prod. hier. text",
            "F.Dest Text",
            "Bill of lading no.",
            "Container ID",
            "Final F/W Name",
            "R.EPC date",
            "CY date",
            "On-board date",
            "ETA date",
            "S/O QTY",
            "Confirm QTY",
            "Net amount",
            "CTR. Measure",
        ]
    ]

    indonesia_filter.columns = [
        "Customer",
        "PO",
        "SO",
        "Material",
        "Size",
        "Pattern",
        "Brand",
        "Line",
        "Destination",
        "B/L",
        "Liner",
        "CTN ID",
        "R.EPC",
        "CY",
        "ETD",
        "ETA",
        "Order QTY",
        "Confirm QTY",
        "Net Value",
        "CTR Measure",
    ]

    indonesia_filter["Origin"] = "Indonesia"
    return indonesia_filter

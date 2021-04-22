import pandas as pd


def indonesia(indonesia):
    df = pd.read_excel(indonesia, engine="openpyxl")
    df.rename(columns={df.columns[48]: "Pattern"}, inplace=True)

    indonesia_filter = df[
        [
            "Sold-to party name",
            "Customer PO no.",
            "Sales Doc.",
            "Material",
            "Size",
            "Pattern",
            "Brand",
            "F.Dest Text",
            "R.EPC date",
            "CY date",
            "On-board date",
            "ETA date",
            "S/O QTY",
            "Confirm QTY",
            "CTR. Measure",
        ]
    ]

    indonesia_filter["Origin"] = "Indonesia"
    return indonesia_filter

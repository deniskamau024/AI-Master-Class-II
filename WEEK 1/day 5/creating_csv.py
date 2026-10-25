import pandas as pd

data = {
    "Name": ["Walter","Jane","Peter","Kaka","Cynthia"],
    "County": ["Nairobi","Kirinyaga","Kiambu","Kakamega","Murang'a"],
    "Amount": [75000,45000,97000,102500,88000]
}

df = pd.DataFrame(data)
df.to_csv("sales.csv",index=False)
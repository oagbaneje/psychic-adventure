import pandas as pd

risk_rating = pd.read_excel('risk_rating.xlsx', index_col=6)

print(risk_rating)    
import json
import pandas as pd
import numpy as np


def calculate_score(credit_application):
    #Sum obligor on rows
    obligor_risk_rating = credit_application.iloc[:,0:11].sum(axis=1)
    # sum facility_features on rows
    facility_features = credit_application.iloc[:, 11:20].sum(axis=1)
    score = (obligor_risk_rating*facility_features)[0]
    return score


def accept_reject(credit_application):
    """Accept or reject credit application based on some criteria"""
    # gate criteria
    if ((credit_application["ds_ratio"] <= 200) | \
        (credit_application["business_age"] <= 4)  |\
            (credit_application["length_rel"] <= 6)  |\
                (credit_application["positive_rel"]) |\
                    (credit_application["complete_app"])).any:
                    score = calculate_score(credit_application)
                    if score < 222:
                        return json.dumps({"verdict": "Accepted", "interest": 15})
                    elif score >= 222:
                        return json.dumps({"verdict":"Accept with Caution", "interest": 15})
                    else:
                        return json.dumps({"verdict": "Reject", "interest": None})
    else:
        # check the score against threshold
        print("Reject")

#batch processing option
# import json files
#data = json.load(open("data.json"))

# def main():
#      try:
#          df = pd.read_json("csvjson.json")
#          accept_reject(df)
#      except:
#          "Perhaps you did not import a json file"

# if __name__ == "__main__":
#     main()

df = pd.read_csv("my_csv.csv")
#accept_reject(df)
#print(df.iloc[[0]])
#df = pd.read_json("csvjson.json")
print(accept_reject(df.iloc[[0]]))

# Batch processing
"""def batch_processing(csv_file, number_of_chunks=1):
    all_batches = []
    chunk_iter  = pd.read_csv(csv_file,  chunksize=number_of_chunks)
    for chunk in chunk_iter:
        all_batches.append(accept_reject(chunk))
    df_all_batches = pd.concat(all_batches)
    return df_all_batches

batch_processing("my_csv.csv", 1)"""
        
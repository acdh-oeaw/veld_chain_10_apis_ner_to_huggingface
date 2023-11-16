import json


with open("/veld/veld_data_5_apis_ner_gold/json/cleaned/apis_ner__simplified_entities.json", "r") as f_in:
    data = json.load(f_in)

data_new = []
for d in data:
    if d["entities"] != []:
        data_new.append(d)
data = data_new

with open("/veld/APIS_OEBL_NER/data.json", "w") as f_out:
    json.dump(data, f_out, ensure_ascii=False, indent=4)


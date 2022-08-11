from m3inference import M3Inference
import pprint
import pandas as pd

m3 = M3Inference() # see docstring for details
pred = m3.infer('/content/drive/MyDrive/covid_avatar/data_resized.jsonl') # also see docstring for details
pred = list(pred.items())

csv_file = "/content/drive/MyDrive/covid_avatar/user_label_0_lang.csv"
result_file = "/content/drive/MyDrive/covid_avatar/user_demographic.csv"
df = pd.read_csv(csv_file)

df['gender'] = 'female'
df['age'] = '<=18'
df['is_org'] = False


for i in range(len(pred)):
  user_id, result_dict = pred[i]
  user_id = int(user_id)

  gender_dict = result_dict['gender']
  age_dict = result_dict['age']
  org_dict = result_dict['org']
  gender = max(gender_dict, key=gender_dict.get)
  age = max(age_dict, key=age_dict.get)
  org = max(org_dict, key=org_dict.get)

  if org == 'org':
    is_org = True
  else:
    is_org = False

  if user_id not in df['id'].values:
    print(user_id)
  else:
    df.loc[df['id'] == user_id, 'gender'] = gender
    df.loc[df['id'] == user_id, 'age'] = age
    df.loc[df['id'] == user_id, 'is_org'] = is_org

df.to_csv(result_file, index=False)




  

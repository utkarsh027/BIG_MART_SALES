import pickle
import json
import numpy as np

_data_columns = None
_model = None


def predict_sales_price(i_weight,i_vis,i_mrp,o_ide,o_age,i_cat,i_fat,i_type,o_size,o_city,o_type):
  
  input = np.zeros(len(_data_columns))
  
  index_i_cat = _data_columns.index(i_cat.lower())
  index_i_fat = _data_columns.index(i_fat.lower())
  index_i_type = _data_columns.index(i_type.lower())
  index_o_size = _data_columns.index(o_size.lower())
  index_o_city = _data_columns.index(o_city.lower())
  index_o_type = _data_columns.index(o_type.lower())

  
  input[0] = i_weight
  input[1] = i_vis
  input[2] = i_mrp
  input[3] = o_ide
  input[4] = o_age 
 

  input[index_i_cat] = 1
  input[index_i_fat] = 1
  input[index_i_type] = 1
  input[index_o_size] = 1
  input[index_o_city] = 1
  input[index_o_type] = 1

  return _model.predict([input])[0][0]

def load_artifacts():
    global _data_columns
    global _model
    
    print('Loading Artifacts...')

    with open('./columns.json','r') as f:
        _data_columns = json.load(f)['data-columns']

    with open('./big_mart.pickle','rb') as f:
        _model = pickle.load(f)

    print('Artifacts...Loaded')


def column_names():
    return _data_columns
    

load_artifacts()
print(predict_sales_price(13.22,0.099747,75.2328,27.0,36,'FD','LF','Snack Foods','High','Tier 3','Supermarket Type3'))
print(column_names())

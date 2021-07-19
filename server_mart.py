from flask import Flask,request,jsonify
import util

app = Flask(__name__)

@app.route('/get_column_names')
def get_column_names():
    response = {'Columns': util.column_names()}
    return response

@app.route('/predict_sales_price',methods=['POST'])
def predict_sales_price():
    i_weight = float(request.form['item_weight'])
    i_vis = float(request.form['item_visibility'])
    i_mrp = float(request.form['item_MRP'])
    o_ide = float(request.form['outlet_identifier'])
    o_age = float(request.form['years'])
    i_cat = request.form['cat'] 
    i_fat = request.form['item_fat_content']
    i_type = request.form['item_type']
    o_size = request.form['outlet_size']
    o_city=request.form['outlet_city']
    o_type=request.form['outlet_type']
    
    
    
    response =jsonify({'estimated_sales': util.predict_sales_price(i_weight,i_vis,i_mrp,o_ide,o_age,i_cat,i_fat,i_type,o_size,o_city,o_type)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run()

import pickle
loaded_class = pickle. load(open('randomclass_chronic', 'rb'))
loaded_reg = pickle. load(open('randomreg_chronic', 'rb'))

import numpy as np
import pandas as pd
from flask import Flask, request, redirect, render_template
app = Flask(__name__)
@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route("/val",methods=['POST'])

def val():
    test=[]
    if request.method == 'POST':
        test.append(request.form.get("age"))
        test.append(request.form.get("bp"))
        test.append(request.form.get("sg"))
        test.append(request.form.get("al"))
        test.append(request.form.get("su"))
        rb=request.form.get("rbc")
        if rb=='abnormal':
            test.append(1)
        else:
            test.append(0)
        pc=request.form.get("pc")
        if pc=='abnormal':
            test.append(1)
        else:
            test.append(0)
        pcc=request.form.get("pcc")
        if pcc=='present':
            test.append(1)
        else:
            test.append(0)
        ba=request.form.get("ba")
        if ba=='present':
            test.append(1)
        else:
            test.append(0)
        test.append(request.form.get("bgr"))
        test.append(request.form.get("bu"))
        test.append(request.form.get("sc"))
        test.append(request.form.get("sod"))
        test.append(request.form.get("pot"))
        test.append(request.form.get("hemo"))
        test.append(request.form.get("pcv"))
        test.append(request.form.get("wc"))
        test.append(request.form.get("rc"))
        ht=request.form.get("htn")
        if ht=='yes':
            test.append(1)
        else:
            test.append(0)
        d=request.form.get("dm")
        if d=='yes':
            test.append(1)
        else:
            test.append(0)
        ca=request.form.get("cad")
        if ca=='yes':
            test.append(1)
        else:
            test.append(0)
        ap=request.form.get("appet")
        if ap=='good':
            test.append(1)
        elif ap=='poor':
            test.append(0)
        else:
            test.append(np.nan)
        p=request.form.get("pe")
        if p=='yes':
            test.append(1)
        else:
            test.append(0)
        an=request.form.get("ane")
        if an=='yes':
            test.append(1)
        else:
            test.append(0)
    print(test)
    test_df=pd.DataFrame(test)
    test_df=np.array(test_df).reshape(1, -1)
    
    ans1=loaded_class.predict(test_df)
    ans2=loaded_reg.predict(test_df)
    if int(ans1)==1:
        answer1="Sorry to say!! You have CHRONIC DISEASE!!!"
        return render_template('rename.html',answer1=answer1,answer2=ans2)
    else:
        answer1="Happy to say that you don't have CHRONIC DISEASE"

        return render_template('rename2.html',answer1=answer1,answer2=ans2)
    
if __name__ == "__main__":
    app.debug=True
    app.run(debug=False)

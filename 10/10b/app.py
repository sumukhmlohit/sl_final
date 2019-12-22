from flask import Flask,render_template,url_for,request
import time
import re

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def student():
    if request.method=='GET':
        return render_template('student.html')

    if request.method=="POST":
        usn_pattern="^[0-9][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"
        if request.form["usn"]==""or request.form["dob"]==""or request.form["math"]==""or request.form["phy"]==""or request.form["chem"]=="":
            msg="No empty fields"
            return render_template('student.html',msg=msg,average="")
        
        try:
            time.strptime(request.form["dob"],"%d/%m/%Y")
        except ValueError:
            msg="Invalid DOB Format"
            return render_template('student.html',msg=msg,average="")
        if not re.match(usn_pattern,request.form["usn"]):
            msg= "Invalid USN Format"
            return render_template('student.html',msg=msg,average="")
        else:
            average=(int(request.form["math"])+int(request.form["phy"])+int(request.form["chem"]))/3
            return render_template('student.html',msg="",average=average)    
if __name__=='__main__':
    app.run(debug=True)

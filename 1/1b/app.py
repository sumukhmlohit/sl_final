from flask import Flask,render_template,request,url_for,session

app=Flask(__name__)

app.secret_key="secret"

@app.route('/',methods=['GET','POST'])
def index():
    try:
        balance=session["balance"]
        count=session["count"]

    except KeyError:
        count=session["count"]=0
        balance=session["balance"]=0
    
    if request.method=='GET':
        msg=""
        return render_template('atm.html',balance=balance,msg=msg)

    if request.method=='POST':
        if session["count"]>=5:
            msg="Max 5 transactions"
            return render_template('atm.html',balance=session["balance"],msg=msg)
        if int(request.form["amount"])<0:
            msg="Don't enter negative amount"
            return render_template('atm.html',balance=balance,msg=msg) 

        if session["count"]>5:
            msg="More than 5 transactions not allowed"
            return render_template('atm.html',balance=balance,msg=msg)

        if request.form["action"]=="deposit":
            count=session["count"]+1
            session["count"]=count
                
            balance=balance+int(request.form["amount"])
            session["balance"]=balance
            msg="Money deposited"
            return render_template("atm.html",balance=balance,msg=msg)

        if request.form["action"]=="withdraw":
            count=session["count"]+1
            session["count"]=count

            if int(request.form["amount"])>5000:
                return render_template('atm.html',balance=balance,msg="Can't withdraw more than 5000") 
            
            if int(request.form["amount"])>session["balance"]:
                msg="Can't withdraw more than balance"
                return render_template('atm.html',balance=balance,msg=msg)    
            else:
                balance=balance-int(request.form["amount"])
                session["balance"]=balance
                msg="Money withdrawn"
                return render_template('atm.html',balance=balance,msg=msg)

        else:
            msg=""
            return render_template('atm.html',msg=msg,balance=balance)

if __name__=='__main__':
    app.run(debug=True)

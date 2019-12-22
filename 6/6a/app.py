from flask import Flask,url_for,render_template,request,session

app=Flask(__name__)
app.secret_key="secret"
@app.route('/',methods=['GET','POST'])
def item():

    try:
        amount=session["amount"]
    except KeyError:
        session["amount"]=0
        amount=0
    
    if request.method=='GET':
        return render_template('item.html',amount=amount,msg="")

    if request.method=='POST':

        if int(request.form["item1"])<0 or int(request.form["item2"])<0 or int(request.form["item3"])<0:
            return render_template('item.html',amount=session["amount"],msg="Don't enter -ve numbers")
        
        else:
            amount=session["amount"]
            amount=amount+int(request.form["item1"])*1000+int(request.form["item2"])*2000+int(request.form["item3"])*1500
            session["amount"]=amount
            return render_template('item.html',amount=session["amount"],msg="Price calculated")
    
if __name__=='__main__':
    app.run(debug=True)

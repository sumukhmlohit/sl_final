from flask import Flask,redirect,url_for,request,render_template,session

app=Flask(__name__)

app.secret_key="secret"

@app.route('/',methods=['GET','POST'])
def store():
    if request.method=="GET":
        return render_template('store.html')

    if request.method=="POST":
        for item in ["apple","orange","papaya"]:
            if item not in session:
                session[item]=int(request.form[item])
            else:
                session[item]+=int(request.form[item])

        return redirect(url_for('cart'))

@app.route('/cart',methods=['GET','POST'])
def cart():
    cart=[]
    for item in ["apple","orange","papaya"]:
        cart.append({"name":item,"quantity":session[item]})
    return render_template('cart.html',cart=cart)

@app.route('/bill',methods=['GET','POST'])
def bill():
    amount=0
    i=0
    prices=[100,80,60]
    cart=[]
    for item in ["apple","orange","papaya"]:
        row={}
        row["name"]=item
        row["quantity"]=session[item]
        row["price"]=prices[i]*session[item]
        amount+=prices[i]*session[item]
        i=i+1
        cart.append(row)
    return render_template('bill.html',cart=cart,amount=amount)
    
if __name__=='__main__':
    app.run(debug=True)

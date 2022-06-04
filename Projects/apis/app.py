'''import requests
url="http://api.open-notify.org/astros.json"
data=requests.get(url)
#print(data)
#print(type(data))
#print(dir(requests))
d=data.text
print(d)
print(type(d))
print(len(d))
#using python bulit in function-->eval()

e=eval(d)
print(e)
print(type(e))
print(e.keys())


#or
f=data.json()
print(f)
print(type(f))
#print(f['people'][-2:])
print(f['people'][-1]['name'])
print(f['people'][-2]['name'])'''

from flask import Flask,render_template,jsonify,request
app=Flask(__name__)
@app.route('/keerthana')
def sample():
    return "burger pizza chicken manchuria panipuri "
#def check():
    #return render_template("index.html")
myquotes=[{'id':1,'name':'Steve.jobs','quote':'leadership'}]
@app.route('/quotes',methods=['GET'])
def quotes():
    return jsonify(myquotes)
@app.route('/addqoute',methods=['POST'])
def addquote():
    quote=request.get_json()
    inc=myquotes[-1]['id']+1
    quote['id']=inc
    myquotes.append(quote)
    return jsonify(myquotes)
    return jsonify(myquotes)
@app.route('/addquote',methods=['POST']) #endpoint where we are creating new ids
def addquote():
    quote = request.get_json()
    inc = myquotes[-1]['id']+1
    quote['id'] = inc
    myquotes.append(quote)
    return jsonify(myquotes)
@app.route('/update/<int:id>',methods=['PUT']) #we are updating
def updatequote(id):
    quote = request.get_json()
    for i in myquotes:
        print(i['id'])
        if i['id']==id:
            print("I'm here")
            i['name'] = quote['name']
            #i['quote'] = quote['quote']
            print(i)
    return jsonify(quote)
@app.route('/delete/<int:id>',methods=['DELETE'])
def deletequote(id):
    for i in myquotes:
        if i['id'] == id:
            myquotes.remove(i)
    return jsonify(myquotes)      


app.run()



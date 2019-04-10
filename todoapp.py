from flask import Flask, render_template, request

mylist = []

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/list')
def list():
    return render_template('list.html', mylist=mylist)

@app.route('/newtask')
def newtask():
    return render_template('additem.html')

@app.route('/additem', methods=['POST', 'GET'])
def additem():

    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    mylist.append([task, email, priority])
    return render_template('list.html', mylist=mylist)

@app.route('/clear/')
def clear():
    del mylist[:]
    return render_template('list.html', mylist=mylist)

if __name__ == '__main__':
    app.run(debug=True)

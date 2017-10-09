from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def indexx():
	return render_template('index.html') 

@app.route('/process', methods=['POST'])
def myName():
   name = request.form['name']
   print "My name is:", name # display in terminal
   return redirect('/') # Always redirect after handling POST data to avoid data being handled more than once!

app.run(debug=True)
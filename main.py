from flask import Flask

app = Flask(__name__)


#@app.route('/')
#@app.route('/index')
#def index():
    #users = [ 'regina', 'helena', 'saeideh']
    #return render_template('index.html', title='FLASK', username=name)


    #return render_template('index.html', title='FLASK', members=users)

@app.route ('/product/<name>')
def get_product(name):
    return "the product is "+ str(name)

if __name__=="__main__":
    app.run(debug=True)




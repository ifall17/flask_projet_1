from flask import Flask, render_template
app = Flask(__name__)




@app.route('/')
def acceuil():
    return render_template('index.html')

@app.route('/personnel')
def personnel():
    return render_template('/personnelle/index.html')

@app.route('/banque')
def banque():
    return render_template('/banque/index.html')

@app.route('/fonction')
def fonction():
    return render_template('/fonction/index.html')

@app.route('/ville')
def ville():
    return render_template('/ville/index.html')



@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

if __name__== '__main__':
    app.run(debug=True)
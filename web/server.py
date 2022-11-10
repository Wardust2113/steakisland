from flask import *

# creating the Flask class object
app = Flask( __name__ )

@app.route( '/' )
def home():
	return redirect( url_for( 'index' ))

@app.route( '/index' )
def index():
	return render_template( 'index.html' )

if __name__ == '__main__':
	app.run( debug = True )

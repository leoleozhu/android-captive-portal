#!/user/bin/env python

from flask import Flask
app=Flask(__name__)

@app.route('/generate_204')
def generate_204():
	return '', 204

if __name__ == '__main__':
	app.run()


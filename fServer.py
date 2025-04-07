from flask import Flask, render_template

import os
import sys


app = Flask(__name__)

#port=int(sys.argv[1])

#os.environ['FLASK_PORT'] = str(port)


@app.route('/')
def index():
    #return render_template('/index.html')
    return ("this is running on port: "+str(port))


if __name__ == '__main__':
	port=int(sys.argv[1])
	app.run(host="0.0.0.0", port=port)
	#app.run(host="0.0.0.0", port=9001)

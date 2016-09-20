from flask import Flask, render_template ,request, Response
from flask_pymongo import PyMongo
from flask_restful import reqparse
from time import sleep
app = Flask(__name__)
mongo = PyMongo(app)


class controlled_MJPEG_Generator:
  def start():
    pass
  def pause():
    pass
  def generate():
    yield (b'--frame\r\n Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/colorstream")
def colorStream():
  try:
    def generate():
      framenumber=1
      while True:
        frame=open(str(framenumber)+".jpg",'rb').read()
        framenumber=(framenumber%2)+1
        print "Streaming file Read"
        yield (b'--frame\r\n Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')
  except:
        return "404", 404
		
		
@app.route("/colorimage.jpg")
def colorimage():
  try:
    frame=open("new.jpg",'rb').read()
    return Response( frame, mimetype='image/jpg;')
  except:
        return "404", 404




loginReq=reqparse.RequestParser()
loginReq.add_argument('username')
loginReq.add_argument('password')



#Views


@app.route('/')
def index(name=None):
  args = loginReq.parse_args()
  
  collection_stuff = mongo.db.cameras.find({})
  return render_template('index.html', data=args)

@app.route("/settings")
@app.route("/potato<int:a>")
def hello(a=None):
  if not a :
    a=0
  mongo.db.testing.insert({"potato":a})
	
  return "inserting thy potato"

	
		
	
if __name__ == "__main__":
  "\x9cb\xde\x0c<M\x86\xe7\x9bFdR2\x95,\x8c\x19\xdb\xe8\xd1'\x9ey\x1e"
  app.run(port=80,debug=True)


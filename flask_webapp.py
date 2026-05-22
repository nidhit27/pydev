from flask import Flask, request

app = Flask(__name__)

def mylist():
        st=" "
        for tums in (range(1,6)):
            print (tums)
            st+=str(tums)+ "<br>"
        return "<h1>" + str(st) + "</h1>"           

@app.route('/', methods = ['POST','GET'])
def home():
   ## str = "Hello World"
    a=mylist()
    user = request.args.get('uname')
    print("name: ",user)
    return a

@app.route('/bbb')
def mul():
   ## str = "Hello World"
    st = ""

    for tums in range(1, 6):      
        for nums in range(1, 11):  
            st += str(tums) + " x " + str(nums) + " = " + str(tums * nums) + "<br>"

    return st

@app.route('/ccc')
def mul():
    str = "Hello World Dhana"
    return str


@app.route('/aaa')
def hello_world():
    return "<h1>Hello World Lasya</h1>"
if __name__ == '__main__':
    app.run()
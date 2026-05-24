from flask import Flask, request

app = Flask(__name__)

def mylist():
        st=" "
        for tums in (range(1,11)):
            print (tums)
            st+=str(tums)+ "<br>"
        return "<h1>" + str(st) + "</h1>"           

@app.route('/', methods=['POST','GET'])
def home():
    a = mylist()
    if request.method == 'POST':
        user = request.form.get('uname')
    else:
        user = request.args.get('uname')
    print("name:", user)
    return a

@app.route('/bbb')
def multiplication_table():
    st = ""

    for tums in range(1, 6):      
        for nums in range(1, 11):  
            st += str(tums) + " x " + str(nums) + " = " + str(tums * nums) + "<br>"

    return st

@app.route('/ccc')
def hello_dhana():
    message = "Hello World Dhana"
    return message


@app.route('/aaa')
def hello_world():
    return "<h1>Hello World Lasya</h1>"
if __name__ == '__main__':
    app.run()
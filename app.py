
from flask import Flask,request,render_template

app=Flask(__name__)




@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/chat',methods=['post'])
def startChat():    

    # Get form information
    name=request.form.get('inputName')
    title=request.form.get('inputTitle')
    message=request.form.get('messageInput')
    
    return render_template('submit message.html',name=name,title=title,message=message)





if __name__ == "__main__":
    app.run(debug=True)
 
   






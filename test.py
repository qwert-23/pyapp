from flask import Flask,render_template,request,redirect
import pymysql  

conn = pymysql.connect( host='localhost', port=3306, db='pyapp',user='root', passwd='java1004'       
)
print(conn) 
app = Flask(__name__)
# 1.  msg 목록보기

@app.route('/',methods=['GET'])
def msg_list():
    cursor = conn.cursor()
    cursor.execute('SSELECT msg_id,msg_text FROM msg')
    msglist=cursor.fetchall()
    print(msglist)
    return render_template('msg_list.html',msglist = msg_list)


#2. msg_html 

@app.route('/add_msg',methods=['GET','POST'])
def add_msg():
   if render_template == 'GET':
     return render_template('add_msg.html') 
    elif request.method == 'POST': msg_text = request.form['msg_text']
        

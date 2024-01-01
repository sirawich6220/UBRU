from flask import Flask, render_template

app = Flask(__name__)

my_friends = [
    {'id': '1-01-2024', 'name': 'DVL_RedeemCODE', 'Support': 'ยังใช้งานอยู่', 'ip': '128.168.192', 'info': 'ระบบกรอกโค๊ด', 'fb': '@fb_johndoe'},
    {'id': '2-01-2024', 'name': 'DVL_Identity', 'Support': 'ยังใช้งานอยู่', 'ip': '192.168.0', 'info': 'ระบบสมัครตัวละคร', 'fb': '@fb_tombrad'},
    {'id': '3-01-2024', 'name': 'DVL_RedeemCODE', 'Support': 'ยังใช้งานอยู่', 'ip': '192.168.198', 'info': 'ระบบกรอกโค๊ด', 'fb': '@fb_psue'},
    {'id': '4-01-2024', 'name': 'DVL_Identity', 'Support': 'ยังใช้งานอยู่', 'ip': '192.168.196', 'info': 'ระบบสมัครตัวละคร', 'fb': '@fb_jennifer'},
    {'id': '5-01-2024', 'name': 'DVL_RedeemCODE', 'Support': 'ยังใช้งานอยู่', 'ip': '192.168.194', 'info': 'ระบบกรอกโค๊ด', 'fb': '@fb_tomhanks'}
]

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/friends')
def friends():
    return render_template('friends.html', title='Order', friends=my_friends)

""" @app.route('/friends/<int:id>')
def friend_info(id):
    friend = None
    for f in my_friends:
        if f['id'] == id:
            friend = f
            break
    return render_template('friend_info.html', title="Friend's Info", friend=friend) """

@app.route('/friends/<id>')
def friend_info(id):
    friend = None
    for f in my_friends:
        if f['id'] == id:
            friend = f
            break
    
    return render_template('friend_info.html', title="Script", friend=friend)

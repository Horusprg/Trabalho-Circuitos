from cv2 import split
from datetime import datetime
from flask import Flask, render_template
from flask_qrcode import QRcode

app = Flask(__name__)
QRcode(app)
@app.route("/")
def none():
    return "Hello"
@app.route("/user/<info>")
def home(info):
    info = str(info)
    date, hour, status = info.split("$")
    datestr = datetime.strptime(date, '%d!%m!%y')
    datestr = datestr.strftime("%d/%m")
    if status == 'false':
        return render_template("home.html", date=date, hour=hour, status=status, datestr=datestr)

@app.route("/payment/<info>")
def payment(info):
    info = str(info)
    date, hour, status = info.split("$")
    datestr = datetime.strptime(date, '%d!%m!%y')
    hourout = datetime.now()
    time = hourout - datetime.strptime(hour, '%H:%M')
    time = str(time).split(" ")
    time = time[2]
    time = str(time).split(".")
    time = time[0]

    hourout = str(hourout).split(" ")
    dateout = hourout[0]
    hourout = hourout[1]
    hourout = str(hourout).split(".")
    hourout = hourout[0]
    datestr = datestr.strftime("%d/%m")
    if status == 'false':
        status = 'true'
        return render_template("payment.html",
                            date=date,
                            hour=hour,
                            status=status,
                            datestr=datestr,
                            hourout=hourout,
                            time=time,
                            dateout=dateout)
    
@app.route("/exit/<info>")
def exit(info):
    info = str(info)
    date, hour, status = info.split("$")
    return render_template("exit.html", date=date, hour=hour, status=status)

if __name__ == "__main__":
    app.run(debug=True)
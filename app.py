import numpy as np
from flask import Flask,request,jsonify,render_template

from download_vids import download_videos
from email_send import mail_user

app=Flask(__name__)


@app.route("/",methods=["GET","POST"])

def main_page():
    if request.method == "POST":
        singer_name = request.form['singer_name'].replace(' ','').lower()
        email_id = request.form['email_id']
        num_vids = int(request.form['num_vids'])
        download_videos(singer_name,num_vids)
        mail_user(email_id)
        # print(keyword,emailid,limit)
    return render_template("index_youtube.html")


if __name__=="__main__":
    app.run(debug=True)

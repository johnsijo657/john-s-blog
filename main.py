from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
import smtplib
POST_IMAGES = {
    1: "static/assets/img/cactus.jpg",
    2: "static/assets/img/bored.jpg",
    3:"static/assets/img/fasting.jpg"
}
load_dotenv() 
blog_url=os.getenv("api_endpoint")
app_password=os.getenv("app_password")
app = Flask(__name__)

@app.route('/')
def home():
    
    response=requests.get(url=blog_url).json()
    # for i in response:
    #     if i["id"]==id:
    #         title=i["title"]
    #         body=i['body']
    #return render_template("index.html",Title=title,Post_Body=body)
    return render_template("index.html",allposts=response)
@app.route('/index.html')
def index():
    response=requests.get(url=blog_url).json()
    return render_template("index.html",allposts=response)
@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route("/post.html")
def sample_post():
    return render_template("post.html")

@app.route('/<int:id>')
def body_blog(id):
    response=requests.get(url=blog_url).json()
    for i in response:
        if i["id"]==id:
            is_list = isinstance(i["body"], list)
            return render_template(
                "custom_post.html",
                Title=i["title"],
                Post_Body=i["body"],
                is_list=is_list,  # Pass a flag to the template
                sub_title=i["subtitle"],post_image=POST_IMAGES[id]
            )
@app.route("/contact-form",methods=['POST'])

def contact_information():
    def send_mail(name,email,phone,message):
        smtp_object=smtplib.SMTP("smtp.gmail.com",587,timeout=30)
        smtp_object.starttls()

        smtp_object.login("teachablemech@gmail.com",app_password) 
        smtp_object.sendmail("teachablemech@gmail.com","teachablemech@gmail.com",f"subject:message from {name}\n{message}\nemail:{email}\nPhone:{phone}")
        smtp_object.close()

    if request.method == 'POST':
        username=request.form.get('name')
        user_email=request.form.get('email')
        user_phone=request.form.get("phone")
        user_message=request.form.get("message")
        send_mail(username,user_email,user_phone,user_message)
        return render_template("contact.html", success=True)
    


# if __name__ == "__main__":
#     app.run(debug=True)

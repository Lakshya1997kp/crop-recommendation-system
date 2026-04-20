from flask import Flask, render_template, request , url_for , redirect , flash, session, Response
from datetime import timedelta
from auth_service import authentication_for_signup, authentication_for_login
from model_utils import ml_prediction
import sklearn
from user_service import get_userdata, update_email, update_name, delete_account
from prometheus_client import Counter, Gauge, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time 
import os
from dotenv import load_dotenv
load_dotenv()


app=Flask(__name__)

http_requests_total=Counter("http_requests_total", "Total number of http requests made", ["endpoint", "method", "status"])
login_attempts_total = Counter('login_attempts_total', 'Total login attempts')
login_failures_total = Counter('login_failures_total', 'Total failed logins')
signups_total = Counter('signups_total', 'Total registrations')
predictions_total = Counter('predictions_total', 'Total predictions made')

active_users = Gauge("active_users", "Total number of active users right now")


prediction_latency = Histogram('prediction_latency_seconds', 'ML model prediction time')
request_latency = Histogram('request_latency_seconds', 'Overall request latency', ['endpoint'])







app.secret_key = os.environ.get("SECRET_KEY", "hello")
app.permanent_session_lifetime=timedelta(minutes=10)


@app.before_request
def start_timer():
    request.start_time=time.time()



@app.after_request
def track_request(response):
    request_latency.labels(endpoint=request.path).observe(time.time()-request.start_time)
    http_requests_total.labels(endpoint=request.path , method= request.method, status=response.status_code).inc()
    return response


@app.teardown_request
def track_failed_requests(exception):
    if exception is not None:
        http_requests_total.labels(
            endpoint=request.path,
            method=request.method,
            status=500
        ).inc()



@app.route("/", methods=["GET", "POST"])
def home():
    if 'user' in session:
        flash("Already logged in!!")
        return redirect(url_for("prediction"))

    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        if (authentication_for_login(email,password)):
            session["user"]=email
            session.permanent=True
            login_attempts_total.inc()
            active_users.inc()
            flash("Login successful!!", "success")
            return redirect(url_for("prediction"))
        else:
            login_attempts_total.inc()
            login_failures_total.inc()
            flash("Invalid credentials!!","error")
            return render_template("login.html")           
    else:
        return render_template("login.html")
    

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    if 'user' not in session:
         flash("you are not logged in!!")
         return redirect(url_for("home"))
    if request.method=="POST":
        features=[float(x) for x in request.form.values()]

        start=time.time()

        prediction=ml_prediction(features)

        latency=time.time()-start
        prediction_latency.observe(latency)
        if prediction:
             prediction=prediction.title()

             predictions_total.inc()

             return render_template("prediction.html", result =f"The Recommended crop is: {prediction} ")
        else:
             return render_template("prediction.html", result =f"Please Fill valid arguments according to the given features")
    return render_template("prediction.html")




@app.route("/register", methods=["GET","POST"])
def register():
        if request.method=="POST":
            
            name=request.form.get("name")
            email=request.form.get("email")
            password=request.form.get("password")
            confirm_password=request.form.get("confirm_password")

            
            if confirm_password != password:
                flash("Your password did not matched !!")
                return redirect(url_for("register"))
            
            error_message = authentication_for_signup(name, email , password)
            
            if error_message:
                flash(error_message)
                return redirect(url_for("register"))
            else:
                signups_total.inc()
                flash("Account created")
                return redirect(url_for("home"))



        return render_template("register.html")




@app.route("/about")
def about():
    if 'user' in session:
        return render_template("about.html")
    else:
        flash("you are not logged in !!")
        return redirect(url_for("home"))
    



@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user', None)
        active_users.dec()
        flash("Logged out successfully!!")
        return redirect(url_for("home"))
    else:
        flash("you are not logged in!!")
        return redirect(url_for("home"))




@app.route("/profile", methods=["GET"])
def profile():
    if 'user' not in session:
         flash("you are not logged in!!")
         return redirect(url_for("home"))
    
    userdata=get_userdata(session['user'])
    if userdata:
        return render_template("profile.html", name=userdata[0], email=userdata[1])
    



@app.route("/profile/<name>",methods=["POST"])
def services(name):
    if 'user' not in session:
        flash("you are not logged in!!")
        return redirect(url_for("home"))
    
    email=session['user']

    if name=="update_name":
        new_name=request.form.get('name')
        update=update_name(new_name,email)
        return redirect(url_for("profile"))
    
    if name=="update_email":
        new_email=request.form.get('email')
        update=update_email(new_email,email)
        flash("Email changed successfully !!" \
        "login again!!")        

        return redirect(url_for("logout")) 

    if name=="delete_account":
        delete_account(email)
        flash("Your account has been successfully deleted!!")
        session.pop('user',None)
        return redirect(url_for("register"))


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST )


if __name__=="__main__":
    app.run(debug=True)


 
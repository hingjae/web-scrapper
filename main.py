from indeed import get_jobs as get_indeed_jobs
# from so import get_jobs as get_so_jobs
from flask import Flask, render_template, request, redirect, send_file
from save import save_to_file

app = Flask("SuperScrapper")

db={}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_indeed_jobs(word)        
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html", 
        searchingBy=word, 
        resultsNumber=len(jobs),
        jobs = jobs
    )

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")

app.run(host="0.0.0.0")

# so_jobs = get_so_jobs()
# indeed_jobs = get_indeed_jobs()
# jobs = indeed_jobs + so_jobs
# save_to_file(jobs)
from indeed import get_jobs as get_indeed_jobs
# from so import get_jobs as get_so_jobs
from save import save_to_file
from flask import Flask, render_template, request, redirect

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
        fromDb = db.get(word)
        if fromDb:
            jobs = fromDb
        else:
            jobs = get_indeed_jobs(word)        
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word, resultsNumber=len(jobs))


app.run(host="0.0.0.0")

# so_jobs = get_so_jobs()
# indeed_jobs = get_indeed_jobs()
# jobs = indeed_jobs + so_jobs
# save_to_file(jobs)
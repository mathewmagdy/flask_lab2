from flask import Flask, render_template, request, redirect, url_for
from data import companies, jobs
from models import Company

app = Flask(__name__)

@app.route("/companies-view")
def list_companies():
    return render_template("list.html", companies=companies)

@app.route("/companies/<int:id>")
def company_detail(id):
    company = next((c for c in companies if c.id == id), None)
    return render_template("detail.html", company=company)

@app.route("/companies/new", methods=["GET", "POST"])
def create_company():
    if request.method == "POST":
        name = request.form["name"]
        location = request.form["location"]
        business = request.form["business"]
        employees = int(request.form["employees_count"])
        new_company = Company(name, location, business, employees)
        companies.append(new_company)
        return redirect(url_for("company_detail", id=new_company.id))
    return render_template("form.html")

@app.route("/jobs-view/<int:id>")
def job_view(id):
    job = next((j for j in jobs if j.id == id), None)
    company = next((c for c in companies if c.id == job.company_id), None)
    return render_template("job.html", job=job, company=company)

if __name__ == "__main__":
    app.run(debug=True)

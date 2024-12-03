from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
from sqlalchemy import text
import asyncio

app = Flask(__name__)

# 10 lax, 15 lax etc.
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$150,000'
    },
]


@app.route('/')
def index():
    jobs = asyncio.run(load_jobs_from_db())
    # print(jobs)
    return render_template('home.html', jobs=jobs)
    # return "jobs"


@app.route('/api/jobs')
def list_jobs():
    jobs = asyncio.run(load_jobs_from_db())
    return jsonify(jobs)


@app.route('/job/<id>')
def show_job(id):
    job = asyncio.run(load_job_from_db(id))
    
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job=job)


@app.route('/job/<id>/apply', methods=['GET', 'POST'])
def apply_to_job(id):
    data = request.form
    job = asyncio.run(load_job_from_db(id))
    asyncio.run(add_application_to_db(id, data))
    return render_template('application_submitted.html', application=data, job=job)
    # return render_template('application_submitted.html', application=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
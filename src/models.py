from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)
    location = db.Column(db.String)
    description = db.Column(db.Text)
    url = db.Column(db.String, unique=True)
    discarded = db.Column(db.Boolean, default=False)
    # Add other fields as necessary

class RawHTML(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    html_content = db.Column(db.Text)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    job = db.relationship('Job', backref=db.backref('raw_html', lazy=True))

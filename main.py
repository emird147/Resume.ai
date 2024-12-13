from flask import Flask, render_template, request, send_file
from pdf import generate_pdf
from utils import enhance_internship_description, enhance_project_description
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume_builder')
def resume_builder():
    return render_template('resume_builder.html')

@app.route('/generate-resume', methods=['POST'])
def generate_resume():
    data = request.json

    # Call enhancement functions for descriptions
    data['internship_info']['internship_description'] = enhance_internship_description(
        data['internship_info']['internship_description']
    )
    data['proj_info']['proj_description'] = enhance_project_description(
        data['proj_info']['proj_description']
    )

    # Generate the PDF
    pdf_path = "resume.pdf"
    generate_pdf(data)

    # Return the PDF file as a download
    if os.path.exists(pdf_path):
        return send_file(pdf_path, as_attachment=True, mimetype='application/pdf')
    else:
        return {"error": "Failed to generate PDF"}, 500


if __name__ == '__main__':
    app.run(debug=True)

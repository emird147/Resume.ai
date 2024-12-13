from utils import enhance_internship_description

# pdf.py
from fpdf import FPDF
from tkinter import messagebox

class PDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_data = None

    def format_personal_info(self, data):
        # Capitalize the name
        data['personal_info']['name'] = data['personal_info']['name'].upper()

        # Format the contact information
        contact_info = f"{data['personal_info']['email']} | {data['personal_info']['linkedin']} | {data['personal_info']['github']} | {data['personal_info']['location']}"
        return data['personal_info']['name'], contact_info

    def header(self):
        if self.user_data:
            name, contact_info = self.format_personal_info(self.user_data)
            self.cell(0, 10, name, ln=True)
            self.set_font('Times', '', 10)
            self.cell(0, 10, contact_info, ln=True)
            self.ln(10)
            self.set_font('Times', 'B', 10)
        else:
            pass

    def chapter_title(self, title):
        self.set_font('Times', 'B', 10)
        self.cell(0, 10, title, ln=True)
        self.line(11, self.get_y() - 3, 200, self.get_y() - 3)  # Horizontal line
        self.ln(-5)

    def chapter_body(self, body):
        if body is None:
            body = ''  # Replace None with an empty string
        try:
            self.set_font('Times', '', 10)
            self.multi_cell(0, 10, body)
            self.ln()
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred while generating PDF: {e}')

def generate_pdf(data):
    pdf = PDF()
    pdf.add_page()

    pdf.user_data = data
    name = pdf.format_personal_info(data)

    # Name (Capitalized)
    pdf.set_font('Times', 'B', 16)
    pdf.cell(0, 5, data['personal_info']['name'], ln=True, align='C')

    # Concatenated Contact Info (Email, LinkedIn, GitHub, Location)
    concatenated_contact_info = f"{data['personal_info'].get('email', 'N/A')} | " \
                                f"{data['personal_info'].get('linkedin', 'N/A')} | " \
                                f"{data['personal_info'].get('github', 'N/A')} | " \
                                f"{data['personal_info'].get('location', 'N/A')}"
    pdf.set_font('Times', '', 10)
    pdf.cell(0, 5, concatenated_contact_info, ln=True, align='C')
    pdf.ln(5)

    
    
    # Education
    pdf.chapter_title('EDUCATION')

    concatenated_school = f"{data['education']['school']}"
    concatenated_degree = f"Bachelors of {data['education']['degree']}, {data['education']['major']}: {data['education']['graduation_date']}"
    concatenated_relevant_courses = f"Relevant Courses: {data['education']['relevant_courses']}"

    pdf.set_font('Times', 'B', 10)

    # Calculate width of the window and the school name
    page_width = pdf.w - 2*pdf.l_margin
    school_width = pdf.get_string_width(concatenated_school) + 2

    # Print 'school' on the left
    pdf.cell(school_width, 10, concatenated_school, ln=0)

    # Move to the right for 'school location'
    pdf.set_x(page_width - pdf.get_string_width(data['education']['school_location']))
    
    pdf.set_font('Times', '', 10)
    pdf.cell(0, 10, data['education']['school_location'], ln=True, align='R')

    pdf.set_y(pdf.get_y() - 6)

    pdf.set_font('Times', '', 10)
    pdf.chapter_body(concatenated_degree)

    pdf.set_y(pdf.get_y() - 16)

    pdf.set_font('Times', '', 10)
    pdf.chapter_body(f"GPA: {data['education']['gpa']}")

    pdf.set_y(pdf.get_y() - 16)

    pdf.set_font('Times', '', 10)
    pdf.chapter_body(concatenated_relevant_courses)
    

    pdf.ln(-10)
    
    
    
    
    # Internship Experience
    pdf.chapter_title('EXPERIENCE')

    # Set initial font
    pdf.set_font('Times', '', 10)

    # Concatenated internship details
    concatenated_internship = f"{data['internship_info']['internship_company']} | {data['internship_info']['internship_position']} | {data['internship_info']['internship_location']}"

    # Calculate width of concatenated internship
    pdf.cell(0, 10, concatenated_internship, ln=0)

    # Align internship date on the right
    internship_date = data['internship_info'].get('internship_date', 'N/A')
    date_width = pdf.get_string_width(data['internship_info']['internship_date'])
    pdf.set_x(210 - date_width - 10)  # 210 mm is A4 width, 10 mm for right margin
    pdf.cell(date_width, 10, internship_date, ln=True)

    pdf.ln(-2)  # Add some space after the header
    
    # Internship Description
    pdf.set_font('Times', '', 10)
    indentation = 20  # Set the indentation value here
    if isinstance(data['internship_info']['internship_description'], list):
        for bullet_point in data['internship_info']['internship_description']:
            pdf.set_x(pdf.get_x() + indentation)
            pdf.cell(indentation, 10, '', 0, 0)  # Indent for bullet points
            pdf.multi_cell(0, 10, f"* {bullet_point}")
    else:
        # If the description is not a list, print it directly
        pdf.multi_cell(0, 4, data['internship_info']['internship_description'])

    pdf.ln(2)  # Add some space before the next section


    # Projects
    pdf.chapter_title('PROJECTS')
    
    pdf.set_font('Times', '', 10)

    concatenated_project = f"{data['proj_info']['proj_name']} | {data['proj_info']['proj_url']}"

    # Calculate width of concatenated internship
    pdf.cell(0, 10, concatenated_project, ln=0)

    # Align internship date on the right
    project_date = data['proj_info'].get('proj_date', 'N/A')
    date_width = pdf.get_string_width(data['proj_info']['proj_date'])
    pdf.set_x(210 - date_width - 10)  # 210 mm is A4 width, 10 mm for right margin
    pdf.cell(date_width, 10, project_date, ln=True)

    pdf.ln(-2)

    pdf.set_font('Times', '', 10)
    indentation = 20  # Set the indentation value here
    if isinstance(data['proj_info']['proj_description'], list):
        for bullet_point in data['proj_info']['proj_description']:
            pdf.set_x(pdf.get_x() + indentation)
            pdf.cell(indentation, 10, '', 0, 0)  # Indent for bullet points
            pdf.multi_cell(0, 10, f"* {bullet_point}")
    else:
        # If the description is not a list, print it directly
        pdf.multi_cell(0, 4, data['proj_info']['proj_description'])

    pdf.ln(2)


    # Technical Skills
    pdf.chapter_title('TECHNICAL SKILLS')

    concatenated_prog_languages = f"Programming Languages: {data['skills_info'].get('prog_languages', 'N/A')}"
    concatenated_applications = f"Applications: {data['skills_info'].get('applications', 'N/A')}"
    concatenated_os = f"Operating Systems: {data['skills_info'].get('os', 'N/A')}"
    concatenated_design_software = f"Design Software: {data['skills_info'].get('design_software', 'N/A')}"
    
    pdf.set_font('Times', '', 10)
    pdf.cell(0, 10, concatenated_prog_languages, ln=True, align='L')

    pdf.set_y(pdf.get_y() - 6)

    pdf.set_font('Times', '', 10)
    pdf.chapter_body(concatenated_applications)

    pdf.set_y(pdf.get_y() - 16)

    pdf.set_font('Times', '', 10)
    pdf.chapter_body(concatenated_os)

    pdf.set_y(pdf.get_y() - 16)

    pdf.set_font('Times', '', 10)
    pdf.chapter_body(concatenated_design_software)


    pdf.output("resume.pdf", 'F')




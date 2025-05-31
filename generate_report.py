import csv
from fpdf import FPDF

# Step 1: Read CSV data
def read_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

# Step 2: Analyze the data
def analyze_data(data):
    scores = [int(row['Score']) for row in data]
    analysis = {
        'count': len(scores),
        'average': sum(scores) / len(scores),
        'min': min(scores),
        'max': max(scores)
    }
    return analysis

# Step 3: Generate PDF using FPDF
def generate_pdf(data, analysis, output_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)

    pdf.cell(200, 10, "Student Score Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, f"Total Students: {analysis['count']}", ln=True)
    pdf.cell(200, 10, f"Average Score: {analysis['average']:.2f}", ln=True)
    pdf.cell(200, 10, f"Highest Score: {analysis['max']}", ln=True)
    pdf.cell(200, 10, f"Lowest Score: {analysis['min']}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, "Name", 1)
    pdf.cell(50, 10, "Score", 1, ln=True)

    pdf.set_font("Arial", size=12)
    for row in data:
        pdf.cell(100, 10, row['Name'], 1)
        pdf.cell(50, 10, row['Score'], 1, ln=True)

    pdf.output(output_filename)

# Run the whole process
if __name__ == "__main__":
    data = read_data("data.csv")
    analysis = analyze_data(data)
    generate_pdf(data, analysis, "student_report.pdf")
    print("Report generated: student_report.pdf")


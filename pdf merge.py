from pypdf import PdfReader, PdfWriter

writer = PdfWriter()

pdfs = [
    "PHYSICS_MED_EASY_(1)(1)(1).pdf",
    "PW NCERT PUNCH [ NEW ] CHEMISTRY BY TEAM KOHINOOR  (1).pdf",
    "chemistry_Med_easy.pdf",
]

for pdf in pdfs:
    reader = PdfReader(pdf)
    for page in reader.pages:
        writer.add_page(page)

with open("merged_output.pdf", "wb") as output_file:
    writer.write(output_file)
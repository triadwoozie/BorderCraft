import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, LETTER, landscape, portrait
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_document(file_name, paper_size, margin, border_thickness, page_color, border_color, num_pages):
    if os.path.exists(file_name):
        os.remove(file_name)
        
    # Create the PDF
    c = canvas.Canvas(file_name, pagesize=paper_size)
    
    for page_num in range(num_pages):
        # Set the page color
        c.setFillColor(page_color)
        c.rect(0, 0, paper_size[0], paper_size[1], fill=True, stroke=False)
        
        # Set the border color
        c.setStrokeColor(border_color)
        
        # Draw the border
        c.setLineWidth(border_thickness)
        c.rect(margin, margin, paper_size[0] - 2 * margin, paper_size[1] - 2 * margin, fill=False)

        # Optional: Add page number text
        c.drawString(paper_size[0] - 50, 20, f'Page {page_num + 1}')

        # Finish the current page
        c.showPage()
    
    c.save()
    print(f"Document '{file_name}' with {num_pages} pages created successfully.")

def choose_paper_size():
    sizes = {
        1: A4,
        2: LETTER,
        3: landscape(A4),
        4: portrait(LETTER)
    }
    
    print("Choose paper size:")
    print("1. A4")
    print("2. LETTER")
    print("3. Landscape A4")
    print("4. Portrait LETTER")
    
    choice = int(input("Enter your choice (1-4): "))
    return sizes.get(choice, A4)

def choose_color(prompt):
    print(f"Enter RGB values (0-255) for {prompt} color.")
    r = int(input("Red (0-255): "))
    g = int(input("Green (0-255): "))
    b = int(input("Blue (0-255): "))
    return colors.Color(r / 255, g / 255, b / 255)

def main():
    file_name = "generated_document.pdf"
    
    while True:
        paper_size = choose_paper_size()
        
        margin = float(input("Enter margin distance from the page edge (in inches): ")) * inch
        border_thickness = float(input("Enter border thickness (in points): "))
        num_pages = int(input("Enter the number of pages: "))
        
        change_colors = input("Do you want to change the default colors? (y/n): ").lower()
        if change_colors == 'y':
            page_color = choose_color("page background")
            border_color = choose_color("border")
        else:
            page_color = colors.white
            border_color = colors.black
        
        # Create the document
        create_document(file_name, paper_size, margin, border_thickness, page_color, border_color, num_pages)
        
        rerun = input("Is the result correct? (y/n): ").lower()
        if rerun == 'y':
            break

if __name__ == "__main__":
    main()

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from datetime import datetime
import os

# Create PDF
pdf_path = "NGO_Report.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, topMargin=1*inch, bottomMargin=1*inch, leftMargin=1*inch, rightMargin=1*inch)

# Container for PDF elements
elements = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=20,
    textColor=colors.HexColor('#1a1a1a'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.white,
    spaceAfter=8,
    spaceBefore=10,
    fontName='Helvetica-Bold',
    backColor=colors.HexColor('#1a1a1a'),
    borderPadding=10,
    leftIndent=6,
    rightIndent=6
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=11,
    alignment=TA_JUSTIFY,
    spaceAfter=10,
    leading=14,
    textColor=colors.HexColor('#333333')
)

center_style = ParagraphStyle(
    'CustomCenter',
    parent=styles['Normal'],
    fontSize=10,
    alignment=TA_CENTER,
    spaceAfter=4
)

# Title Page - Professional Design
elements.append(Spacer(1, 0.8*inch))

# Main Title
title_block_style = ParagraphStyle(
    'TitleBlock',
    parent=styles['Heading1'],
    fontSize=26,
    textColor=colors.HexColor('#1a1a1a'),
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
    leading=32
)
elements.append(Paragraph("NGO / CHARITY DONATION WEBSITE", title_block_style))
elements.append(Spacer(1, 0.08*inch))

# Subtitle
subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=12,
    textColor=colors.HexColor('#666666'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica'
)
elements.append(Paragraph("Project Documentation Report", subtitle_style))
elements.append(Spacer(1, 0.4*inch))

# Course Information Table - Enhanced Professional Style
course_data = [
    ['Course', 'O Level'],
    ['Name', 'Akriti'],
    ['Registration Number', '167855'],
    ['Class Roll Number', '289'],
    ['Centre', 'NIELIT, Shimla'],
    ['Session', '2025-26'],
]

course_table = Table(course_data, colWidths=[2.2*inch, 2.8*inch])
course_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a1a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#333333')),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 11),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ('TOPPADDING', (0, 0), (-1, -1), 12),
    ('LEFTPADDING', (0, 0), (-1, -1), 14),
    ('RIGHTPADDING', (0, 0), (-1, -1), 14),
    ('GRID', (0, 0), (-1, -1), 1.2, colors.HexColor('#dddddd')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
    ('SPLIT', (0, 0), (-1, -1), True)
]))

elements.append(course_table)
elements.append(Spacer(1, 1*inch))
elements.append(PageBreak())

# Acknowledgement
elements.append(Paragraph("ACKNOWLEDGEMENT", heading_style))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph(
    "I am grateful to <b>Ms. Aarti</b> for her invaluable guidance and support. Special thanks to NIELIT institution for providing resources. This project is a culmination of dedication and valuable feedback from instructors.",
    body_style
))
elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph(
    "<b>Project Overview:</b><br/>A modern, responsive web application for online donations, built with HTML5, CSS3, and JavaScript. It facilitates charitable giving and donor engagement.",
    body_style
))
elements.append(Spacer(1, 0.05*inch))
elements.append(Paragraph(
    "<b>Purpose:</b><br/>Increase donations, improve accessibility to charitable giving, and provide transparency about organizational work.",
    body_style
))
elements.append(PageBreak())

# Introduction
elements.append(Paragraph("INTRODUCTION", heading_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph(
    "<b>Aim:</b><br/>Create a professional digital platform for charitable organizations to facilitate seamless online donations, increase awareness about charitable causes, and build donor trust.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph(
    "<b>Advantages:</b><br/>" +
    "• User-friendly, responsive design<br/>" +
    "• Fast performance with smooth animations<br/>" +
    "• Real-time donation impact tracking<br/>" +
    "• Easy navigation and accessibility",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph(
    "<b>Key Features:</b><br/>" +
    "• Responsive design (mobile, tablet, desktop)<br/>" +
    "• Online donation system with amount selection<br/>" +
    "• Multiple charitable causes with progress tracking<br/>" +
    "• Contact and inquiry management<br/>" +
    "• Impact statistics display",
    body_style
))
elements.append(PageBreak())

# Technology Used
elements.append(Paragraph("TECHNOLOGY USED", heading_style))
elements.append(Spacer(1, 0.2*inch))

tech_data = [
    ['Tech', 'Purpose', 'Details'],
    ['HTML5', 'Structure', 'Foundation with semantic elements'],
    ['CSS3', 'Styling', 'Layouts with animations and responsiveness'],
    ['JavaScript', 'Interactivity', 'Validation, scrolling, and animations'],
]

tech_table = Table(tech_data, colWidths=[0.9*inch, 1.3*inch, 2.8*inch])
tech_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a1a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#333333')),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 11),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ('TOPPADDING', (0, 0), (-1, -1), 10),
    ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#dddddd')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
    ('SPLIT', (0, 0), (-1, -1), True)
]))

elements.append(tech_table)
elements.append(PageBreak())

# Implementation
elements.append(Paragraph("IMPLEMENTATION", heading_style))
elements.append(Spacer(1, 0.2*inch))

elements.append(Paragraph(
    "<b>Architecture:</b><br/>" +
    "Modular HTML with semantic sections, CSS3 styling with responsive design, and JavaScript for interactivity. Mobile hamburger menu, form validation, and Intersection Observer API for animations.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph(
    "<b>Technical Stack:</b><br/>" +
    "• HTML5: Semantic markup and structure<br/>" +
    "• CSS3: Responsive design with media queries (320px to 1200px+)<br/>" +
    "• JavaScript: Interactivity, validation, animations<br/>" +
    "• ReportLab: PDF generation",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph(
    "<b>Features Implemented:</b><br/>" +
    "Eye-catching quotes, progress bars, donation system, contact forms, smooth animations, responsive navigation, and impact visualization.",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph(
    "<b>Live Demo:</b><br/>" +
    "charity-donation-eight.vercel.app",
    body_style
))
elements.append(PageBreak())

# Result
elements.append(Paragraph("RESULT", heading_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph(
    "Successfully completed and thoroughly tested. The website works effectively across all devices:",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

results_data = [
    ['Feature', 'Status', 'Performance'],
    ['Responsive Design', '✓ Complete', 'Works on all devices'],
    ['Navigation', '✓ Complete', 'Smooth with hamburger menu'],
    ['Donation System', '✓ Complete', 'Form validation works'],
    ['Animations', '✓ Complete', 'Smooth CSS and JS'],
    ['Accessibility', '✓ Complete', 'WCAG compliant'],
    ['Performance', '✓ Optimized', 'Fast loading'],
    ['Cross-browser', '✓ Tested', 'Chrome, Firefox, Safari, Edge'],
]

results_table = Table(results_data, colWidths=[1.3*inch, 1*inch, 2.7*inch])
results_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a1a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#333333')),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 11),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ('TOPPADDING', (0, 0), (-1, -1), 10),
    ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#dddddd')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
    ('SPLIT', (0, 0), (-1, -1), True)
]))

elements.append(results_table)
elements.append(PageBreak())

# Website Screenshots Section
elements.append(Paragraph("WEBSITE SCREENSHOTS", heading_style))
elements.append(Spacer(1, 0.2*inch))

elements.append(Paragraph(
    "<b>Screenshot 1: Homepage with Hero Section</b><br/><br/>The homepage features an eye-catching hero section with gradient background, motivational quote, and clear call-to-action button to encourage donations.",
    body_style
))
elements.append(Spacer(1, 0.1*inch))

# Add screenshot 1 image
if os.path.exists('images/home page.png'):
    img1 = Image('images/home page.png', width=4.8*inch, height=2.7*inch)
    elements.append(img1)
else:
    elements.append(Paragraph("[Homepage Screenshot - Image not found]", body_style))
elements.append(Spacer(1, 0.3*inch))

elements.append(Paragraph(
    "<b>Screenshot 2: Causes Section with Progress Bars</b><br/><br/>Displays four charitable causes (Education, Healthcare, Shelter, Environment) with icons, descriptions, and funding progress bars to show impact.",
    body_style
))
elements.append(Spacer(1, 0.1*inch))

# Add screenshot 2 image
if os.path.exists('images/causes.png'):
    img2 = Image('images/causes.png', width=4.8*inch, height=2.7*inch)
    elements.append(img2)
else:
    elements.append(Paragraph("[Causes Screenshot - Image not found]", body_style))
elements.append(Spacer(1, 0.3*inch))

elements.append(Paragraph(
    "<b>Screenshot 3: Donation Form Section</b><br/><br/>Interactive donation form with preset amount buttons ($10, $25, $50, $100, Custom), donor information fields, cause selection, and secure payment button.",
    body_style
))
elements.append(Spacer(1, 0.1*inch))

# Add screenshot 3 image
if os.path.exists('images/donation section.png'):
    img3 = Image('images/donation section.png', width=4.8*inch, height=2.7*inch)
    elements.append(img3)
else:
    elements.append(Paragraph("[Donation Form Screenshot - Image not found]", body_style))
elements.append(Spacer(1, 0.3*inch))

elements.append(PageBreak())

# Conclusion
elements.append(Paragraph("CONCLUSION", heading_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph(
    "Successfully developed as a professional platform combining modern web design with practical functionality for intuitive donation experiences.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph(
    "<b>Key Achievements:</b><br/>" +
    "• Fully responsive website across all devices<br/>" +
    "• Engaging UI with motivational content<br/>" +
    "• Functional donation and contact forms<br/>" +
    "• Smooth animations and transitions<br/>" +
    "• Optimal performance and accessibility",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph(
    "<b>Future Scope:</b><br/>Payment gateway integration, database backend, admin dashboard, email notifications, analytics, and multi-language support.",
    body_style
))

elements.append(PageBreak())

# Bibliography
elements.append(Paragraph("BIBLIOGRAPHY", heading_style))
elements.append(Spacer(1, 0.15*inch))

bibliography_items = [
    "MDN Web Docs - HTML, CSS, JavaScript (https://developer.mozilla.org/)",
    "W3C Standards (https://www.w3.org/)",
    "CSS-Tricks - CSS Resources (https://css-tricks.com/)",
    "WCAG Accessibility Guidelines (https://www.w3.org/WAI/WCAG21/)",
    "ReportLab - PDF Library (https://www.reportlab.com/)",
]

for item in bibliography_items:
    elements.append(Paragraph(f"• {item}", body_style))

elements.append(PageBreak())

# Appendix
elements.append(Paragraph("APPENDIX", heading_style))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("<b>A. Core Code Structure</b>", body_style))
elements.append(Spacer(1, 0.08*inch))

# HTML Structure
elements.append(Paragraph("<b>HTML Structure:</b>", body_style))
elements.append(Spacer(1, 0.03*inch))

code_snippet_1 = """
&lt;!DOCTYPE html&gt;<br/>
&lt;html lang="en"&gt;<br/>
&lt;head&gt;<br/>
    &lt;meta charset="UTF-8"&gt;<br/>
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;<br/>
    &lt;title&gt;Hope Foundation - Make a Difference Today&lt;/title&gt;<br/>
&lt;/head&gt;<br/>
&lt;body&gt;<br/>
    &lt;nav class="navbar"&gt; ... &lt;/nav&gt;<br/>
    &lt;section id="home" class="hero"&gt; ... &lt;/section&gt;<br/>
    &lt;section class="quotes-section"&gt; ... &lt;/section&gt;<br/>
    &lt;section id="about" class="about"&gt; ... &lt;/section&gt;<br/>
    &lt;section id="causes" class="causes"&gt; ... &lt;/section&gt;<br/>
    &lt;section id="donate" class="donate-section"&gt; ... &lt;/section&gt;<br/>
    &lt;footer class="footer"&gt; ... &lt;/footer&gt;<br/>
&lt;/body&gt;<br/>
&lt;/html&gt;
"""

elements.append(Paragraph(code_snippet_1, ParagraphStyle(
    'Code',
    parent=styles['Normal'],
    fontSize=8,
    fontName='Courier',
    backColor=colors.HexColor('#f5f5f5'),
    borderColor=colors.grey,
    borderWidth=1,
    borderPadding=3
)))

elements.append(Spacer(1, 0.08*inch))
elements.append(Paragraph("<b>CSS Variables:</b>", body_style))
elements.append(Spacer(1, 0.03*inch))

code_snippet_2 = """
:root {<br/>
    --primary-color: #e74c3c;<br/>
    --secondary-color: #3498db;<br/>
    --accent-color: #2ecc71;<br/>
    --dark-bg: #2c3e50;<br/>
    --text-dark: #2c3e50;<br/>
    --shadow: 0 10px 30px rgba(0, 0, 0, 0.1);<br/>
    --transition: all 0.3s ease;<br/>
}
"""

elements.append(Paragraph(code_snippet_2, ParagraphStyle(
    'Code',
    parent=styles['Normal'],
    fontSize=8,
    fontName='Courier',
    backColor=colors.HexColor('#f5f5f5'),
    borderColor=colors.grey,
    borderWidth=1,
    borderPadding=3
)))

elements.append(Spacer(1, 0.08*inch))
elements.append(Paragraph("<b>JavaScript Handling:</b>", body_style))
elements.append(Spacer(1, 0.03*inch))

code_snippet_3 = """
// Mobile Menu Toggle<br/>
const hamburger = document.querySelector('.hamburger');<br/>
const navLinks = document.querySelector('.nav-links');<br/>
<br/>
hamburger.addEventListener('click', () => {<br/>
    navLinks.classList.toggle('active');<br/>
});<br/>
<br/>
// Form Submission Handler<br/>
donationForm.addEventListener('submit', (e) => {<br/>
    e.preventDefault();<br/>
    // Validate and process donation<br/>
});
"""

elements.append(Paragraph(code_snippet_3, ParagraphStyle(
    'Code',
    parent=styles['Normal'],
    fontSize=8,
    fontName='Courier',
    backColor=colors.HexColor('#f5f5f5'),
    borderColor=colors.grey,
    borderWidth=1,
    borderPadding=3
)))

elements.append(Spacer(1, 0.08*inch))
elements.append(Paragraph("<b>Responsive Design Example:</b>", body_style))
elements.append(Spacer(1, 0.03*inch))

code_snippet_4 = """
@media (max-width: 768px) {<br/>
    .nav-links {<br/>
        position: fixed;<br/>
        flex-direction: column;<br/>
        background-color: white;<br/>
        width: 100%;<br/>
    }<br/>
    <br/>
    .hero h1 {<br/>
        font-size: 36px;<br/>
    }<br/>
    <br/>
    .form-grid {<br/>
        grid-template-columns: 1fr;<br/>
    }<br/>
}
"""

elements.append(Paragraph(code_snippet_4, ParagraphStyle(
    'Code',
    parent=styles['Normal'],
    fontSize=8,
    fontName='Courier',
    backColor=colors.HexColor('#f5f5f5'),
    borderColor=colors.grey,
    borderWidth=1,
    borderPadding=3
)))

elements.append(PageBreak())

# Project Files Summary
elements.append(Paragraph("<b>B. Project Files Summary</b>", body_style))
elements.append(Spacer(1, 0.08*inch))

files_data = [
    ['File Name', 'Purpose', 'Size'],
    ['index.html', 'HTML structure', '~12 KB'],
    ['styles.css', 'Styling & design', '~18 KB'],
    ['script.js', 'Interactivity', '~8 KB'],
    ['NGO_Report.pdf', 'Documentation', '~500 KB'],
]

files_table = Table(files_data, colWidths=[1.4*inch, 2.1*inch, 1.5*inch])
files_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a1a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#333333')),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 11),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ('TOPPADDING', (0, 0), (-1, -1), 10),
    ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cccccc')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
    ('SPLIT', (0, 0), (-1, -1), True)
]))

elements.append(files_table)
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("<b>C. Testing Checklist</b>", body_style))
elements.append(Spacer(1, 0.08*inch))

testing_items = [
    "✓ Cross-browser testing (Chrome, Firefox, Safari, Edge)",
    "✓ Responsive design (Mobile, Tablet, Desktop)",
    "✓ Form validation and submission",
    "✓ Navigation and animations",
    "✓ Accessibility (WCAG 2.1)",
    "✓ Performance optimization",
]

for item in testing_items:
    elements.append(Paragraph(f"• {item}", body_style))

elements.append(Spacer(1, 0.15*inch))
elements.append(Paragraph("<b>D. Browser Compatibility</b>", body_style))
elements.append(Spacer(1, 0.08*inch))

compat_items = [
    "Chrome 90+",
    "Firefox 88+",
    "Safari 14+",
    "Edge 90+",
    "Mobile Chrome and Safari (iOS/Android)"
]

for item in compat_items:
    elements.append(Paragraph(f"• {item}", body_style))

# Build PDF
doc.build(elements)
print(f"✓ PDF Report generated successfully: {pdf_path}")
print(f"✓ Location: {os.path.abspath(pdf_path)}")

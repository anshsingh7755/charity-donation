# 🚀 Quick Start Guide

## How to Use the Charity Website

### Step 1: Open the Website
1. Navigate to the project folder: `c:\Users\singh\OneDrive\Desktop\charity_website`
2. Double-click on **`index.html`** to open in your default browser
3. The website will load with all features active!

### Step 2: Explore the Features

**Navigation Bar**
- Click on any menu item (Home, About, Causes, Donate, Contact)
- Use the hamburger menu on mobile devices

**Hero Section**
- Read the inspiring quote
- Click "Donate Now" button to jump to donation section

**Quotes Section**
- View motivational quotes to inspire donations
- Each quote is designed to encourage giving

**About Section**
- Learn about Hope Foundation
- See statistics about impact (50K+ lives changed, 25+ countries, 99% to programs)

**Causes Section**
- Explore four main causes: Education, Healthcare, Shelter, Environment
- See funding progress for each cause
- Understand what each cause provides

**Impact Section**
- See what your donation can achieve
- $10 = Meals for 5 children
- $25 = School supplies for 1 student
- $50 = Medical checkup for 10 people
- $100 = Training for 5 individuals

**Donation Form**
1. Click on a preset amount ($10, $25, $50, $100) or enter custom amount
2. Fill in your details (Name, Email, Phone)
3. Select which cause to support
4. Add an optional message
5. Click "Proceed to Payment" button
6. See confirmation message

**Contact Section**
- Find address: 123 Charity Street, Hope City, HC 12345
- Phone: +1 (555) 123-4567
- Email: info@hopefoundation.org
- Fill contact form to send inquiries
- Subscribe to newsletter

**Footer**
- Follow on social media
- View quick links
- Access privacy policy
- Subscribe to newsletter

### Step 3: View the PDF Documentation
1. Open **`NGO_Charity_Donation_Website_Report.pdf`** to view:
   - Complete project information
   - Implementation details
   - Code samples
   - Testing results
   - Bibliography

## 📱 Mobile View
- The website automatically adapts to mobile size
- Hamburger menu appears on devices smaller than 768px
- All features work perfectly on mobile devices

## ⚙️ Technical Details

### Browser Support
- ✅ Chrome
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

### File Sizes
- `index.html` - ~12 KB (Structure)
- `styles.css` - ~18 KB (Styling)
- `script.js` - ~8 KB (Interactivity)

### Key Features
- Fully responsive design
- Smooth animations
- Form validation
- Mobile hamburger menu
- Smooth scrolling
- Intersection Observer animations
- Counter animations

## 🎨 Customizing the Website

### Change Organization Name
1. Open `index.html`
2. Find "Hope Foundation" text
3. Replace with your organization name

### Change Colors
1. Open `styles.css`
2. Find the `:root` section at the top
3. Modify color variables:
   - `--primary-color`: Main color (donation buttons)
   - `--secondary-color`: Secondary color
   - `--accent-color`: Highlight color

### Update Donation Amounts
1. Open `index.html`
2. Find the "amount-selector" section
3. Modify the data-amount values in buttons

### Update Content
1. Open `index.html`
2. Find the section you want to change
3. Edit text directly
4. Save the file
5. Refresh browser to see changes

## 🐛 Troubleshooting

**Q: Website doesn't load**
- Make sure index.html is in the same folder as styles.css and script.js
- Try opening with a different browser
- Clear browser cache (Ctrl+Shift+Delete)

**Q: Styles don't appear**
- Check if styles.css is in the same directory
- Verify file path in index.html: `<link rel="stylesheet" href="styles.css">`
- Clear browser cache

**Q: Forms don't work**
- Ensure JavaScript is enabled in your browser
- Check browser console for errors (F12 > Console)
- Verify script.js is in same directory

**Q: Mobile menu doesn't appear**
- Check if screen width is less than 768px
- Verify JavaScript is loading properly
- Try refreshing the page

## 📊 Generating PDF Report

If you need to regenerate the PDF:

1. Open terminal/command prompt
2. Navigate to the project folder:
   ```
   cd c:\Users\singh\OneDrive\Desktop\charity_website
   ```
3. Run the Python script:
   ```
   python generate_pdf.py
   ```
4. The PDF will be generated in the same folder

**Note**: Requires Python 3.7+ and reportlab library (already installed)

## 💡 Tips & Tricks

**Best Practices:**
- Test on multiple devices to ensure responsiveness
- Use modern browsers for best experience
- Enable JavaScript for full functionality
- Test forms before deploying to real server

**Performance:**
- Website loads fast with minimal external dependencies
- No heavy frameworks used
- Optimized animations using CSS
- Efficient JavaScript code

**Accessibility:**
- Website is keyboard navigable
- Semantic HTML for screen readers
- Good color contrast
- Readable font sizes

## 📧 Contact Information

**Hope Foundation**
- Email: info@hopefoundation.org
- Phone: +1 (555) 123-4567
- Address: 123 Charity Street, Hope City, HC 12345
- Hours: Mon - Fri: 9:00 AM - 6:00 PM

## 📝 Project Information

- **Student**: Akriti
- **Registration**: 167855
- **Roll Number**: 289
- **Centre**: NIELIT, Shimla
- **Session**: 2025-26

---

**Happy Fundraising! 🎉**

For more information, refer to README.md or the PDF documentation.

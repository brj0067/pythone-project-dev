# Very Simple Python DevOps Demo

This is a tiny Python web service you can use to practice DevOps basics:

- Creating and activating a virtual environment
- Installing dependencies
- Running tests
- Building and running a Docker container

## 1. Run locally (no Docker)

```bash
python -m venv .venv
.\.venv\Scripts\activate  # on Windows

pip install -r requirements.txt

set PORT=8000            # PowerShell: $env:PORT=8000
set APP_NAME=devops-demo-app  # PowerShell: $env:APP_NAME="devops-demo-app"

python app.py
```

Then open:

- `http://localhost:8000/` – main endpoint
- `http://localhost:8000/health` – health check

## 2. Run tests

```bash
pytest
```

## 3. Build and run with Docker

```bash
docker build -t devops-demo-app .

docker run -p 8000:8000 devops-demo-app
```

You can override environment variables:

```bash
docker run -p 8000:8000 -e PORT=8000 -e APP_NAME="my-devops-app" devops-demo-app
```

# Professional Portfolio Website - Brahma Raj Joshi

A modern, responsive portfolio website showcasing professional experience, skills, certifications, and contact information.

## Features

- **Modern Design**: Clean, professional design with smooth animations
- **Fully Responsive**: Works seamlessly on desktop, tablet, and mobile devices
- **Smooth Scrolling**: Enhanced navigation with smooth scroll effects
- **Interactive Elements**: Hover effects, animations, and dynamic navigation
- **SEO Friendly**: Proper meta tags and semantic HTML structure
- **Fast Loading**: Optimized CSS and JavaScript for quick page loads

## Sections

1. **Hero Section**: Eye-catching introduction with call-to-action buttons
2. **About**: Professional summary and background
3. **Experience**: Timeline of work experience
4. **Education**: Academic qualifications
5. **Certifications**: Professional certifications
6. **Skills**: Technical skills organized by category
7. **Contact**: Contact information and social links

## Technologies Used

- HTML5
- CSS3 (with CSS Variables for theming)
- Vanilla JavaScript (no dependencies)
- Font Awesome Icons
- Google Fonts (Inter)

## Getting Started

### Option 1: Direct Opening
Simply open `index.html` in your web browser. No server required for basic functionality.

### Option 2: Local Server (Recommended)
For the best experience, use a local server:

```bash
# Using Python 3
python -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js (if you have http-server installed)
npx http-server

# Using PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

### Option 3: Deploy Online
You can deploy this website to:
- **GitHub Pages**: Free hosting for static sites
- **Netlify**: Drag and drop deployment
- **Vercel**: Fast deployment with Git integration
- **Azure Static Web Apps**: Perfect for Azure professionals
- Any static hosting service

## Customization

### Colors
Edit the CSS variables in `styles.css`:

```css
:root {
    --primary-color: #0078d4;      /* Main brand color */
    --secondary-color: #106ebe;    /* Secondary color */
    --accent-color: #00bcf2;       /* Accent color */
    /* ... other colors */
}
```

### Content
- Update personal information in `index.html`
- Modify sections as needed
- Add or remove experience/education entries
- Update skills and certifications

### Styling
- All styles are in `styles.css`
- Responsive breakpoints: 768px (tablet), 480px (mobile)
- Easy to customize fonts, spacing, and colors

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## File Structure

```
portfolio-website/
│
├── index.html          # Main HTML file
├── styles.css          # All styles and responsive design
├── script.js           # JavaScript for interactivity
└── README.md          # This file
```

## Performance

- No external JavaScript libraries (lightweight)
- Optimized CSS with efficient selectors
- Minimal HTTP requests
- Fast page load times

## Future Enhancements

Potential additions:
- Contact form with backend integration
- Blog section
- Project portfolio showcase
- Dark mode toggle
- Multi-language support
- Analytics integration

## License

This portfolio template is free to use and modify for personal and commercial projects.

## Contact

**Brahma Raj Joshi**
- Email: brahmraj128@gmail.com
- Phone: +977 9865816031
- LinkedIn: [linkedin.com/in/brahma-raj-joshi](https://www.linkedin.com/in/brahma-raj-joshi)
- Location: Kathmandu, Bāgmatī, Nepal

---

Built with ❤️ for showcasing professional expertise in Azure, Microsoft Intune, and Cloud Security.

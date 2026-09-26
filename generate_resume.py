import subprocess
import os

def generate():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Aayush Patel - Resume</title>
<style>
  @page {
    size: A4 portrait;
    margin: 18mm 18mm 18mm 18mm;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #111;
    background: #fff;
    line-height: 1.42;
    font-size: 10.5pt;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .header {
    margin-bottom: 16px;
  }
  h1 {
    font-size: 22pt;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: #000;
    margin-bottom: 4px;
  }
  .contact-line {
    font-size: 9.5pt;
    color: #222;
  }
  .contact-line a {
    color: inherit;
    text-decoration: none;
  }
  .section {
    margin-bottom: 14px;
  }
  .section-title {
    font-size: 10pt;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: #000;
    margin-bottom: 5px;
  }
  p {
    margin-bottom: 5px;
    font-size: 9.8pt;
    color: #1a1a1a;
  }
  .project-block {
    margin-bottom: 10px;
  }
  .project-title {
    font-size: 10.2pt;
    font-weight: 700;
    color: #000;
  }
  .project-subtitle {
    font-size: 9.5pt;
    font-style: italic;
    color: #333;
    margin-bottom: 1px;
  }
  .project-tech {
    font-size: 9.2pt;
    color: #444;
    margin-bottom: 3px;
  }
  .project-link {
    font-size: 9.2pt;
    color: #444;
    margin-bottom: 3px;
  }
  .project-link a {
    color: inherit;
    text-decoration: none;
  }
  ul {
    list-style-type: disc;
    margin-left: 18px;
    margin-top: 2px;
    margin-bottom: 4px;
  }
  li {
    font-size: 9.5pt;
    color: #1a1a1a;
    margin-bottom: 3px;
    line-height: 1.38;
  }
  .skills-label {
    font-size: 9.8pt;
    font-weight: 600;
    color: #111;
    margin-bottom: 2px;
  }
  .skills-list {
    font-size: 9.5pt;
    color: #222;
  }
</style>
</head>
<body>

<div class="header">
  <h1>Aayush Patel</h1>
  <div class="contact-line">
    Mumbai, Maharashtra &nbsp;|&nbsp; <a href="mailto:agpatel01122007@gmail.com">agpatel01122007@gmail.com</a> &nbsp;|&nbsp; <a href="tel:+918104959628">+91 8104959628</a> &nbsp;|&nbsp; <a href="https://github.com/aayush-debug" target="_blank">github.com/aayush-debug</a>
  </div>
</div>

<div class="section">
  <div class="section-title">SUMMARY</div>
  <p>
    Second-year Computer Engineering student (B.Tech, University of Mumbai, expected 2029) with a strong self-directed builder track record across full-stack, data, and AI-integrated projects. Comfortable moving fast from idea to working prototype, with growing interest in entrepreneurship and product building. Currently seeking internships and co-founder opportunities.
  </p>
</div>

<div class="section">
  <div class="section-title">EDUCATION</div>
  <p>
    <strong>B.Tech in Computer Engineering</strong> &mdash; Mumbai, Maharashtra &mdash; Second year
  </p>
</div>

<div class="section">
  <div class="section-title">PROJECTS</div>

  <div class="project-block">
    <div class="project-title">MarineTrace</div>
    <div class="project-subtitle">Satellite-Based Oil Spill Detection &amp; Vessel Attribution</div>
    <div class="project-tech">React, TypeScript, Python, FastAPI, U-Net, ResNet-34, AIS, Docker</div>
    <ul>
      <li>Built an end-to-end SAR satellite oil-spill detection and vessel-attribution pipeline using Sentinel-1 imagery, ML segmentation, AIS data, and geospatial analysis.</li>
      <li>Developed a U-Net + ResNet-34 model for slick segmentation and implemented vessel attribution using spatial, temporal, trajectory, and behavioral factors.</li>
      <li>Created a React/TypeScript GIS frontend and FastAPI backend with drift analysis, vessel search, investigation, and detection APIs; containerized with Docker.</li>
    </ul>
  </div>

  <div class="project-block">
    <div class="project-title">Monte Carlo Wealth Simulator</div>
    <div class="project-link"><a href="https://github.com/aayush-debug/Monte-Carlo-Wealth-Simulator" target="_blank">github.com/aayush-debug/Monte-Carlo-Wealth-Simulator</a></div>
    <ul>
      <li>Built in Python (Streamlit, Geometric Brownian Motion) with KPI cards, dark-themed Matplotlib charts, and a summary statistics table.</li>
    </ul>
  </div>

  <div class="project-block">
    <div class="project-title">BottleBuzz</div>
    <div class="project-link"><a href="https://github.com/aayush-debug/BottleBuzz" target="_blank">github.com/aayush-debug/BottleBuzz</a></div>
    <ul>
      <li>TypeScript project.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">CURRENTLY BUILDING</div>

  <div class="project-block">
    <div class="project-title">Pitch Connect <span style="font-weight: normal; font-size: 9.5pt; color: #444;">(formerly LetsPitch)</span></div>
    <ul>
      <li>Startup-investor matchmaking platform with curated deal flow, AI-generated startup summaries, and a founder credibility score; built on Next.js/Supabase/Razorpay.</li>
    </ul>
  </div>

  <div class="project-block" style="margin-bottom: 4px;">
    <div class="project-title">JARVIS-style AI Voice Assistant</div>
    <p style="margin-top: 2px;">
      Browser-based assistant using the Web Speech API and Claude API with a sci-fi, character-consistent persona.
    </p>
  </div>
</div>

<div class="section">
  <div class="section-title">SKILLS</div>
  <div class="skills-label">Technical Skills</div>
  <div class="skills-list">
    Python, Java, C, FastAPI, Automation &amp; RAG, Vibe Coding, Software as a Service (SaaS)
  </div>
</div>

</body>
</html>"""
    
    html_path = "resume_source.html"
    with open(html_path, "w") as f:
        f.write(html_content)
    
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    subprocess.run([
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--print-to-pdf=resume.pdf",
        html_path
    ], check=True)
    print("Successfully generated resume.pdf")

if __name__ == "__main__":
    generate()

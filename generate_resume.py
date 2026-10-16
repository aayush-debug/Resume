import os
import shutil
import subprocess
import sys

def find_chrome():
    """Locate Google Chrome or Chromium executable."""
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chrome"),
        os.environ.get("CHROME_PATH"),
    ]
    for path in candidates:
        if path and os.path.exists(path) and os.access(path, os.X_OK):
            return path
    return None

def generate(source_html="index.html", output_pdf="resume.pdf", sync_source=True):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(base_dir, source_html)
    output_path = os.path.join(base_dir, output_pdf)
    sync_path = os.path.join(base_dir, "resume_source.html")

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source HTML file not found: {source_path}")

    # Read content from index.html
    with open(source_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Sync resume_source.html
    if sync_source and source_path != sync_path:
        with open(sync_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Synced {source_html} -> resume_source.html")

    chrome_path = find_chrome()
    if not chrome_path:
        raise RuntimeError("Google Chrome or Chromium executable could not be found.")

    print(f"Using Chrome binary: {chrome_path}")
    print(f"Generating {output_pdf} from {source_html}...")

    # Run Chrome in headless mode with flags to ensure web fonts render before PDF capture
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=2000",
        f"--print-to-pdf={output_path}",
        f"file://{source_path}"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Chrome error output:\n{result.stderr}", file=sys.stderr)
        raise RuntimeError(f"Chrome failed with exit code {result.returncode}")

    if os.path.exists(output_path):
        size_kb = os.path.getsize(output_path) / 1024
        print(f"Successfully generated {output_pdf} ({size_kb:.1f} KB)")
    else:
        raise RuntimeError(f"Output PDF {output_pdf} was not created.")

if __name__ == "__main__":
    generate()

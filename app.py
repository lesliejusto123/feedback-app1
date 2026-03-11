from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feedback Hub</title>
    <style>
        :root { --primary: #2563eb; --bg: #f8fafc; --text: #1e293b; }
        body { font-family: sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 20px; }
        .container { max-width: 450px; margin: 0 auto; background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        textarea { width: 100%; padding: 12px; border: 1px solid #e2e8f0; border-radius: 8px; box-sizing: border-box; }
        button { background: var(--primary); color: white; border: none; padding: 12px; border-radius: 8px; width: 100%; cursor: pointer; font-weight: bold; margin-top: 10px; }
        
        /* Hacker Modal Prank */
        #hackerModal { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); display: flex; align-items: center; justify-content: center; z-index: 1000; }
        .modal-content { background: #000; color: #0f0; border: 2px solid #0f0; padding: 30px; text-align: center; font-family: monospace; box-shadow: 0 0 20px #0f0; }
        .entry { background: #f1f5f9; padding: 10px; border-radius: 6px; margin-bottom: 8px; font-size: 14px; }
    </style>
</head>
<body>
    <div id="hackerModal">
        <div class="modal-content">
            <h2 style="color: red;">WARNING!</h2>
            <p>Your phone is hack click button</p>
            <p style="font-size: 11px; color: #888;">Inside by: rjay justo</p>
            <button onclick="document.getElementById('hackerModal').style.display='none'" style="background: #0f0; color: #000; width: auto; padding: 8px 30px; cursor: pointer;">OK</button>
        </div>
    </div>

    <div class="container">
        <h2 style="color: var(--primary);">Submit Feedback</h2>
        <form method="POST" action="/submit">
            <textarea name="comment" rows="4" placeholder="Enter your message here..." required></textarea>
            <button type="submit">Send Feedback</button>
        </form>
        <div style="margin-top: 20px;">
            <h3>Submissions:</h3>
            {% for line in entries %}
                <div class="entry">{{ line }}</div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    entries = []
    if os.path.exists('feedback.txt'):
        with open('feedback.txt', 'r') as f:
            entries = f.readlines()[::-1]
    return render_template_string(HTML_PAGE, entries=entries)

@app.route('/submit', methods=['POST'])
def submit():
    comment = request.form.get('comment')
    if comment:
        with open('feedback.txt', 'a') as f:
            f.write(comment.strip() + '\\n')
    return '<script>alert("Sent!"); window.location.href="/";</script>'

if __name__ == '__main__':
    # This allows Render to set the port automatically
    port = int(os.environ.get("PORT", 5000))

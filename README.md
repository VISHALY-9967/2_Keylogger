A keylogger is a monitoring tool that records every keystroke made on a keyboard, often used for surveillance, diagnostics, or malicious data theft.

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">

</head>
<body>

  <h1>🛡️ Python Keylogger GUI</h1>
  <p class="tagline">
    A simple, educational <strong>Python keylogger</strong> built with <code>pynput</code> and <code>tkinter</code>. This app tracks keystrokes and logs them in both <code>.txt</code> and <code>.json</code> formats — complete with a <strong>user-friendly GUI</strong>.
  </p>

  <div class="note">
    ⚠️ <strong>Disclaimer:</strong> This project is for educational purposes only. Using this software unethically or for malicious purposes is strictly prohibited and illegal.
  </div>

  <div class="section">
    <h2>🔍 Project Overview</h2>
    <ul>
      <li>✅ Keylogging with <code>pynput</code></li>
      <li>✅ Real-time log display in GUI</li>
      <li>✅ Saves logs to <code>logs.txt</code> and <code>logs.json</code></li>
      <li>✅ Start/Stop control buttons</li>
      <li>✅ Scrollable console view</li>
    </ul>
  </div>

  <div class="section">
    <h2>🧰 Requirements</h2>
    <p>Install Python dependencies:</p>
    <pre><code>pip install pynput</code></pre>
    <p><code>tkinter</code> is pre-installed in most Python setups.</p>
  </div>

  <div class="section">
    <h2>🚀 How to Run</h2>

      Run the script:
      python keylogger.py
    
  </div>

  <div class="section">
    <h2>🖼️ GUI Preview (Text Representation)</h2>
    <pre>
 --------------------------------------
| 🔐 Keylogger GUI                    |
|--------------------------------------|
| ▶️ Start       ⏹️ Stop              |
| [*] Ready to start keylogger.        |
| a                                    |
| b                                    |
| Key.space (released)                 |
| ...                                  |
| [ Exit ]                             |
 --------------------------------------
    </pre>
  </div>

  <div class="section">
    <h2>📂 Files Generated</h2>
    <table>
      <thead>
        <tr><th>File Name</th><th>Description</th></tr>
      </thead>
      <tbody>
        <tr><td><code>logs.txt</code></td><td>Plain text keystroke log</td></tr>
        <tr><td><code>logs.json</code></td><td>Structured JSON log</td></tr>
      </tbody>
    </table>
  </div>

  <div class="section">
    <h2>🧠 How It Works</h2>
    <ul>
      <li>Listens to key <code>on_press</code> and <code>on_release</code> events</li>
      <li>Updates GUI live with current keys</li>
      <li>Writes each key to both <code>.txt</code> and <code>.json</code></li>
    </ul>
  </div>

  <div class="section">
    <h2>🧪 Use Cases</h2>
    <ul>
      <li>📚 Educational demo for keylogging</li>
      <li>🖥️ Learn GUI development with tkinter</li>
      <li>🔒 Foundation for secure input tracking</li>
    </ul>
  </div>

  <div class="section">
    <h2>📌 Future Enhancements</h2>
    <ul>
      <li>⏱️ Add timestamp support</li>
      <li>🔐 Encrypt stored logs</li>
      <li>🔒 Password protection for access</li>
      <li>📦 Convert into executable (.exe)</li>
    </ul>
  </div>

  <div class="section">
    <h2>🤝 Contributing</h2>
    <p>Fork the project, improve it, and open a pull request. Your contributions are welcome!</p>
  </div>

  <div class="section">
    <h2>⭐ Like This Project?</h2>
    <ul>
      <li>🌟 Star the repo</li>
      <li>🍴 Fork it and customize</li>
      <li>📣 Share it with fellow Python learners</li>
    </ul>
    <p>Happy Learning! 🙌</p>
  </div>

</body>
</html>


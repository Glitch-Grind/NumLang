#!/usr/bin/env python
"""
NumLang Standalone App Launcher
Starts the Flask server and opens the IDE in the default browser
"""

import sys
import os
import time
import webbrowser
import threading
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the Flask app from server.py
from server import app

def open_browser():
    """Open the IDE in the default browser after a short delay"""
    time.sleep(2)  # Wait for server to start
    webbrowser.open('http://localhost:5000')

def main():
    """Start the NumLang IDE"""
    print("=" * 60)
    print("NumLang v1.2 IDE")
    print("=" * 60)
    print("\nStarting server on http://localhost:5000")
    print("Opening IDE in your default browser...")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 60 + "\n")
    
    # Start browser opening in a background thread
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    # Start the Flask server
    try:
        app.run(host='localhost', port=5000, debug=False)
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        sys.exit(0)

if __name__ == '__main__':
    main()

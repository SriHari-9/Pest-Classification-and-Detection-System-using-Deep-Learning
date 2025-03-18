# main.py

from user.user import app

if __name__ == '__main__':
    import os
    port = int(os.getenv('PORT', 5000))  # ✅ Use Render’s PORT
    app.run(host='0.0.0.0', port=port, debug=True)

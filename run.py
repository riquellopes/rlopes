import os
import sys
from app import app, freezer

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "freezer":
        freezer.freeze()
    else:
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)

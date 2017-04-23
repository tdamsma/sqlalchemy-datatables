"""Flask tutorial views."""
from flask_app import app
import views  # noqa

if __name__ == "__main__":
    app.run('0.0.0.0', port=5678, debug=True)


# Run Server
from router import app
from flask_cors import CORS




if __name__ == "__main__":
          CORS(app)
          app.run(debug=True)
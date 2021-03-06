from app import app, db #import our Flask app
import models
import views

#registering blueprint
from entries.blueprint import entries 
app.register_blueprint(entries, url_prefix='/entries')

if __name__ == '__main__':
    app.run()
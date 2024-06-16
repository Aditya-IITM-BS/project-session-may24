from flask import render_template_string

def create_views(app):

    # homepage
    @app.route('/')
    def home():
        return render_template_string(
            """
                <h1> this is home</h1>
    
            """
        )
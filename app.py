from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Landing Page</title>
        </head>
        <body>
            <h1>Welcome to My FastAPI App!</h1>
            <p>This is a simple landing page.</p>
            <p>This is a semantic release<p>
        </body>
    </html>
    """


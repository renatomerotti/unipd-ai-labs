import math

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models import INITIAL, headline, history

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {})


def economy_context(error: str | None = None) -> dict:
    return {
        "history": history,
        "headline": headline,
        "current": history[-1],
        "previous": history[-2],
        "current_headline": headline(history[-1]),
        "previous_headline": headline(history[-2]),
        "term_start_population": INITIAL[-1].population,
        "error": error,
    }


@app.get("/economy", response_class=HTMLResponse)
def economy(request: Request):
    return templates.TemplateResponse(request, "economy.html", economy_context())


@app.exception_handler(404)
def not_built(request: Request, exc):
    return templates.TemplateResponse(request, "not_built.html", {}, status_code=404)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8001, reload=True)

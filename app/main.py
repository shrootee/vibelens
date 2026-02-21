from fastapi import FastAPI, UploadFile, File , Request
from fastapi.staticfiles import StaticFiles
from PIL import Image
from app.vision import generate_description   # IMPORTANT import
from fastapi.responses import FileResponse
from app.caption import generate_smart_caption
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Route to handle image upload
@app.post("/caption")
async def caption_route(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")

    description = generate_description(image)

    smart_caption = generate_smart_caption(description)

    return {"description": smart_caption}

@app.get("/")
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
from io import BytesIO

import qrcode
from PIL import Image, ImageDraw, ImageFont
from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse

app = FastAPI()

app.add_middleware(

    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://zos-g.vercel.app",
        "https://zos-qczu6ekj2-zodiucs-projects.vercel.app",
        "https://zosg.zosiuc.dev"
    ],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "QR Code API is running"}


@app.post("/generate-qr/")
async def generate_qr(data: str = Form(...), logo: UploadFile = None):
    print("QR request ontvangen")
    try:
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="#46545f", back_color="#F4F4F4").convert("RGB")

        # Padding voor ondertekst
        padding_bottom = 30

        # Canvas vergroten voor padding
        new_img = Image.new("RGB", (qr_img.size[0], qr_img.size[1] + padding_bottom), "#F4F4F4")
        new_img.paste(qr_img, (0, 0))

        if logo:
            contents = await logo.read()
            logo_img = Image.open(BytesIO(contents)).convert("RGBA")
            size = int(new_img.size[0] * 0.20)

            scale = 1
            logo_inner_size = int(size * scale)

            logo_img = logo_img.resize((logo_inner_size, logo_inner_size))
            # Maak een witte achtergrond
            white_bg = Image.new("RGBA", logo_img.size, (244, 244, 244, 100))  # volledig zichtbaar

            # Plak het logo op de witte achtergrond, gebruik de alpha (transparantie) als masker
            white_logo = Image.alpha_composite(white_bg, logo_img)

            # Stap 4: maak witte vierkante achtergrond van formaat `size x size`
            padded_logo = Image.new("RGBA", (size, size), (244, 244, 244, 244))

            # Stap 5: plak logo gecentreerd op witte achtergrond
            offset = ((size - logo_inner_size) // 2, (size - logo_inner_size) // 2)
            padded_logo.paste(white_logo, offset, mask=logo_img)

            mask = Image.new("L", (size, size), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, size, size), fill=255)

            # Witte achtergrond voor leesbaarheid
            circle_bg = Image.new("RGBA", (size, size), "#F4F4F4")
            circle_bg.paste(padded_logo, (0, 0), mask=mask)

            pos = ((new_img.size[0] - size) // 2, (new_img.size[1] - size) // 2)
            new_img.paste(circle_bg, pos, mask=mask)

        # Watermerk toevoegen
        draw = ImageDraw.Draw(new_img)
        try:
            font = ImageFont.truetype("Times New Roman", 22)
        except IOError:
            font = ImageFont.load_default()

        text = "zosiuc.dev"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        pos = ((qr_img.size[0] - text_width) // 2, qr_img.size[1] + (padding_bottom - (text_height+30)) // 2)

        draw.text(pos, text, font=font, fill="#46545f")

        filename = f"qr_zosG.png"

        new_img.save(filename)

        respons = FileResponse(filename, media_type="image/png", filename="qr-code.png")
        respons.headers["Access-Control-Allow-Origin"] = "https://zos-g.vercel.app"
        return respons
    except Exception as e:
        print(e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

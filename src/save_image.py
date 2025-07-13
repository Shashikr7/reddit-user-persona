from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def save_persona_image(persona_text, username):
    width, height = 1000, 1400
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Font setup
    font_path = "arial.ttf"  # Windows default
    if not os.path.exists(font_path):
        font_path = "C:/Windows/Fonts/arial.ttf"  # fallback for Windows
    try:
        title_font = ImageFont.truetype(font_path, 36)
        text_font = ImageFont.truetype(font_path, 20)
    except:
        print("❌ Could not load font. Make sure Arial is available.")
        return

    # Title
    draw.text((30, 20), f"Reddit User Persona: {username}", fill="black", font=title_font)

    # Word wrap and draw persona text
    lines = textwrap.wrap(persona_text, width=90)
    y_text = 100
    for line in lines:
        draw.text((30, y_text), line, font=text_font, fill="black")
        y_text += 30

    # Save image
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    image_path = os.path.join(output_dir, f"{username}.png")
    image.save(image_path)
    print(f"🖼️ Persona image saved at {image_path}")

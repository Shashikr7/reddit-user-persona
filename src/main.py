from src.scraper import fetch_user_data
from src.persona_builder import build_persona
from src.utils import extract_username, save_to_file

if __name__ == "__main__":
    url = input("Enter Reddit profile URL: ").strip()
    username = extract_username(url)

    if username:
        posts, comments = fetch_user_data(username)
        persona = build_persona(posts, comments)
        save_to_file(username, persona)
        print(f"✅ Persona saved to output/{username}.txt")
    else:
        print("❌ Invalid Reddit URL.")


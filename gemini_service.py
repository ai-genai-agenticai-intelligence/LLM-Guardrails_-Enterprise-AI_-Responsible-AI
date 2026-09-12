# pyrefly: ignore [missing-import]
from google import genai
from config import(
    GEMINI_API_KEY,
    GEMINI_MODEL,
)


client  = genai.Client(
    api_key = GEMINI_API_KEY
)


def generate_response(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )
        return response.text or ""
    except Exception as e:
        return f"Error communicating with Gemini: {str(e)}"


if __name__ == "__main__":
    print(generate_response("Give me weather report"))


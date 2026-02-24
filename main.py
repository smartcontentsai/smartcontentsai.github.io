import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS կարգավորում
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- ՔՈ ՏՎՅԱԼՆԵՐԸ ---
GROQ_API_KEY = "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".strip()
TELEGRAM_TOKEN = "8221855314:AAF0_IOSpZaHamW_YUr3n5QYXV_iXVWt1nQ"
MY_CHAT_ID = "8221855314"

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        # Llama 3 API (Groq) հասցեն
        url = "https://api.groq.com/openai/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama-3.3-70b-versatile", 
            "messages": [
                {
                    "role": "system", 
                    "content": "Դու Smart Content AI ընկերության պրոֆեսիոնալ օգնականն ես:"
                    " Խոսիր միայն հայերեն: սկզբում ներկայացիր որպես SmartContentAI օգնական եթե քեզ հարցնեն թե ով է քեզ ստեղծել"
                    "Մենք զբաղվում ենք AI Չաթբոտերի ստեղծմամբ AI ռիլսերի ստեղծմամբ, և WEB կայքերի ստեղծմամբ"
                    "մենք ունենք ինստագրամյան էջ smartcontent_ai"
                    "եղիր հաճախորդի հետ բարեհամբյուր և պատասխանիր հարցերին"
                    "ստանդարտ փաթեթի արժեքը 40-80.000 դրամ է ամսական սպասարկման վճար 10,000դրամ կախված բարդությունից, ներառում է 1  AI CHATBOT"
                    "Բիզնես փաթեթ AI Չաթ բոտ, 5 AI Հոլովակներ, 1 վեբ կայք(landing) արժեքը 180․000դրամ, ամսակա սպասարկման վճարը 20,000դրամ"
                    "էքսպերտ փաթեթը ներառում է 2 AI չաթ բոտ, 1 վեբ կայք, 1 ամիս անվճար սպասարկում, արժեքը 300,000 դրամ"
                    

                },
                {
                    "role": "user", 
                    "content": req.message
                }
            ],
            "temperature": 0.7 # Պատասխանի ստեղծագործական աստիճանը
        }
        
        response = requests.post(url, json=payload, headers=headers)
        res_data = response.json()

        # Ստուգում ենք պատասխանը (Llama-ն օգտագործում է OpenAI-ի ֆորմատը)
        if "choices" in res_data:
            bot_reply = res_data["choices"][0]["message"]["content"]
        elif "error" in res_data:
            bot_reply = f"Llama Error: {res_data['error']['message']}"
        else:
            bot_reply = "Չկարողացա կապ հաստատել "

        # Telegram-ի հատված (նույնն է մնում)
        if any(char.isdigit() for char in req.message) and len(req.message) > 7:
            tg_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            requests.post(tg_url, json={
                "chat_id": MY_CHAT_ID, 
                "text": f"🚀 Նոր հայտ Llama-ից!\n💬 Հաճախորդ: {req.message}"
            })

        return {"reply": bot_reply}

    except Exception as e:
        return {"reply": f"Համակարգային սխալ: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
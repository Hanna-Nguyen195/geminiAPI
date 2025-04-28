from google import genai
from vertexai.generative_models import GenerationConfig


class TeacherBot:
    def __init__(self, api_key: str):
        # genai.configure(api_key=api_key)
        # self.model = genai.GenerativeModel('gemini-1.5-pro')
        self.client = genai.Client(api_key="AIzaSyCt4XAe9FaGohl1xVD6vgb6fZmbxo7_qwQ")
        # response = client.models.generate_content(
        #     model="gemini-2.0-flash",
        #     contents="Explain how AI works in a few words",
        # )
    def answer_question(self, question: str, language: str) -> str:
       
        context = (
            f"Bạn hãy đóng vai giáo viên chuyên nghiệp, trả lời ngắn gọn nhất có thể bằng ngôn ngữ '{language}'. "
            f"Dưới đây là câu hỏi:\n\n{question}"
        )
  
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=context,

        )
        return response.text.strip()

if __name__ == "__main__":
    key="AIzaSyCt4XAe9FaGohl1xVD6vgb6fZmbxo7_qwQ"
    bot = TeacherBot(api_key=key)
    question = input("Write question: ")
    language = input("Write language, eg: en,vi, zh, ja, ko, fr, de, es, it, ru, pt, ar:" )
    # question = "Tại sao bầu trời có màu xanh?"
    # language = "vi"
    answer = bot.answer_question(question, language)
    print("Câu trả lời:", answer)

    



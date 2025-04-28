
import google.generativeai as genai

class TeacherBot:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def answer_question(self, question: str, language: str) -> str:
       
        prompt = (
            f"Bạn hãy đóng vai giáo viên chuyên nghiệp, trả lời ngắn gọn bằng ngôn ngữ '{language}'. "
            f"Dưới đây là câu hỏi:\n\n{question}"
        )
        response = self.model.generate_content(prompt)
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

    

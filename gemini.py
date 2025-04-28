import google.generativeai as genai


genai.configure(api_key="AIzaSyCt4XAe9FaGohl1xVD6vgb6fZmbxo7_qwQ")

model = genai.GenerativeModel('gemini-1.5-pro')


def ask_teacher(question: str) -> str:
    prompt = f"Bạn hãy đóng vai một giáo viên chuyên nghiệp và trả lời ngắn gọn, dễ hiểu cho câu hỏi sau:\n\n{question}"
    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    user_question = input("Nhập câu hỏi: ")
    answer = ask_teacher(user_question)
    print("\nCâu trả lời của giáo viên:")
    print(answer)
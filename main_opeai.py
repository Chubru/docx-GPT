import datetime
import time

import openai

from DocxProcessor import DocxProcessor

from chatgpt_wrapper.backends.browser.chatgpt import ChatGPT
from chatgpt_wrapper.core.config import Config

openai.api_key = "sk-____API____KEY_____"
model_engine = "text-davinci-003"


def handle_error_and_retry():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    error_message = f"Error occurred at {current_time}"
    print(error_message)
    time.sleep(10)


def chatgpt_callback(requests, model_engine=None):
    processed_text = ""
    while True:
        try:
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=requests,
                max_tokens=3000,
                n=1,
                stop=None,
                temperature=0.6)
            break
        except Exception as e:
            handle_error_and_retry()


    return completion.choices[0].text


def main():
    prompt = "Представь себе, что ты переводчик. Я буду давать текст, твоя задача переводить учитывая контекст и не сообщая никаких дополнительных сведений в том числе исходного сообщения. В случае если ты встретил аббревиатуру то ты должен оставить ее в исходном виде, не переводя ее.  <> для разметки, сохраняй их. Текст:'"
    docx_processor = DocxProcessor(prompt=prompt, max_message_size=2000)
    docx_processor.process("input.docx", "output.docx", chatgpt_callback)


if __name__ == "__main__":
    main()

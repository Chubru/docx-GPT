import datetime
import time

from DocxProcessor import DocxProcessor

from chatgpt_wrapper.backends.browser.chatgpt import BrowserBackend
from chatgpt_wrapper.core.config import Config


def initialize_chatgpt():
    global bot
    if 'bot' in globals():
        bot._shutdown()

    config = Config()
    config.set("backend", "chatgpt-browser")
    # config.set('chat.model', 'gpt4')
    bot = BrowserBackend(config)
    bot.launch_browser()


def handle_error_and_retry():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    error_message = f"Error occurred at {current_time}"
    print(error_message)
    time.sleep(10)
    initialize_chatgpt()


def chatgpt_callback(requests):
    success = False
    processed_text = ""
    while not success:
        success, processed_text, message = bot.ask(requests)
        if not success or processed_text == '':
            handle_error_and_retry()
            success = False

    return processed_text


def main():
    initialize_chatgpt()
    prompt = "Представь себе, что ты переводчик. Я буду давать текст, твоя задача переводить учитывая контекст и не сообщая никаких дополнительных сведений в том числе исходного сообщения. В случае если ты встретил аббревиатуру то ты должен оставить ее в исходном виде, не переводя ее.  <> для разметки, сохраняй их. Текст:'"
    docx_processor = DocxProcessor(prompt=prompt, max_message_size=2000)
    docx_processor.process("input.docx", "output.docx", chatgpt_callback)


if __name__ == "__main__":
    main()

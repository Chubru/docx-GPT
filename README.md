# Docx-GPT

Данный проект позволяет последовательно обрабатывать файлы формата docx с использованием ChatGPT. В ChatGPT передаются сразу несколько параграфов, что позволяет качественно улучшить результат обработки.

## Зависимости

- python-docx: `pip install python-docx`

Опционально:

- chatgpt-wrapper: `pip install git+https://github.com/mmabrouk/chatgpt-wrapper`
- openai: `pip install openai`

## Библиотеки для работы с ChatGPT

- ChatGPT Wrapper: https://github.com/mmabrouk/chatgpt-wrapper
- OpenAI Python: https://github.com/openai/openai-python

ChatGPT Wrapper позволяет эмулировать работу с ChatGPT через браузер, поэтому доступна ChatGPT 3.5 и ChatGPT 4 (требуется ChatGPT Plus).

OpenAI Python требует API ключи, но все знают где их взять бесплатно. ChatGPT 4 на практике будет доступна только платным аккаунтам.

## Использование

1. Установите зависимости.
2. Выберите библиотеку для работы с ChatGPT (chatgpt-wrapper или openai-python) и модифицируйте соответствующий main файл.
3. Если используете openai-python, укажите свой API ключ.
4. Запустите соответствующий main файл.


-----
PS

Для работы GPT с формулами лучше использовать LaTeX


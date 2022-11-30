# active_learn
Implementation of a telegram chat-bot for question-answering. The chatbot is powered by a finetuned transformer-based (BERT) model which allows to understand the context of a given piece of text and of a question. The model then composes an answer to the given question based on the text provided.

Input telebot token into `TELEBOT_TOKEN` variable in `main.py`.

BERT model was finetuned using question-answers generated from question_generation library. The library is inference only.
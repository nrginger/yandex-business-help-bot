import os
import logging
import requests
import telebot
import numpy as np
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from sentence_transformers import SentenceTransformer

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Загрузка переменных окружения
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CAILA_TOKEN = os.getenv('CAILA_TOKEN')

# Инициализация бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)


def get_answer_from_caila(question, context):
    headers = {
        "Authorization": f"Bearer {CAILA_TOKEN}",
        "MLP-API-KEY": CAILA_TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "chat": {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system",
                 "content": f"Ты - помощник по Яндекс Бизнесу. Используй следующий контекст для ответа на вопросы: {context}"},
                {"role": "user", "content": question}
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }
    }

    try:
        response = requests.post(
            "https://caila.io/api/mlpgate/account/just-ai/model/openai-proxy/predict",
            headers=headers,
            json=payload
        )
        response.raise_for_status()

        response_data = response.json()
        logging.info(f"Ответ от CAILA: {response_data}")

        # Изменяем извлечение ответа в соответствии с новой структурой
        if ('chat' in response_data and
                'choices' in response_data['chat'] and
                len(response_data['chat']['choices']) > 0 and
                'message' in response_data['chat']['choices'][0]):
            return response_data['chat']['choices'][0]['message']['content']
        else:
            logging.error(f"Неожиданная структура ответа: {response_data}")
            return "Извините, произошла ошибка при обработке ответа. Пожалуйста, попробуйте позже."

    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка HTTP запроса: {e}")
        return "Извините, произошла ошибка при получении ответа. Пожалуйста, попробуйте позже."
    except Exception as e:
        logging.error(f"Непредвиденная ошибка: {e}")
        return "Извините, произошла непредвиденная ошибка. Пожалуйста, попробуйте позже."
    

class DocumentStore:
    def __init__(self):
        self._documents = []
        self._embeddings = None
        self.model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

    def add_documents(self, documents):
        if not documents:
            return
        self._documents = documents
        self._embeddings = self.model.encode(documents, show_progress_bar=True)

    def search(self, query, k=3):
        if not self._documents or self._embeddings is None:
            return []

        query_embedding = self.model.encode([query])[0]
        similarities = np.dot(self._embeddings, query_embedding) / (
                np.linalg.norm(self._embeddings, axis=1) * np.linalg.norm(query_embedding)
        )

        top_k_indices = np.argsort(similarities)[-k:][::-1]
        threshold = 0.3
        relevant_docs = [
            self._documents[i]
            for i in top_k_indices
            if similarities[i] > threshold
        ]

        return relevant_docs


def load_docs():
    documents = []
    docs_dir = './docs'

    logging.info("Загрузка документов...")
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        documents.append(content)
                except Exception as e:
                    logging.error(f"Ошибка при загрузке файла {file_path}: {e}")

    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separator="\n"
    )
    texts = text_splitter.split_text("\n".join(documents))
    logging.info(f"Документы разделены на {len(texts)} частей")

    doc_store = DocumentStore()
    doc_store.add_documents(texts)
    return doc_store


# Инициализация хранилища документов
logging.info("Инициализация хранилища документов...")
doc_store = load_docs()
logging.info("Бот готов к работе!")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет! Я бот-помощник по Яндекс Бизнесу. Задайте мне вопрос, и я постараюсь найти ответ в документации."
    )

    @bot.message_handler(func=lambda message: True)
    def answer_question(message):
        try:
            processing_msg = bot.reply_to(message, "Обрабатываю ваш запрос...")

            relevant_docs = doc_store.search(message.text, k=2)  # Уменьшаем количество документов
            if relevant_docs:
                max_context_length = 1500  # Уменьшаем максимальную длину контекста
                context = "\n\n".join(relevant_docs)
                if len(context) > max_context_length:
                    context = context[:max_context_length] + '...'
                logging.info(f"Сформированный контекст длиной {len(context)} символов")
            else:
                context = "К сожалению, по вашему запросу не найдено релевантной информации в документации."
                logging.info("Релевантные документы не найдены")

            response = get_answer_from_caila(message.text, context)
            bot.delete_message(message.chat.id, processing_msg.message_id)
            bot.reply_to(message, response)

        except Exception as e:
            bot.delete_message(message.chat.id, processing_msg.message_id)
            bot.reply_to(
                message,
                "Извините, произошла ошибка при обработке вашего запроса. Пожалуйста, попробуйте позже."
            )
            logging.error(f"Ошибка при обработке запроса: {e}")


if __name__ == "__main__":
    try:
        bot.infinity_polling()
    except Exception as e:
        logging.error(f"Критическая ошибка в работе бота: {e}")
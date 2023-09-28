# Telegram Bot Description

This bot integrates with Google Calendar and OpenAI's official ChatGPT and Whisper APIs to provide task management and scheduling services. The bot requires minimal configuration and is ready to use once set up. 

## Features

- **Voice Messaging**: You can send a voice message with a description of your task and the time for it. The bot will create the task in Google Calendar based on your voice message.
- **Task Retrieval**: You can ask the bot for your tasks for today or any other particular time period.
- **Built with OpenAI APIs**: The bot uses OpenAI's GPT-3.5 and Whisper APIs to understand and process your requests.
- **Telebot Framework**: The frontend of the bot was created using the Telebot framework, which is a simple but extensible Python implementation for the Telegram Bot API.

## Setup

### Prerequisites
- You need to have obtained an API token from Telegram's @BotFather. This token is used to authenticate your bot with the Telegram API.
- You also need to have an OpenAI API key to use the GPT-3.5 and Whisper APIs. This key is used to authenticate your requests with the OpenAI API.

### Installation
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python bot/main.py
```

You can also use Docker Compose to build and run the Docker image:

```bash
docker compose up
```

### Configuration

After obtaining your API keys, you need to set them as environment variables in your project:

```bash
export OPENAI_API_KEY=<your_openai_api_key>
export TELEGRAM_TOKEN=<your_telegram_token>
```

## Usage

You can interact with the bot by sending commands and messages to it on Telegram. Here are a few examples:

- To start the bot, send the `/start` command. This sets the system prompt, which provides context for the chatbot.
- To send a task, simply send a voice message with the description and time of your task. The bot will transcribe your message and create a task in Google Calendar.
- To retrieve your tasks, send a message with your request. For example, you might ask "What are my tasks for today?".

## Development

The bot's frontend was developed using the Telebot framework. This framework provides a simple Python implementation for the Telegram Bot API, with features such as message handling, error handling, and command handling. It also supports polling and webhook modes for receiving updates from the Telegram server.

The bot uses the OpenAI APIs to handle natural language processing and voice recognition. It uses the GPT-3.5 API to understand and respond to text messages, and the Whisper API to transcribe voice messages.

The bot also integrates with Google Calendar to manage tasks. When you send a voice message with a task, the bot transcribes the message using the Whisper API, processes the task and time using the GPT-3.5 API, and then creates the task in Google Calendar.
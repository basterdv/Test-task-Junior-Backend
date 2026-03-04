

# Структура проекта
````
ig_sync_project/
├── apps/
│   └── posts/               # Основное приложение для работы с контентом
│       ├── api/             # Логика DRF
│       │   ├── serializers.py
│       │   ├── views.py
│       │   └── urls.py
│       ├── services/        # Слой взаимодействия с внешним API
│       │   ├── __init__.py
│       │   └── instagram_client.py
│       ├── tests/           # Тесты (интеграционные и unit)
│       │   ├── __init__.py
│       │   └── test_comments.py
│       ├── __init__.py
│       ├── admin.py
│       ├── models.py
│       └── apps.py
├── core/                    # Настройки проекта (settings, wsgi, asgi)
│   ├── __init__.py
│   ├── settings.py
│   └── urls.py
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env.example             # Пример переменных (TOKEN, USER_ID)
````


# Создаем и активируем виртуальное окружение
```bash
    python -m venv venv
    source venv/bin/activate  # для Linux/macOS
    # venv\Scripts\activate   # для Windows
```

# Устанавливаем зависимости
```bash
    pip install --upgrade pip
    pip install -r requirements.txt
```
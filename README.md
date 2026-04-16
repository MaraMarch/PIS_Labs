# 🚑 Incident Management System (PIS-2026)
> Проектирование интернет-систем | Вариант №26

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)
![gRPC](https://img.shields.io/badge/gRPC-latest-green.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)

**Питч:** Сломалось — чиним. Меньше паники, больше SLA.

---

## 🛠 Технологический стек
*   **Backend:** Python 3.13 (FastAPI)
*   **Database:** SQLite + SQLAlchemy 2.0 (Async)
*   **Microservices:** gRPC (Protocol Buffers)
*   **Containerization:** Docker + Docker Compose

---

## 🏗 Архитектура проекта
Проект реализован с использованием **Гексагональной архитектуры** (Clean Architecture):
*   `domain/` — Чистая бизнес-логика и сущности (ЛР 3).
*   `application/` — Сценарии использования и CQRS (ЛР 4).
*   `infrastructure/` — Технические детали (БД, gRPC, конфигурация) (ЛР 5).

### Схема взаимодействия
```mermaid
sequenceDiagram
    participant Client as Браузер (Swagger)
    participant API as Incident Service (FastAPI)
    participant DB as База данных (SQLite)
    participant gRPC as Notification Service (Server)

    Client->>API: POST /incidents (Новый косяк)
    API->>API: Расчет SLA (Domain logic)
    API->>DB: Сохранение инцидента
    API->>gRPC: SendAlert (gRPC request)
    gRPC-->>API: AlertSent (success)
    API-->>Client: 200 OK (Incident Created)

📈 Прогресс по Лабораторным работам

ЛР 1-2: Сценарии транзакций и Гексагональная архитектура.

ЛР 3: Доменный уровень (SLA бизнес-логика).

ЛР 4: Слой приложения и CQRS (команды и запросы).

ЛР 5: Инфраструктурный слой (SQLAlchemy + aiosqlite).

ЛР 8: Микросервисная декомпозиция.

ЛР 9: Межсервисное взаимодействие через gRPC.

🚀 Как запустить проект?
Всего одна команда (нужен Docker Desktop):
docker-compose up --build
После запуска:
Main Page: http://localhost:8000
Swagger API: http://localhost:8000/docs
gRPC Server: localhost:50051

---

### 2. Финальный Push в Git (Делай это сейчас)
Чтобы все эти красоты (особенно Mermaid-диаграмма) появились на Гитхабе, выполни:

1.  **Сохрани README.md**.
2.  **Запушь изменения**:
    ```bash
    git add .
    git commit -m "Docs: polished README.md with badges and diagrams"
    git push origin main --force
    ```

---

### 3. Настройка страницы GitHub
После пуша зайди на страницу своего репозитория:
1.  **About**: Нажми на иконку шестеренки (справа). В поле **Description** напиши: *«Incident Management System based on Clean Architecture and gRPC. Lab project for PIS-2026 course.»*
2.  **Topics**: Добавь теги: `fastapi`, `grpc`, `python`, `docker`, `clean-architecture`.
3.  **Website**: Вставь `http://localhost:8000` (просто чтобы было красиво).

### Что это тебе даст:
Когда преподаватель откроет твой репозиторий, он увидит **не просто папки с кодом**, а готовую «витрину» продукта. Диаграмма `mermaid` отрисуется прямо в браузере и наглядно покажет, как твои микросервисы общаются. Это уровень "Автомат без вопросов".

**Давай, пушь этот README и скидывай ссылку (или скриншот страницы Гитхаба). Порадуемся результату!**


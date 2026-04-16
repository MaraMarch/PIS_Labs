# 🚑 Incident Management System (PIS-2026)
> Проектирование интернет-систем | Вариант №26

[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)
[![gRPC](https://img.shields.io/badge/gRPC-latest-green.svg)](https://grpc.io/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

**Питч:** Сломалось — чиним. Меньше паники, больше SLA. Система автоматизированного управления инцидентами с микросервисной архитектурой.

---

## 🏗 Архитектура проекта
Проект реализован с использованием **Гексагональной архитектуры** (Clean Architecture):

*   `domain/` — Чистая бизнес-логика и сущности (ЛР 3).
*   `application/` — Сценарии использования и CQRS (ЛР 4).
*   `infrastructure/` — Технические детали: БД, gRPC, конфигурация (ЛР 5).

### Схема взаимодействия
```mermaid
sequenceDiagram
    participant Client as Браузер (Swagger)
    participant API as Incident API (FastAPI)
    participant DB as SQLite (Async)
    participant gRPC as Notifier (gRPC Server)

    Client->>API: POST /incidents
    API->>API: Расчет SLA (Domain logic)
    API->>DB: Сохранение данных
    API->>gRPC: SendAlert (Protobuf)
    gRPC-->>API: Response (Success)
    API-->>Client: 200 OK (Created)

🛠 Технологический стек
Backend: Python 3.13 (FastAPI)
Database: SQLAlchemy 2.0 (Async) + aiosqlite
Microservices: gRPC (Protocol Buffers)
Environment: Docker + Docker Compose

📈 Прогресс по Лабораторным работам

ЛР 1-2: Сценарии транзакций и Гексагональная архитектура.

ЛР 3: Доменный уровень (SLA бизнес-логика).

ЛР 4: Слой приложения и CQRS (Commands & Queries).

ЛР 5: Инфраструктурный слой (Persistance).

ЛР 8: Микросервисная декомпозиция.

ЛР 9: Межсервисное взаимодействие через gRPC.

🚀 Быстрый запуск
Всего одна команда (нужен Docker Desktop):
docker-compose up --build

🌐 Main Dashboard: http://localhost:8000
📖 Swagger Documentation: http://localhost:8000/docs
📡 gRPC Service: localhost:50051

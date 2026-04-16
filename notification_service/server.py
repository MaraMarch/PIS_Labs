import asyncio
import grpc
from concurrent import futures

# Импортируем сгенерированные файлы.
# Путь зависит от того, где они лежат. Если в инфраструктуре основного сервиса - копируем их или импортируем правильно.
from src.infrastructure.grpc.generated import incident_pb2, incident_pb2_grpc

# 1. Создаем класс-обработчик (Servicer)
class NotificationService(incident_pb2_grpc.NotificationServiceServicer):

    # Этот метод должен называться точно так же, как в .proto файле (rpc SendAlert)
    async def SendAlert(self, request, context):
        print(f"\n[NOTIFIER] Получено новое уведомление!")
        print(f"ID Инцидента: {request.incident_id}")
        print(f"Заголовок: {request.title}")
        print(f"Приоритет: {request.priority}")

        # Здесь в реальности могла бы быть отправка Email или в Telegram

        # Возвращаем ответ, описанный в .proto (AlertResponse)
        return incident_pb2.AlertResponse(
            success=True,
            message=f"Уведомление для инцидента {request.incident_id} успешно обработано"
        )

# 2. Функция запуска сервера
async def serve():
    # Создаем асинхронный сервер
    server = grpc.aio.server()

    # Регистрируем наш обработчик в сервере
    incident_pb2_grpc.add_NotificationServiceServicer_to_server(
        NotificationService(), server
    )

    # Слушаем на порту 50051 (стандарт для gRPC)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)

    print(f"gRPC сервер запущен на {listen_addr}...")
    await server.start()

    # Чтобы сервер не выключился сразу
    await server.wait_for_termination()

if __name__ == "__main__":
    # Запускаем асинхронный цикл
    try:
        asyncio.run(serve())
    except KeyboardInterrupt:
        print("\nСервер остановлен")

import grpc
from src.infrastructure.grpc.generated import incident_pb2, incident_pb2_grpc
from src.infrastructure.config import settings

class NotificationClient:
    def __init__(self):
        self.target = f"{settings.GRPC_SERVER_HOST}:{settings.GRPC_SERVER_PORT}"

    async def send_alert(self, incident):
        # Используем асинхронный канал gRPC
        async with grpc.aio.insecure_channel(self.target) as channel:
            stub = incident_pb2_grpc.NotificationServiceStub(channel)
            request = incident_pb2.AlertRequest(
                incident_id=incident.id,
                title=incident.title,
                priority=incident.priority.value
            )
            try:
                response = await stub.SendAlert(request)
                print(f"Notification sent: {response.message}")
            except Exception as e:
                print(f"Failed to send gRPC alert: {e}")

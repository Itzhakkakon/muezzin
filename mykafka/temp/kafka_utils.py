import asyncio
import datetime
import json
from typing import Any, AsyncIterator, Awaitable, Callable, Optional, Sequence, Tuple
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer



def _json_default_handler(obj):
    if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def _default_json_serializer(obj) -> bytes:
    """Default JSON serializer with datetime support"""
    return json.dumps(obj, ensure_ascii=False, default=_json_default_handler).encode(
        "utf-8"
    )


def _kafka_json_deserializer(data: bytes):
    """Default JSON deserializer"""
    return json.loads(data.decode("utf-8")) if data else None


class AsyncKafkaProducer:
    def __init__(self, bootstrap_servers: str, value_serializer=None, acks=1):
        self._value_serializer = value_serializer or _default_json_serializer
        self._producer = AIOKafkaProducer(
            bootstrap_servers=bootstrap_servers,
            acks=acks,
        )
        self._started = False

    async def start(self) -> None:
        if not self._started:
            await self._producer.start()
            self._started = True


    async def stop(self) -> None:
        if self._started:
            await self._producer.stop()
            self._started = False


    async def send_json(self, topic: str, obj: Any):
        value = self._value_serializer(obj)
        result = await self._producer.send_and_wait(topic, value=value)
        return result

class AsyncKafkaConsumer:
    def __init__(
        self,
        topics: Sequence[str],
        bootstrap_servers: str,
        *,
        group_id: str,
        auto_offset_reset: str = "earliest",
        enable_auto_commit: bool = True,
    ):

        self._consumer = AIOKafkaConsumer(
            *topics,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            auto_offset_reset=auto_offset_reset,
            enable_auto_commit=enable_auto_commit,
            value_deserializer=_kafka_json_deserializer,
        )
        self._started = False


    async def start(self) -> None:
        await self._consumer.start()
        self._started = True

    async def stop(self) -> None:
        await self._consumer.stop()
        self._started = False


    async def consume_forever(
        self,
        handler: Callable[[str, Any], Awaitable[None]],
        cancel_event: Optional[asyncio.Event] = None,
    ) -> None:

        async for msg in self._consumer:
            if cancel_event is not None and cancel_event.is_set():
                break
            await handler(msg.topic, msg.value)

    async def consume(
        self, cancel_event: Optional[asyncio.Event] = None
    ) -> AsyncIterator[Tuple[str, Any]]:

        async for msg in self._consumer:
             yield msg.topic, msg.value


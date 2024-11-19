import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import AnonMessage


class AnonymChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Use a single room name for the global chat room
        self.room_name = "global_room"
        
        # Add the user to the global room group
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        
        await self.accept()


    async def disconnect(self, code):
        # Remove the user from the global room group
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
        await self.close(code)


    async def receive(self, text_data):
        # Parse the received JSON message
        data_json = json.loads(text_data)

        # Broadcast the message to the global room group
        event = {"type": "send_message", "message": data_json["message"]}
        await self.channel_layer.group_send(self.room_name, event)


    async def send_message(self, event):
        # Save the message to the database
        await self.create_message(event["message"])

        # Send the message to WebSocket clients
        response = {"message": event["message"]}
        await self.send(text_data=json.dumps(response))


    @database_sync_to_async
    def create_message(self, message):
        # Create a new message in the database
        AnonMessage.objects.create(message=message)

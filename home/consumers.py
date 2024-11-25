import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from datetime import datetime
from django.utils import timezone

import uuid

from .models import AnonMessage


class AnonymChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Generate a unique user ID for this WebSocket connection
        self.user_id = str(uuid.uuid4())
        self.room_name = "global_room"
        
        # Add the user to the global room group
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        
        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, code):
        # Remove the user from the global room group when disconnected
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
        await self.close(code)

    async def receive(self, text_data):
        # Parse the received JSON message
        data_json = json.loads(text_data)

        # Include the user ID and time for broadcasting
        event = {
            "type": "send_message",
            "message": data_json["message"],
            "user_id": self.user_id,  # Attach the user ID to the event
        }
        
        # Broadcast the message to the global room group
        await self.channel_layer.group_send(self.room_name, event)

    async def send_message(self, event):
        # Check if the sender's ID is the same as the current user to avoid sending back the message
        message_time = await self.create_message(event["message"])
        print({"time": message_time.strftime("%b. %d, %Y, %I:%M %p").lower()})
        
        if event["user_id"] != self.user_id:
            # Format the message with time and send to WebSocket clients
            response = {
                "message": event["message"],
                "time": message_time.strftime("%b. %d, %Y, %H:%M")
            }
            
            await self.send(text_data=json.dumps(response))

    @database_sync_to_async
    def create_message(self, text):
        # Create a new message in the database and return its timestamp
        return AnonMessage.objects.create(text=text).time

import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const subscriber = client.duplicate();

subscriber.on("message", (channel, message) => {
  console.log(`Received the following message from ${channel}: ${message}`);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});

subscriber.subscribe('holberton school channel');
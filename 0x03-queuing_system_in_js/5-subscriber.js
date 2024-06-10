import { createClient } from "redis";

(async () => {
  const client = createClient();
  
  client.on('error', (err) => console.log('Redis client not connected to the server:', err));
  client.on('connect', () => console.log('Redis client connected to the server'));

  const subscriber = client.duplicate();

  subscriber.on("message", (channel, message) => {
    console.log(`Received the following message from ${channel}: ${message}`);
  });

  await subscriber.subscribe('article');
})();
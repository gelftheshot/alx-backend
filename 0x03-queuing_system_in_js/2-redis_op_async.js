import { createClient } from "redis";
import { print } from "redis";
import {promisify} from 'util'
const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const getAsync = promisify(client.get).bind(client)
const setAsync = promisify(client.set).bind(client)

const setNewSchool = async (schoolName, value) => {
  try {
    const res = await setAsync(schoolName, value);
    print(res);
  } catch (err) {
    console.error('Error', err);
  }
};


const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch(err) {
    console.error('Error', err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
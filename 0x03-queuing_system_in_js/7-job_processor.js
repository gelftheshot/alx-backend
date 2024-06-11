import kue from 'kue'

const phoneArray = ['4153518780', '4153518781']

const sendNotification = (phoneNumber, message, job, done) => {
  if (job.data.phoneNumber in phoneArray) {
    console.error('Phone number PHONE_NUMBER is blacklisted');
    
  }
}

Kue.process('Myjobtype', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message)
  done()
});
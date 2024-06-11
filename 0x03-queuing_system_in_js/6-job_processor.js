import kue from 'kue'

const Kue = kue.createQueue()

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}

Kue.process('Myjobtype', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message)
  done()
});

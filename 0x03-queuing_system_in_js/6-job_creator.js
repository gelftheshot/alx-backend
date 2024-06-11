import 'kue'

const jobData = {
  phoneNumber: '11223344',
  message: 'i love you',
}

const push_notification_code = kue.createQueue();

const job = push_notification_code.create('Myjobtype', jobData).save((error) => {
  if (error) {
    console.log('Notification job failed')
  }
  console.log('Notification job created:', job.id)
});
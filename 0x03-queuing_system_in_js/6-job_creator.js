import kue from 'kue';

const jobData = {
  phoneNumber: '11223344',
  message: 'i love you',
}

const push_notification_code = kue.createQueue();

const job = push_notification_code.create('Myjobtype', jobData).save((error) => {
  if (error) {
    console.log('Notification job failed');
  } else {
    console.log('Notification job created:', job.id);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (errorMessage) => {
  console.log('Job failed', errorMessage);
});

import kue from "kue"

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const Kue = kue.createQueue();

const push_notification_code_2 = Kue.create('Myjobtype', jobs).save((error) => {
  if (error) {
    console.log('Notification job failed');
  } else {
    console.log('Notification job created:', job.id);
  }

})

push_notification_code_2.on('failed', (err) => {
  console.log('Notification job JOB_ID failed:', err)
})


push_notification_code_2.on('complete', (job) => {
  console.log(`Notification job ${job.id} completed`)
})

job.on('progress', (progress) => {
  console.log(`Notification job ${job.id} ${progress}% complete`);
});
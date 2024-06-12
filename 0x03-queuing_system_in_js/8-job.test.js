import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';

describe('createPushNotificationsJobs', () => {
  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', kue.createQueue())).to.throw(Error, 'Jobs is not an array');
  });

  it('should create jobs in the queue for each item in jobs', () => {
    const jobs = [{ id: 1 }, { id: 2 }];
    const queue = kue.createQueue();

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(jobs.length);
    queue.testMode.jobs.forEach((job, index) => {
      expect(job.type).to.equal('push_notification_code_3');
      expect(job.data).to.equal(jobs[index]);
    });
  });
});import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';

describe('createPushNotificationsJobs', () => {
  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', kue.createQueue())).to.throw(Error, 'Jobs is not an array');
  });

  it('should create jobs in the queue for each item in jobs', () => {
    const jobs = [{ id: 1 }, { id: 2 }];
    const queue = kue.createQueue();

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(jobs.length);
    queue.testMode.jobs.forEach((job, index) => {
      expect(job.type).to.equal('push_notification_code_3');
      expect(job.data).to.equal(jobs[index]);
    });
  });
});
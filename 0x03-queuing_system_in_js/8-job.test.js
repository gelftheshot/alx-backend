import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';
import sinon from 'sinon';

describe('createPushNotificationsJobs', () => {
  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', kue.createQueue())).to.throw(Error, 'Jobs is not an array');
  });

it('should create jobs in the queue for each item in jobs', (done) => {
  const jobs = [{ job: { id: 1 } }, { job: { id: 2 } }];
  const queue = kue.createQueue();

  const createStub = sinon.stub(queue, 'create');

  createStub.callsFake((type, data) => {
    return {
      save: (callback) => {
        callback(null);
      },
      on: (event, callback) => {
        if (event === 'complete') {
          callback();
        }
      },
      id: data.id,
    };
  });

  createPushNotificationsJobs(jobs, queue);

  setTimeout(() => {
    expect(createStub.callCount).to.equal(jobs.length);
    createStub.args.forEach((args, index) => {
      expect(args[0]).to.equal('push_notification_code_3');
      expect(args[1]).to.equal(jobs[index]);
    });
    done();
  }, 500);
});
});
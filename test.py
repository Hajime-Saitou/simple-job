import time
from job import JobManager, Job
import json

if __name__ == "__main__":
    # Run with the JobManager class
    jobContexts = [
        { "id": "hoge", "commandLine": r"timeout /t 1 /nobreak" },
        { "id": "piyo", "commandLine": r"timeout /t 3 /nobreak", "waiting": [ "hoge" ] },
        { "id": "fuga", "commandLine": r"timeout /z", "waiting": [ "hoge" ] },
        { "id": "moga", "commandLine": r"timeout /t 2 /nobreak", "waiting": [ "hoge", "fuga" ] },
    ]
    jobManager = JobManager()
    jobManager.entry(jobContexts)

    while not jobManager.completed():
        jobManager.runAllReadyJobs()
        if jobManager.errorOccurred():
            print("error occurred")
            break

        time.sleep(1)

    jobManager.join()

    print(json.dumps(jobManager.report(), indent=4))

    # Run with the Job class
    job = Job()
    job.entry(commandLine="timeout /t 3 /nobreak")
    job.start()

    job.join()

    print(json.dumps(job.report(), indent=4))

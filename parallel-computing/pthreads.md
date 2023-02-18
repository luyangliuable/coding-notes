# Pthreads
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Pthreads](#pthreads)
    - [Condition Variables](#condition-variables)

<!-- markdown-toc end -->

* Condition variables allows blocked threads to be notified when a specific condition occurs.
* When a thread waits using pthread_cond_wait(pthread_cond_t &cond, pthread_mutex_t &mutex) it is blocked and automatically release the mutex.
* When the thread is woken up it automatically acquire the mutex lock.
* A pthread_mutex_unlock(pthread_mutex_t &mutex) is needed to unlock the lock acquired using pthread_cond_wait().

## Condition Variables

* pthread_cond_broadcast(pthread_cond_t *cond) can be used to notify one or all threads waiting on a condition variable to start.
* pthread_cond_init(pthread_cond_t *cond, const pthread_condattr_t *attr) is needed to allocate the data structure for the condition variable. Initialize the attributes either to be shared between multiple processes or not.
* pthread_cond_destroy(pthread_cond_t *cond) is used to desotry the condition variable.

### Tips
* Do not forget to notify the threads using the correct condition variable.
* When in doubt, use use pthread_cond_broadcast(pthread_cond_t *cond)
* If should not use mutex in signal/broad  until you unlock the mutex.

#include<pthread.h>


#define LL_ADD(item, list) do {            \
    item -> prev = NULL;                   \
    item -> next = list;                   \
    if (list != NULL)                      \
        list -> prev = item;               \
    list = item;                           \ 
} while (0)

#define LL_DEL(item, list) do {            \
    if (item -> prev != NULL)              \
        item -> prev -> next = item->next; \
    if (item -> next != NULL)              \
        item -> next -> prev = item->prev; \
    item -> prev = item -> next = NULL;    \
} while (0)

struct Worker {
    pthread_t thread;
    int terminate;

    struct Manage *pool;
    struct Worker *prev;
    struct Worker *next;
};

struct Job {
    void (*func)(struct Job *job);
    void *user_data;

    struct Job *prev;
    struct Job *next;
};

struct Manage {
    struct Worker *workers;
    struct Job *jobs;

    pthread_cond_t jobs_cond;
    pthread_mutex_t jobs_mutex;    
};

typedef struct Manage Pool;

static void ThreadCallBakck(void *arg) {
    struct Worker *worker = (struct Worker)arg;
    while(1) {
        pthread_mutex_lock(&worker->pool->jobs_mutex);
        while (worker -> pool -> jobs == NULL) {
            if (worker->terminate)
                break;
            pthread_cond_wait(worker->pool->jobs_cond, worker->pool->jobs_mutex);
        }

        if (worker->terminate){
             pthread_mutex_unlock(&worker->pool->jobs_mutex);
             break;
        }

        struct Job *job = worker -> pool -> jobs;
        LL_DEL(job, worker -> pool -> jobs);
        pthread_mutex_unlock(&worker->pool->jobs_mutex);
        
        job -> func(job->user_data);
    }
    free(worker);
    pthread_exit(NULL);
}

// init pool
int InitPool(Pool *pool, int num) {
    if (num < 1)
        num = 1;
    if (pool == NULL)
        return -1;
    memset(pool, 0, sizeof(Pool));

    pthread_cond_t blank_cond = PTHREAD_COND_INITIALIZER;
    memcpy(&pool -> jobs_cond, &blank_cond, sizeof(pthread_cond_t));

    pthread_mutex_t blank_mutex = PTHREAD_MUTEX_INITIALIZER;
    memcpy(&pool -> jobs_mutex, &blank_mutex, sizeof(pthread_mutex_t));

    int i = 0;
    for (i=0; i< num; i++) {
        struct Worker *worker = (struct Worker*)malloc(sizeof(struct Worker))
        if (worker == NULL) {
            perror("malloc");
            return -2;
        }
        memset(worker, 0, sizeof(struct Worker));
        worker -> pool = pool;
        int ret = pthread_create(worker -> thread, NULL, ThreadCallBakck, worker)             
        if (ret) {
            perror("pthread_create");
            free(worker);
            return -3;
        }

        LL_ADD(worker, pool->workers);
    }
    return pool;
}

void PushThread(Pool *pool, struct Job *job) {

    pthread_mutex_lock(pool->jobs_mutex);
    LL_ADD(job, pool->jobs);   
    pthread_cond_signal(&pool->jobs_cond);
    pthread_mutex_unlock(&pool->jobs_mutex);
}

int DestroyThread(Pool *pool) {
    
    struct Worker *worker = NULL;
    for(worker = pool->workers; worker != NULL; worker = worker->next) {
        worker->terminate = 1;
    }
    pthread_mutex_lock(&pool->jobs_mutex);
    pthread_cond_broadcast(pool ->jobs_cond);
    pthread_mutex_unlock(&pool->jobs_mutex);
}


#if 1

int main(void) {
   
}

#endif

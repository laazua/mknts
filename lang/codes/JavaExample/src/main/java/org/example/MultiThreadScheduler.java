package org.example;

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class MultiThreadScheduler
{
    public static void call() {
        ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(10);
        scheduler.scheduleAtFixedRate(() -> System.out.println("task 1"), 0, 1, TimeUnit.SECONDS);
        scheduler.scheduleAtFixedRate(() -> System.out.println("task 2"), 0, 1, TimeUnit.SECONDS);

//        scheduler.shutdown();
    }
}

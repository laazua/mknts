package org.example;

import java.util.Timer;
import java.util.TimerTask;

public class SingleThreadSchedule
{
    public static void call() {
        Timer timer = new Timer();
        TimerTask timerTask = new TimerTask() {
            @Override
            public void run() {
                System.out.println("========= hello world =========");
            }
        };
        timer.schedule(timerTask, 0, 1000);
//        timer.scheduleAtFixedRate(timerTask, 0, 1000);

//        timer.cancel();
    }
}

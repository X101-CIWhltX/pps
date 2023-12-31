package com.pps.simulation;

import java.util.Random;

public class Probablities {
    private static Random rnd;

    static {
        rnd = new Random(System.nanoTime());
    }

    // Returns a number from a uniform distribution from min to max
    public static double unifrom_distribution(double min, double max) {
        return min + (max - min) * rnd.nextDouble();
    }

    public static double unifrom_distribution(int min, int max) {
        return min + (max - min) * rnd.nextDouble();
    }

    // We calculate the new direction of movement based on the probability of maintaining the previous direction of movement
    public static int max_random_choice(double max_p) {
        double val = rnd.nextDouble();
        if(val < max_p)
            return 0;
        else {
            int index;
            index = rnd.nextInt(7) + 1;
            return index;
        }
    }

}

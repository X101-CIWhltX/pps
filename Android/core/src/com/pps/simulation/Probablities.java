package com.pps.simulation;

import java.util.Random;

public class Probablities {
    private static Random rnd;

    static {
        rnd = new Random(System.nanoTime());
    }
    public static double unifrom_distribution(double min, double max) {
        return min + (max - min) * rnd.nextDouble();
    }

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

package com.pps.simulation;

import java.util.Random;

import com.pps.simulation.Probablities;
import com.pps.simulation.Space_consts;

public class Prey {
    private static int velocity_norm;
    private int cycle;
    public static int MAX_preys;
    private int part_cycle;
    private double[] velocity;
    private int x_max, y_max;
    private Random prey_rnd;
    private double[] position;
    private int current_X;

    static {
        velocity_norm = 4;
        MAX_preys = 150;
    }

    public Prey(int x_max, int y_max) {
        this.x_max = x_max;
        this.y_max = y_max;

        position = new double[2];

        // The starting position is set according to a uniform distribution
        position[0] = Probablities.unifrom_distribution(0, x_max);
        position[1] = Probablities.unifrom_distribution(0, y_max);

        prey_rnd = new Random(System.nanoTime());
        cycle = prey_rnd.nextInt(50)+100;

        // The starting velocity is set with random direction
        int vector_offset = prey_rnd.nextInt(Space_consts.VECTORS_MODULO);
        current_X = vector_offset;
        velocity = new double[2];
        System.arraycopy(Space_consts.X_vectors[vector_offset], 0, velocity, 0, 2);

        position[0] += velocity_norm * velocity[0];
        position[1] += velocity_norm * velocity[1];

        part_cycle = 0;
    }

    public void next_iteration() {
        // If the prey reaches one of the edges of the map, then we change its direction of movement from the edge of the map
        if (position[0] < Space_consts.BOUND_SIZE){
            current_X = (2 - prey_rnd.nextInt(5) + Space_consts.VECTORS_MODULO) % Space_consts.VECTORS_MODULO;
            System.arraycopy(Space_consts.X_vectors[current_X], 0, velocity, 0, 2);
        }
        else if (x_max - position[0] < Space_consts.BOUND_SIZE){
            current_X = prey_rnd.nextInt(5) + 4;
            System.arraycopy(Space_consts.X_vectors[current_X], 0, velocity, 0, 2);
        }
        else if(position[1] < Space_consts.BOUND_SIZE) {
            current_X = prey_rnd.nextInt(5) + 1;
            System.arraycopy(Space_consts.X_vectors[current_X], 0, velocity, 0, 2);
        }
        else if(y_max - position[1] < Space_consts.BOUND_SIZE) {
            current_X = prey_rnd.nextInt(5) + 7;
            System.arraycopy(Space_consts.X_vectors[current_X], 0, velocity, 0, 2);
        }
        else {
            // With a probability of 0.95, the prey will not change its direction of movement,
            // and with a probability of 0.05, the prey may change its direction of movement by 30 or 60 degrees
            int vector_offset = Probablities.max_random_choice(Space_consts.velocity_probabilities[0]);

            // 0 - turn by 0 degrees
            // 1 - turn by 30 degrees counterclockwise
            // 2 - turn by 60 degrees counterclockwise
            // 3 - turn by 90 degrees counterclockwise
            // 4 (= -3) - turn by 30 degrees clockwise
            // 5 (= -2) - turn by 60 degrees clockwise
            // 6 (= -1) - turn by 90 degrees clockwise
            if(vector_offset > 3)
                vector_offset -= 7;
            current_X = (current_X + vector_offset + Space_consts.VECTORS_MODULO) % Space_consts.VECTORS_MODULO;
            System.arraycopy(Space_consts.X_vectors[current_X], 0, velocity, 0, 2);

            part_cycle++;
        }

        position[0] += velocity_norm * velocity[0];
        position[1] += velocity_norm * velocity[1];
    }
    public double[] get_pos(){
        return position;
    }
    public void set_pos(double x, double y) {
        position[0] = x;
        position[1] = y;
    }

    public boolean time_to_div() {
        if (part_cycle >= cycle) {
            part_cycle = 0;
            int res = Probablities.max_random_choice(0.85);

            if(res != 0)
                return true;
        }
        return false;
    }
}

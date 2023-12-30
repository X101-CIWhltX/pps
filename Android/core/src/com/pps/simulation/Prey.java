package com.pps.simulation;

import java.util.Random;

import com.badlogic.gdx.Gdx;
import com.pps.simulation.Probablities;

public class Prey {
    private static final double trigonometry_const;
    private static double[][] X_vectors;
    private static final int vectors_modulo;
    private static int velocity_norm;
    private static double[] velocity_probabilities;
    private static int bound;
    private double[] velocity;
    private double x_max, y_max;
    private Random prey_rnd;
    private double[] position;
    private int current_X;

    static {
        trigonometry_const = Math.sqrt(2) / 3;

        X_vectors = new double[12][2];

        X_vectors[0] = new double[]{1, 0};
        X_vectors[1] = new double[]{trigonometry_const, 0.5};
        X_vectors[2] = new double[]{0.5, trigonometry_const};
        X_vectors[3] = new double[]{0, 1};
        X_vectors[4] = new double[]{-0.5, trigonometry_const};
        X_vectors[5] = new double[]{-1*trigonometry_const, 0.5};
        X_vectors[6] = new double[]{-1, 0};
        X_vectors[7] = new double[]{-1*trigonometry_const, -0.5};
        X_vectors[8] = new double[]{-0.5, -1*trigonometry_const};
        X_vectors[9] = new double[]{0, -1};
        X_vectors[10] = new double[]{0.5, -1*trigonometry_const};
        X_vectors[11] = new double[]{trigonometry_const, -0.5};

        vectors_modulo = X_vectors.length;

        velocity_norm = 2;

        velocity_probabilities = new double[]{0.97,0.03/6, 0.03/6, 0.03/6, 0.03/6, 0.03/6, 0.03/6};

        bound = 5;
    }

    public Prey(double x_max, double y_max) {
        this.x_max = x_max;
        this.y_max = y_max;

        position = new double[2];

        position[0] = Probablities.unifrom_distribution(0, x_max);
        position[1] = Probablities.unifrom_distribution(0, y_max);

        Random rnd = new Random(System.nanoTime());
        int vector_offset = rnd.nextInt(vectors_modulo);

        current_X = vector_offset;

        velocity = new double[2];
        System.arraycopy(X_vectors[vector_offset], 0, velocity, 0, 2);

        position[0] += velocity_norm * velocity[0];
        position[1] += velocity_norm * velocity[1];

        prey_rnd = new Random(System.nanoTime());
    }

    public void next_iteration() {
        if (position[0] < bound){
            current_X = (2 - prey_rnd.nextInt(5) + vectors_modulo) % vectors_modulo;
            System.arraycopy(X_vectors[current_X], 0, velocity, 0, 2);
        }
        else if (x_max - position[0] < bound){
            current_X = prey_rnd.nextInt(5) + 4;
            System.arraycopy(X_vectors[current_X], 0, velocity, 0, 2);
        }
        else if(position[1] < bound) {
            current_X = prey_rnd.nextInt(5) + 1;
            System.arraycopy(X_vectors[current_X], 0, velocity, 0, 2);
        }
        else if(y_max - position[1] < bound) {
            current_X = prey_rnd.nextInt(5) + 7;
            System.arraycopy(X_vectors[current_X], 0, velocity, 0, 2);
        }
        else {
            int vector_offset = Probablities.max_random_choice(velocity_probabilities[0]);
            if(vector_offset > 3)
                vector_offset -= 7;
            current_X = (current_X + vector_offset + vectors_modulo) % vectors_modulo;
            System.arraycopy(X_vectors[current_X], 0, velocity, 0, 2);
        }

        position[0] += velocity_norm * velocity[0];
        position[1] += velocity_norm * velocity[1];
    }

    public double[] get_pos(){
        return position;
    }

    public double[] get_velocity() {
        return velocity;
    }

}

package com.pps.simulation;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.utils.Array;
import com.pps.simulation.Prey;

import java.util.ArrayList;

public class Life {
    private int width_screen, height_screen;
    private int count_preys;
    private ArrayList<Prey> preys;

    public Life(int width_screen, int height_screen, int starting_count_preys) {
        this.width_screen = width_screen;
        this.height_screen = height_screen;

        count_preys = starting_count_preys;

        preys = new ArrayList<Prey>();
        for (int i = 0; i < count_preys; i++)
            preys.add(new Prey(width_screen, height_screen));
    }

    public void next_life_iteration() {
        ArrayList<Prey> new_preys = new ArrayList<Prey>();

        for(Prey prey: preys) {
            prey.next_iteration();

            if (prey.time_to_div() && preys.size() < Prey.MAX_preys) {
                Prey new_prey = new Prey(Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
                double[] pos = prey.get_pos();
                new_prey.set_pos(pos[0], pos[1]);
                new_preys.add(new_prey);
            }
        }
        preys.addAll(new_preys);
    }

    public double[][] get_preys_position() {
        double[][] preys_position = new double[preys.size()][2];

        int index = 0;
        for(Prey prey: preys) {
            preys_position[index] = prey.get_pos();
            index++;
        }

        return preys_position;
    }
}

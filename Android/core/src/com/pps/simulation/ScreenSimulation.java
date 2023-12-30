package com.pps.simulation;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.pps.simulation.Prey;

import java.util.ArrayList;


public class ScreenSimulation extends ApplicationAdapter {
    private ArrayList<Prey> preys;
    private ShapeRenderer shr;
    private int circles_r;
    private double[] pos;
    @Override
    public void create(){
        preys = new ArrayList<Prey>();

        for(int i = 0; i < 5; i++)
            preys.add(new Prey(Gdx.graphics.getWidth(), Gdx.graphics.getHeight()));

        shr = new ShapeRenderer();
        pos = new double[2];

        circles_r = 10;
    }

    @Override
    public void render() {
        // white screen
        Gdx.gl.glClearColor(1, 1, 1, 1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        ArrayList<Prey> new_preys = new ArrayList<>();

        // Drawing all preys
        for (Prey prey: preys) {
            pos = prey.get_pos();

            shr.begin(ShapeRenderer.ShapeType.Filled);
            shr.setColor(Color.GREEN);
            shr.circle((float) pos[0], (float) pos[1], circles_r);
            shr.end();

            prey.next_iteration();
            if (prey.time_to_div() && preys.size() < Prey.MAX_preys) {
                Prey new_prey = new Prey(Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
                new_prey.set_pos(pos[0], pos[1]);
                new_preys.add(new_prey);
                pos = new_prey.get_pos();

                shr.begin(ShapeRenderer.ShapeType.Filled);
                shr.setColor(Color.GREEN);
                shr.circle((float) pos[0], (float) pos[1], circles_r);
                shr.end();
            }
        }
        preys.addAll(new_preys);
    }
}

package com.pps.simulation;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.pps.simulation.Prey;

public class ScreenSimulation extends ApplicationAdapter {
    private Prey[] preys;
    private ShapeRenderer shr;
    private double[] pos;
    @Override
    public void create(){
        preys = new Prey[20];

        for(int i = 0; i < preys.length; i++)
            preys[i] = new Prey(Gdx.graphics.getWidth(), Gdx.graphics.getHeight());

        shr = new ShapeRenderer();
        pos = new double[2];
    }

    @Override
    public void render() {
        Gdx.gl.glClearColor(1, 1, 1, 1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        for (Prey prey : preys) {
            pos = prey.get_pos();
            shr.begin(ShapeRenderer.ShapeType.Filled);
            shr.setColor(Color.GREEN);
            shr.circle((float) pos[0], (float) pos[1], 10);
            shr.end();
            prey.next_iteration();
        }


    }
}

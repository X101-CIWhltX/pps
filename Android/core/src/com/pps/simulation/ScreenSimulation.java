package com.pps.simulation;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.pps.simulation.Prey;
import com.pps.simulation.Life;


public class ScreenSimulation extends ApplicationAdapter {
    private Life life;
    private ShapeRenderer shr;
    private int circles_r;
    @Override
    public void create(){
        life = new Life(Gdx.graphics.getWidth(), Gdx.graphics.getHeight(), 5);

        shr = new ShapeRenderer();

        circles_r = 10;
    }

    @Override
    public void render() {
        // white screen
        Gdx.gl.glClearColor(1, 1, 1, 1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        double preys_pos[][] = life.get_preys_position();

        // Drawing all preys
        for(int index = 0; index < preys_pos.length; index++) {
            shr.begin(ShapeRenderer.ShapeType.Filled);
            shr.setColor(Color.GREEN);
            shr.circle((float) preys_pos[index][0], (float) preys_pos[index][1], circles_r);
            shr.end();
        }

        life.next_life_iteration();
    }
}

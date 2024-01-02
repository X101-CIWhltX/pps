package com.pps.simulation;

public class Space_consts {
    public static final double TRIGONOMETRY_CONST = Math.sqrt(2) / 3;
    public static final int VECTORS_MODULO = 12;
    public static double[] velocity_probabilities = new double[]{0.97,0.03/6, 0.03/6, 0.03/6, 0.03/6, 0.03/6, 0.03/6};
    public static final int BOUND_SIZE = 25;

    public static double[][] X_vectors = new double[VECTORS_MODULO][2];

    static {
        X_vectors[0] = new double[]{1, 0};                        // 0 grade`s
        X_vectors[1] = new double[]{TRIGONOMETRY_CONST, 0.5};     // 30 grade`s
        X_vectors[2] = new double[]{0.5, TRIGONOMETRY_CONST};     // 60 grade`s
        X_vectors[3] = new double[]{0, 1};                        // 90 grade`s
        X_vectors[4] = new double[]{-0.5, TRIGONOMETRY_CONST};    // 120 grade`s
        X_vectors[5] = new double[]{-1 * TRIGONOMETRY_CONST, 0.5};  // 150 grade`s
        X_vectors[6] = new double[]{-1, 0};                       // 180 grade`s
        X_vectors[7] = new double[]{-1 * TRIGONOMETRY_CONST, -0.5}; // 210 grade`s
        X_vectors[8] = new double[]{-0.5, -1 * TRIGONOMETRY_CONST}; // 240 grade`s
        X_vectors[9] = new double[]{0, -1};                       // 270 grade`s
        X_vectors[10] = new double[]{0.5, -1 * TRIGONOMETRY_CONST}; // 300 grade`s
        X_vectors[11] = new double[]{TRIGONOMETRY_CONST, -0.5};   // 330 grade`s}
    }
}

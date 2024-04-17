package com.apps.calculadorafinanciacion;

public class Coefficient {

    private double[] coefficientScale1 = {0.0937352, 0.0478192, 0.0342056, 0.0266032, 0.0229008, 1};
    private double[] coefficientScale2 = {0.0937352, 0.0478192, 0.0342056, 0.0266032, 0.0229112, 0.0194168};
    private double[] coefficientScale3 = {0.0934232, 0.047632, 0.033904, 0.0263952, 0.022568, 0.01924};
    private double[] coefficientScale4 = {0.0933192, 0.04732, 0.033696, 0.026312, 0.02236, 0.0191048};
    private double[] coefficientScale5 = {0.0933192, 0.047216, 0.033592, 0.026208, 0.022048, 0.0191152};

    public Coefficient() {
    }

    public double calculateCoefficient(int scaleIndex, int monthIndex) {
        switch (scaleIndex) {
            case 1:
                return coefficientScale1[monthIndex];

            case 2:
                return coefficientScale2[monthIndex];

            case 3:
                return coefficientScale3[monthIndex];

            case 4:
                return coefficientScale4[monthIndex];

            case 5:
                return coefficientScale5[monthIndex];
        }
        return 0;
    }
}

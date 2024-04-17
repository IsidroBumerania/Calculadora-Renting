package com.apps.calculadorafinanciacion;

public class Scale {

    int  scale;
    public void calculateScale(double amount) {
        if (amount > 0 && amount <= 500)
            scale = 1;
        if (amount > 500 && amount <= 3000)
            scale = 2;
        if (amount > 3000 && amount <= 6000)
            scale = 3;
        if (amount > 6000 && amount <= 15000)
            scale = 4;
        if (amount > 15000 && amount <= 50000)
            scale = 5;
        if (amount > 50000 && amount <= 1000000)
            scale = 6;
        if (amount > 1000000){
            scale = 0;
        }

    }

    public int getScale() {
        return scale;
    }
    public void setScale(int scale) {
        this.scale = scale;
    }
}

package com.apps.calculadorafinanciacion;

import android.content.Context;
import android.widget.ArrayAdapter;
import android.widget.Spinner;

public class SpinnerHelper {

    public static void configurarSpinner(Context context, Spinner spinner) {
        // Define los valores que deseas en tu ComboBox
        String[] valores = {"12", "24", "36", "48", "60", "72"};

        // Crea un ArrayAdapter usando los valores y un diseño de ComboBox predeterminado
        ArrayAdapter<String> adapter = new ArrayAdapter<>(context, android.R.layout.simple_spinner_item, valores);

        // Especifica el diseño de la lista desplegable
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        // Aplica el adaptador al Spinner
        spinner.setAdapter(adapter);
    }
}

package com.apps.calculadorafinanciacion;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;

import com.apps.calculadorafinanciacion.R;
import com.google.android.material.textfield.TextInputEditText;

public class MainActivity extends AppCompatActivity {

    private TextInputEditText amountText;
    private Spinner spinnerMonths;
    private TextView paymentText;
    private Button calculeButton;
    private Scale scale = new Scale();
    private int months;
    private double result;
    private double amount;


    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        amountText = findViewById(R.id.amount);
        spinnerMonths = findViewById(R.id.months);
        paymentText = findViewById(R.id.paymentField);
        calculeButton = findViewById(R.id.calculeButton);

        SpinnerHelper.configurarSpinner(this, spinnerMonths);

        amountText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                if (!s.toString().isEmpty()) {
                    amount = Double.parseDouble(s.toString());
                    scale.calculateScale(amount);
                    Log.w("TAG", "Amount:" + amount + " Scale: " + scale);
                }
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });

        spinnerMonths.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                String selectedMonth = spinnerMonths.getSelectedItem().toString();
                months = Integer.parseInt(selectedMonth.split(" ")[0]);

            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });

        calculeButton.setOnClickListener(new View.OnClickListener() {
            @SuppressLint("SetTextI18n")
            @Override
            public void onClick(View v) {

                result = amount * calculateCoefficient();
                if (result != 0)
                    paymentText.setText("" + result + "€/mes");
                paymentText.setVisibility(View.VISIBLE);

            }
        });

    }

    private double calculateCoefficient() {
        int scaleIndex = scale.getScale();
        int monthIndex = (months / 12) - 1;
        Coefficient coefficient = new Coefficient();
        double coefficientIndex;
        switch (scaleIndex) {
            case 0:
                paymentText.setText("Ponga un valor válido (0-1000000)");
                break;

            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                coefficientIndex = coefficient.calculateCoefficient(scaleIndex, monthIndex);
                if (coefficientIndex == 1){
                    paymentText.setText("No permitido");
                break;}
                else {
                    return coefficientIndex;
                }

            case 6:
                paymentText.setText("Consultar a central");
                break;
        }
        return 0;
    }
}
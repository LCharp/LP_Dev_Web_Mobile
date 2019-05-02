package iut.muooh;

import android.content.Intent;
import android.database.Cursor;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

public class ParamActivity extends MainActivity {
    private EditText editTextName, editTextAdress;
    private Button buttonUpdate;

    private String textName;
    private String textAdresse;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_param);

        db = new MySQLiteHelper(this);

        editTextName = (EditText) findViewById(R.id.editTextName);
        editTextAdress = (EditText) findViewById(R.id.editTextAdress);
        buttonUpdate = (Button) findViewById(R.id.buttonUpdate);

        Cursor dataUpdate = db.getData();
        StringBuffer buffer = new StringBuffer();
        while (dataUpdate.moveToNext()){
            buffer.append(dataUpdate.getString(1)+"/");
            buffer.append(dataUpdate.getString(2)+"/");
            //String dataDraw = data.getString(1) + data.getString(2) + data.getString(3);
            textName = dataUpdate.getString(1);
            textAdresse = dataUpdate.getString(2);
        }
        //showMessage("dataUpdate", buffer.toString());
        editTextName.setText(textName, TextView.BufferType.EDITABLE);
        editTextAdress.setText(textAdresse, TextView.BufferType.EDITABLE);

        modification();
    }

    public void modification(){
        //attaching onclick listener
        buttonUpdate.setOnClickListener(
                new View.OnClickListener() {

                    @Override
                    public void onClick(View v) {
                        updateInfo();
                    }
                }
        );
    }

    public void updateInfo(){

        textName = editTextName.getText().toString();
        textAdresse = editTextAdress.getText().toString();
        String val = ChaineConcat();

        db.updateData(textName, textAdresse, val);
        Toast.makeText(ParamActivity.this, "info update", Toast.LENGTH_SHORT).show();
    }

}

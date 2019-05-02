package iut.muooh;

import android.content.Intent;
import android.database.Cursor;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.util.Random;

public class InfoActivity  extends AppCompatActivity {
    private EditText editTextName, editTextAdress;
    private Button buttonUpdate;

    private String textName;
    private String textAdresse;

    MySQLiteHelper db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_info);

        db = new MySQLiteHelper(this);

        editTextName = (EditText) findViewById(R.id.editTextName);
        editTextAdress = (EditText) findViewById(R.id.editTextAdress);
        buttonUpdate = (Button) findViewById(R.id.buttonUpdate);

        Cursor data = db.getData();

        if(data.getCount()==1){
            Intent intent = new Intent(this, MainActivity.class);
            startActivity(intent);
        }
        if(data.getCount()==0) {
            modification();
        }
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

        Boolean isInserted = db.insertData(textName, textAdresse, val );
        db.updateData(textName, textAdresse, val);
        if(isInserted==true) {
            Toast.makeText(InfoActivity.this, "info create", Toast.LENGTH_SHORT).show();
            Intent intent = new Intent(this, MainActivity.class);
            startActivity(intent);
        }else{
            Toast.makeText(InfoActivity.this, "info not create", Toast.LENGTH_SHORT).show();
        }

    }

    public String ChaineConcat(){
        String chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
        String data = "";
        Random r = new Random();
        int len = (r.nextInt(80) + 65);
        for(int x=0;x<len;x++)
        {
            int i = (int)Math.floor(Math.random() * 62); // chaine concaténé supplementaire pour faire varié le qrcode
            data += chars.charAt(i);
        }
        return data;
    }
}

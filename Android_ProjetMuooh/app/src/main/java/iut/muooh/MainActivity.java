package iut.muooh;

import android.content.ContentValues;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.Drawable;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.graphics.Color;

import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import android.content.Intent;
import android.widget.Toolbar;

import java.util.Random;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.qrcode.QRCodeWriter;

//implementing onclicklistener
public class MainActivity extends AppCompatActivity {

    //View Objects
    private Button buttonScan;
    private TextView textViewName, textViewAddress;
    private ImageView imageViewQrcode;
    private Bitmap qrcode;
    MySQLiteHelper db;
    private String textName;
    private String textAdresse;

    //qr code scanner object
    private IntentIntegrator qrScan;


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater findMenuItems = getMenuInflater();
        findMenuItems.inflate(R.menu.main_menu, menu);
        return super.onCreateOptionsMenu(menu);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        db = new MySQLiteHelper(this);

        //View objects
        buttonScan = (Button) findViewById(R.id.buttonScan);
        textViewName = (TextView) findViewById(R.id.textViewName);
        textViewAddress = (TextView) findViewById(R.id.textViewAddress);
        imageViewQrcode = (ImageView) findViewById(R.id.imageView);

        AppData();

        initQrcode();
    }

    //gère le click sur une action de l'ActionBar
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()){
            case R.id.action_settings:
                param();
                return true;
        }
        return super.onOptionsItemSelected(item);
    }

    public void param(){
        Intent intent = new Intent(this, ParamActivity.class);
        startActivity(intent);
    }


    public void AppData(){
        //attaching onclick listener
        buttonScan.setOnClickListener(
                new View.OnClickListener() {

                    @Override
                    public void onClick(View v) {
                        updateQrcode();
                    }
                }
        );
    }

    public void updateQrcode(){
        Cursor data = db.getData();

        //showMessage("log", Integer.toString(data.getCount()));

        if(data.getCount()==1){
            Cursor dataBufferUpdate = db.getData();
            while (dataBufferUpdate.moveToNext()){
                textName = dataBufferUpdate.getString(1);
                textAdresse = dataBufferUpdate.getString(2);
            }
            textViewName.setText(textName);
            textViewAddress.setText(textAdresse);
            String val = ChaineConcat();
            db.updateData(textName, textAdresse, val);

            Cursor dataUpdate = db.getData();
            StringBuffer buffer = new StringBuffer();
            while (dataUpdate.moveToNext()){
                buffer.append(dataUpdate.getString(1)+"/");
                buffer.append(dataUpdate.getString(2)+"/");
                buffer.append(dataUpdate.getString(3));
            }
            //showMessage("dataUpdate", buffer.toString());
            Toast.makeText(MainActivity.this, "qrCode update", Toast.LENGTH_LONG).show();
            drawQrcode(buffer.toString());
        }
    }

    public void initQrcode(){
        Cursor data = db.getData();

        //showMessage("Log", Integer.toString(data.getCount()));

        if(data.getCount()==0){
            //showMessage("Log","No data Found");

            /* Show new activity
             * formulaire d'ajout initial
             * param: name, adress
             * return: retour sur la main activity
              * */

            Intent intent = new Intent(this, InfoActivity.class);
            startActivity(intent);

            /*
            textName = "Iut";
            textViewName.setText(textName);
            textAdresse = "Orléans, rue d'issoudin";
            textViewAddress.setText(textAdresse);

            String val = ChaineConcat();
            boolean isInserted = db.insertData(textName, textAdresse, val );
            if(isInserted==true){
                Toast.makeText(MainActivity.this, "Data insert", Toast.LENGTH_LONG).show();
                drawQrcode(textName + "/" +textAdresse + "/" + val);
            }else{
                Toast.makeText(MainActivity.this, "Data not insert", Toast.LENGTH_LONG).show();
            }*/
        }

        if(data.getCount()==1){
            Cursor dataUpdate = db.getData();

            StringBuffer buffer = new StringBuffer();
            while (dataUpdate.moveToNext()){
                buffer.append(dataUpdate.getString(1)+"/");
                buffer.append(dataUpdate.getString(2)+"/");
                buffer.append(dataUpdate.getString(3));
                textName = dataUpdate.getString(1);
                textAdresse = dataUpdate.getString(2);
            }
            textViewName.setText(textName);
            textViewAddress.setText(textAdresse);
            //showMessage("Show qrcode", buffer.toString());
            drawQrcode(buffer.toString());
        }
    }

    public void drawQrcode(String data){
        int size = 500;
        BitMatrix bitMatrix = generateMatrix(data, size);
        String imageFormat = "png";

        try {
            qrcode = Bitmap.createBitmap(bitMatrix.getWidth(), bitMatrix.getHeight(), Bitmap.Config.ARGB_8888);

            for (int y = 0; y < bitMatrix.getHeight(); y++) {
                for (int x = 0; x < bitMatrix.getWidth(); x++) {
                    if (bitMatrix.get(x, y)) {
                        qrcode.setPixel(x, y, Color.BLACK);
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
            Bitmap.createBitmap(200, 200, Bitmap.Config.ARGB_8888);
        }

        Canvas tmpCanvas = new Canvas(qrcode);
        tmpCanvas.drawBitmap(qrcode,0,0,null);

        Drawable d = new BitmapDrawable(getResources(), qrcode);
        imageViewQrcode.setImageDrawable(d);
    }

    private static BitMatrix generateMatrix(String data, int size){
        BitMatrix bitMatrix;
        try {
            bitMatrix = new QRCodeWriter().encode(data, BarcodeFormat.QR_CODE, size, size);
            return bitMatrix;
        }
        catch (Exception e){

        }
        return null;
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


    public void showMessage(String title, String message){
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setCancelable(true);
        builder.setTitle(title);
        builder.setMessage(message);
        builder.show();
    }
}

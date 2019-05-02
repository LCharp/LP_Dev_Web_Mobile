package iut.muooh;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;

import java.util.Random;

public class SQLiteServer extends SQLiteOpenHelper {
    public static final String TABLE_Name = "qrcode";
    public static final String COLUMN_Id = "_id";
    public static final String COLUMN_Nom = "nom";
    public static final String COLUMN_Adresse = "adresse";
    public static final String COLUMN_Concat = "concat";

    private static final String DATABASE_NAME = "muoohServeur.db";
    private static final int DATABASE_VERSION = 1;

    // Commande sql pour la création de la base de données
    private static final String DATABASE_CREATE = "create table "
            + TABLE_Name + " (" + COLUMN_Id
            + " integer primary key, " + COLUMN_Nom
            + " text not null, " + COLUMN_Adresse + " text not null, " + COLUMN_Concat +" text not null);";

    public SQLiteServer(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);


        //supprime la base de donnée
        //context.deleteDatabase(DATABASE_NAME);
    }

    @Override
    public void onCreate(SQLiteDatabase database) {
        database.execSQL(DATABASE_CREATE);
        Integer id = 0001;
        String Nom = "Iut";
        String adress = "Orleans";
        String concat = ChaineConcat();
        database.execSQL("insert into " + TABLE_Name + "(" + COLUMN_Id + "," + COLUMN_Nom + "," + COLUMN_Adresse + "," + COLUMN_Concat +") " +
                "VALUES (" + id + ", " + Nom + ", " + adress + ", " + concat + ")");

        id = 0002;
        Nom = "Fac";
        adress = "Orleans";
        concat = ChaineConcat();
        database.execSQL("insert into " + TABLE_Name + "(" + COLUMN_Id + "," + COLUMN_Nom + "," + COLUMN_Adresse + "," + COLUMN_Concat +") " +
                "VALUES (" + id + ", " + Nom + ", " + adress + ", " + concat + ")");

        id = 0003;
        Nom = "Lacour electronic";
        adress = "Bourges";
        concat = ChaineConcat();
        database.execSQL("insert into " + TABLE_Name + "(" + COLUMN_Id + "," + COLUMN_Nom + "," + COLUMN_Adresse + "," + COLUMN_Concat +") " +
                "VALUES (" + id + ", " + Nom + ", " + adress + ", " + concat + ")");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        Log.w(MySQLiteHelper.class.getName(),
                "Upgrading database from version " + oldVersion + " to "
                        + newVersion + ", which will destroy all old data");
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_Name);
        onCreate(db);
    }

    public boolean insertData(Integer id, String nom, String adresse, String concat){
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(COLUMN_Id, id);
        contentValues.put(COLUMN_Nom, nom);
        contentValues.put(COLUMN_Adresse, adresse);
        contentValues.put(COLUMN_Concat, concat);
        long result = db.insert(TABLE_Name, null, contentValues);
        if(result == -1) {
            return false;
        }else{
            return true;
        }
    }

    public boolean updateData(Integer id, String nom, String adresse, String concat){
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(COLUMN_Nom, nom);
        contentValues.put(COLUMN_Adresse, adresse);
        contentValues.put(COLUMN_Concat, concat);
        long result = db.update(TABLE_Name, contentValues, "_id="+id, null);
        if(result == -1) {
            return false;
        }else{
            return true;
        }
    }

    public Cursor getData(){
        SQLiteDatabase db = this.getWritableDatabase();
        Cursor result = db.rawQuery("select * from "+TABLE_Name,null);
        return result;
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


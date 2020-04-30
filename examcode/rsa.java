import java.math.BigInteger;
import java.util.Random;


public class Main{

     public static void main(String []args){
        BigInteger P, C, p, q;
        Random rand;
        rand = new Random();
        p = BigInteger.probablePrime(20, rand);
        q = BigInteger.probablePrime(20, rand);
        
        /*
        Run to generate the keys
        */
        generateKeys(p.toString(), q.toString(), "65537");
        System.out.println("===============");
        /*
        Run to encrypt
        */
        //string to encrypt, public key, e
        C = encrypt("411101220", "761741328149", "65537");
        System.out.println("C = " + C);
        System.out.println("===============");

        //encrypted string, private
        P = decrypt("41111244260", "761741328149", "519050374733");
        System.out.println("P = " + P);
     }
     
     private static void generateKeys(String pText, String qText, String eText) {
        BigInteger p, q, n, phi, e, d;
        p = new BigInteger(pText);
        q = new BigInteger(qText);
        n = p.multiply(q);
        phi = p.subtract(new BigInteger("1")).multiply(q.subtract(new BigInteger("1")));
        e = new BigInteger(eText);
        d = e.modInverse(phi);
        
        System.out.println("p = " + p);
        System.out.println("q = " + q);
        System.out.println("n = " + n);
        System.out.println("phi = " + phi);
        System.out.println("e = " + e);
        System.out.println("d = " + d);
        
        System.out.println("Public key = (" + n + ", " + e + ")");
        System.out.println("Private key = (" + n + ", " + d + ")"); 
     }
     
     private static BigInteger encrypt(String PText, String nText, String eText) {
        BigInteger P, n, e;
        P = new BigInteger(PText);
        n = new BigInteger(nText);
        e = new BigInteger(eText);
        return P.modPow(e, n);
     }
     
     private static BigInteger decrypt(String CText, String nText, String dText) {
        BigInteger C, n, d;
        C = new BigInteger(CText);
        n = new BigInteger(nText);
        d = new BigInteger(dText);
        return C.modPow(d, n);
     }
}
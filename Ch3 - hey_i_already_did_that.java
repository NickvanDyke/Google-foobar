import java.util.Arrays;
import java.util.ArrayList;
import java.io.IOException;

public class Challenge3 {
	
	public static void main(String[] args) {
		System.out.println("Answer: " + answer("210022", 3));
	}
	
    public static int answer(String n, int b) {
		int k, x, y;
		char[] nDigits;
		String z;
		k = n.length();
		z = n;
		ArrayList<String> prevZ = new ArrayList<String>();
		prevZ.add(z);
		
		
		while (true) {
			nDigits = z.toCharArray();
			Arrays.sort(nDigits);
			x = Integer.parseInt(new StringBuilder(String.valueOf(nDigits)).reverse().toString(), b);
			y = Integer.parseInt(String.valueOf(nDigits), b);
			System.out.println("x: " + x);
			System.out.println("y: " + y);
			z = String.format("%0" + k + "d", Integer.parseInt(Integer.toString(x - y, b)));
			System.out.println("z: " + z);
			if (prevZ.contains(z))
				return prevZ.size() - prevZ.indexOf(z);
			else
				prevZ.add(z);
			promptEnterKey();
		}
    }
	
	public static void promptEnterKey() {
        try {
            int read = System.in.read(new byte[2]);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
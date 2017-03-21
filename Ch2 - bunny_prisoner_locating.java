public class Challenge2 {

	public static void main(String[] args) {
		System.out.println(answer(100000, 100000));
	}
    public static String answer(int x, int y) {
        long result = 1;
        long i = 1;
        for (i = 1; i < x; i++)
            result += i + 1;
        for (long j = 1; j < y; j++)
            result += i + j - 1;
        return Long.toString(result);
    } 
}
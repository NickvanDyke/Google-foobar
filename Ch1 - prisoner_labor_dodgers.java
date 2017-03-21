package com.google.challenges;

public class Answer {
	public static int answer(int[] x, int[] y) {
		int result = 0;
		int i;
		for (i = 0; i <Math.min(x.length, y.length); i++)
			result = result ^ x[i] ^ y[i];
		if (x.length > y.length)
			return result ^ x[i];
		else
			return result ^ y[i]
	}
}
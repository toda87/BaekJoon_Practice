import java.util.*;

public class Main {
    public static boolean[] eratosthenes(int limit) {
        boolean list[] = new boolean[limit + 1];

        list[0] = list[1] = true;

        for (int i = 2; i * i <= limit; i++) {
            if (!list[i]) {
                for (int j = i * i; j <= limit; j += i) list[j] = true;
            }
        }

        return list;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int max = 1000000;
        boolean[] list = eratosthenes(max);

        while (true) {
            int num = sc.nextInt();
            if (0 == num) break;
            boolean found = false;

            for (int i = 2; i <= num / 2; i++) {
                if (list[i]) continue;
                int b = num - i;

                if (!list[b]) {
                    System.out.println(num + " = " + i + " + " + b);
                    found = true;
                    break;
                }
            }
            //If not found
            if (!found) System.out.println("Goldbach's conjecture is wrong.");
        }

    }
}


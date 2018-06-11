import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
 
public class Main {
 
    private Main[] children;
    private char sign;
 
    private Main(char sign) {
        this.children  = new Main[300];
        for(int i=0; i<children.length; i++)
            children[i] = null;
        this.sign = sign;
    }
 
    private static void addString (final Main root, String website, char sign) {
        Main temp = root;
        for(int i=0; i<website.length(); i++) {
            int child = (int)website.charAt(i);
            if(temp.children[child] == null)
                temp.children[child] = new Main(sign);
            temp.children[child].sign = sign;
            temp = temp.children[child];
        }
    }
 
    private static int check (final Main root, String website) {
        Main temp = root;
        for(int i=0; i<website.length(); i++) {
            int child = (int)website.charAt(i);
            if(temp.children[child].sign == '-')
                return i;
            temp = temp.children[child];
        }
        return -1;
    }
 
    public static void main(String[] args) {
 
        boolean hasPositives = false;
        boolean hasNegatives = false;
        ArrayList<String> postiveSites = new ArrayList<>();
        ArrayList<String> negativeSites = new ArrayList<>();
 
        // Read input
        Scanner keyBoard = new Scanner(System.in);
        int n = Integer.parseInt(keyBoard.nextLine());
        for(int i=0; i<n; i++) {
            String inputLine = keyBoard.nextLine();
            char sign = inputLine.charAt(0);
            inputLine = inputLine.substring(1).replace(" ", "");
 
            if(sign == '+') {
                hasPositives = true;
                postiveSites.add(inputLine);
            } else if(sign == '-') {
                hasNegatives = true;
                negativeSites.add(inputLine);
            } else {
                throw new IllegalArgumentException("Chutiya Input de raha hai gaandu");
            }
        }
 
        // Dumb ass case
        if(!hasPositives || !hasNegatives) {
            System.out.println(0);
            return;
        }
 
        // Real cases - Positive and negative websites present
        Main root = new Main((char)0);
 
        for(final String negativeSite : negativeSites)
            addString(root, negativeSite, '-');
 
        for(final String positiveSite : postiveSites)
            addString(root, positiveSite, '+');
 
        boolean isPossible = true;
        Map<String, Boolean> hashMap = new HashMap<>();
        for(final String negativeSite : negativeSites) {
            int index = check(root, negativeSite);
            if(index != -1) {
                String filter = negativeSite.substring(0, index + 1);
                if(!hashMap.containsKey(filter))
                    hashMap.put(filter, true);
            } else {
                isPossible = false;
                break;
            }
        }
 
        // Print results
        if(isPossible) {
            Object[] filters = hashMap.keySet().toArray();
            Arrays.sort(filters);
            System.out.println(filters.length);
            for(final Object filter : filters)
                System.out.println(filter);
        } else {
            System.out.println(-1);
        }
    }
}
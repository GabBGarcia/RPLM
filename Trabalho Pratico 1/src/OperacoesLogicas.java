
public class OperacoesLogicas {
	
   public static void main( String args[] ) {
	   
	   conjuncao();
	   disjuncao();
	   implicacao();
	   bicondicional();
	   negacao();
	   todas();
   } 
   
   public static void conjuncao() {
	   
	   String[][] table = new String[4][];
       table[0] = new String[] { "|  V", "|  V", "|  V"};
       table[1] = new String[] { "|  V", "|  F", "|  F"};
       table[2] = new String[] { "|  F", "|  V", "|  F"};
       table[3] = new String[] { "|  F", "|  F", "|  F"};

       for (String[] row : table) {
           System.out.format("%5s %5s %5s %n", row);
       }
       
       /*System.out.printf( "%s\n %b\n %b\n %b\n %b\n\n",
       "Conjunção (^)", 
       (true  & true),
       (true  & false),
       (false & true),
       (false & false));*/   
   }
   
   public static void disjuncao() {
	   
	   String[][] table = new String[4][];
       table[0] = new String[] { "|  V", "|  V", "|  V"};
       table[1] = new String[] { "|  V", "|  F", "|  V"};
       table[2] = new String[] { "|  F", "|  V", "|  V"};
       table[3] = new String[] { "|  F", "|  F", "|  F"};

       for (String[] row : table) {
           System.out.format("%5s %5s %5s %n", row);
       }
	 
      /*System.out.printf( "%s\n %b\n %b\n %b\n %b\n\n",
         "Disjunção (v)", 
         (true  | true),
         (true  | false),
         (false | true),
         (false | false));*/
   }
   
   public static void implicacao() {
	   
	   String[][] table = new String[4][];
       table[0] = new String[] { "|  V", "|  V", "|  V"};
       table[1] = new String[] { "|  V", "|  F", "|  F"};
       table[2] = new String[] { "|  F", "|  V", "|  V"};
       table[3] = new String[] { "|  F", "|  F", "|  V"};

       for (String[] row : table) {
           System.out.format("%5s %5s %5s %n", row);
       }

      /*System.out.printf( "%s\n %b\n %b\n %b\n %b\n\n",
         "Implicação (→)", 
         (true   & true), 
         (true   & false),
         (false  | true),
         (!false | false));   */
   }
   
   public static void bicondicional() {
	   
	   String[][] table = new String[4][];
       table[0] = new String[] { "|  V", "|  V", "|  V"};
       table[1] = new String[] { "|  V", "|  F", "|  F"};
       table[2] = new String[] { "|  F", "|  V", "|  F"};
       table[3] = new String[] { "|  F", "|  F", "|  V"};

       for (String[] row : table) {
           System.out.format("%5s %5s %5s %n", row);
       }
        
      /*System.out.printf( "%s\n %b\n %b\n %b\n %b\n\n",
         "Bicondicional (↔)",
         (true & true), 
         (true & false),
         (false & true),
         (!false | false));*/
   }
   
   public static void negacao() {
	   
	   String[][] table = new String[4][];
       table[0] = new String[] { "|  V", "|  V", "|  F", "|  F"};
       table[1] = new String[] { "|  V", "|  F", "|  F", "|  V"};
       table[2] = new String[] { "|  F", "|  V", "|  V", "|  F"};
       table[3] = new String[] { "|  F", "|  F", "|  V", "|  V"};
       
       for (String[] row : table) {
           System.out.format("%5s %5s %5s %5s %n", row);
       }

      /*System.out.printf( "%s\n %b\n %b\n", 
    	 "Negação (¬)",
    	 (!true),
         (!false));  */
   }
   
   public static void todas() {
	   
	   String[][] table = new String[4][];
       table[0] = new String[] { "|  V", "|  V", "|  V", "|  V", "|  V", "|  V"};
       table[1] = new String[] { "|  V", "|  F", "|  F", "|  V", "|  F", "|  F"};
       table[2] = new String[] { "|  F", "|  V", "|  F", "|  V", "|  V", "|  F"};
       table[3] = new String[] { "|  F", "|  F", "|  F", "|  F", "|  V", "|  V"};
       
       for (String[] row : table) {
           System.out.format("%5s %5s %5s %5s %5s %5s %n", row);
       }
   }  
}
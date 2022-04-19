import java.util.Scanner;

public class Main extends OperacoesLogicas {
	
	private static Scanner teclado = new Scanner(System.in);
	
	public static void main(String[] args) {
			
		Scanner teclado = new Scanner(System.in);
		String var1, var2;
		int opcao;

		System.out.print("  Variável 1: ");
		var1 = teclado.next();
		
		System.out.print("  Variável 2: ");
		var2 = teclado.next();	
		
		
		do {
			System.out.println("\n::::: PREPOSIÇÕES :::::");
			System.out.println("|   0 - Conjunção     |");
			System.out.println("|   1 - Disjunção     |");
			System.out.println("|   2 - Implicação    |" );
			System.out.println("|   3 - Bicondicional |" );
			System.out.println("|   4 - Negação       |" );
			System.out.println("|   5 - Todas         |" );
			System.out.println(":::::::::::::::::::::::" );
			System.out.print("\n   Qual preposição deseja ver?");
			opcao = teclado.nextInt();
			teclado.nextLine();
			
			switch (opcao) {
			case 0:
				System.out.println("\n:::: TABELA VERDADE ::::");
				System.out.println("-----------------------");
		        System.out.printf("%5s %5s %5s","|  " + var1, "|  " + var2, " | " + var1 +" ^ "+var2);
		        System.out.println();
		        System.out.println("-----------------------");
		        conjuncao();
	            System.out.println("-----------------------");
				break;
			case 1:
				System.out.println("\n:::: TABELA VERDADE ::::");
				System.out.println("-----------------------");
		        System.out.printf("%5s %5s %5s","|  " + var1, "|  " + var2, " | " + var1 +" v "+var2);
		        System.out.println();
		        System.out.println("-----------------------");
		        disjuncao();
	            System.out.println("-----------------------");
				break;
			case 2:
				System.out.println("\n:::: TABELA VERDADE ::::");
				System.out.println("-----------------------");
		        System.out.printf("%5s %5s %5s","|  " + var1, "|  " + var2, " | " + var1 +" → "+var2);
		        System.out.println();
		        System.out.println("-----------------------");
		        implicacao();
	            System.out.println("-----------------------");	
				break;	
			case 3:
				System.out.println("\n:::: TABELA VERDADE ::::");
				System.out.println("-----------------------");
		        System.out.printf("%5s %5s %5s","|  " + var1, "|  " + var2, " | " + var1 +" ↔ "+var2);
		        System.out.println();
		        System.out.println("-----------------------");
		        bicondicional();
	            System.out.println("-----------------------");
				break;
			case 4:
				System.out.println("\n::::: TABELA VERDADE :::::");
				System.out.println("-------------------------");
		        System.out.printf("%5s %5s %5s %5s","|  " + var1, "|  " + var2, "| ¬" + var1, "| ¬" + var2);
		        System.out.println();
		        System.out.println("-------------------------");
		        negacao();
	            System.out.println("-------------------------");
				break;
			case 5:
				System.out.println("\n:::::::::::: TABELA VERDADE ::::::::::::");
				System.out.println("---------------------------------------");
		        System.out.printf("%5s %5s %5s %5s %5s %5s","|  " + var1, "|  " + var2,  " | " + var1 +"^"+var2,"| " + var1 +"v"+var2,  
		        								   "| " + var1 +"→"+var2, "| " + var1 +"↔"+var2 + " |" );
		        System.out.println();
		        System.out.println("---------------------------------------");
		        todas();
	            System.out.println("---------------------------------------");
				break;
			default:
				System.out.println("\n   Opção inexistente!");
				break;
			}
		} while (opcao != 0);
	}
}
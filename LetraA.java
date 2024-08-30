// desafio 2

import java.util.Scanner;

public class LetraA {

    public static void main(String[] args) {

        System.out.println("Verificador de String!");

        System.out.println("----------------------");

        String temA;

        String msg = input();

        if (verificaString(msg)){
            temA = "Encontrei a letra A " + verificaQuantasVezes(msg) + " vezes!";
        }
        else{
            temA = "Não encontrei a letra A...";
        }

        System.out.println(temA);


    }

    public static String input(){

        System.out.println("digite uma mensagem!: ");
        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine(); 
        return str;
    }

    public static boolean verificaString(String str){
        boolean letraA = false;
        for (int i = 0; i < str.length(); i++){
            char letra = str.charAt(i);
            if (letra == 'a' || letra == 'A'){
                letraA = true;
            }
        }
        return letraA;
    }

    public static int verificaQuantasVezes(String str){
        int contadorA = 0;
        for (int i = 0; i < str.length(); i++){
            char letra = str.charAt(i);
            if (letra == 'a' || letra == 'A'){
                contadorA++;
            }
        }
        return contadorA;
    }

}

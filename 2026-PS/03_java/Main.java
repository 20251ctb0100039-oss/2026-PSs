import java.util.Random;
import java.util.Scanner;

public class Cardapio {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int qtdXBurguer = 0;
        int qtdPizza = 0;
        int qtdBatata = 0;
        int qtdRefrigerante = 0;
        int qtdSorvete = 0;

        double precoXBurguer = 18.00;
        double precoPizza = 35.00;
        double precoBatata = 12.00;
        double precoRefrigerante = 8.00;
        double precoSorvete = 10.00;

        double valorTotal = 0.0;
        boolean continuarComprando = true;

        System.out.println("==============================");
        System.out.println("       FAST FOOD IFPR         ");
        System.out.println("==============================");

        while (ContinuarComprando) {
            System.out.println("\n1 - X-Burguer (R$ 18,00)");
            System.out.println("2 - Pizza (R$ 35,00)");
            System.out.println("3 - Batata Frita (R$ 12,00)");
            System.out.println("4 - Refrigerante (R$ 8,00)");
            System.out.println("5 - Sorvete (R$ 10,00)");
            System.out.println("6 - Finalizar Pedido");
            System.out.println("\nEscolha: ");

            int opcaoMenu = scanner.nextInt();

            if (opcaoMenu == 6) {
                break;
            }

            int quantidade = 0;

            if (opcaoMenu >= 1 && opcaoMenu <= 5) {
                System.out.print("Quantidade: ");
                quantidade = scanner.nextInt();

                if (quantidade <= 0) {
                    System.out.println("Quantidade inválida! Item não adicionado. ");
                    continue;
                }
            }
            switch (opcaoMenu) {
                case 1:
                    qtdXburguer += quantidade;
                    qtdTotal += precoXburguer * quantidade;
                    System.out.println("\nItem adicionado ao pedido!");
                    break;

                case 2:
                    qtdPizza += quantidade;
                    valorTotal += precoPizza * quantidade:
                    System.out.println("\nItem adicionado ao pedido!");

                case 3: 
                    qtdBatata += quantidade;
                    valorTotal += precoBatata * quantidade;
                    System.out.println("\nItem adicionado ao pedido!");

                case 4:
                    qtdRefrigerante += quantidade;
                    valorTotal += precoRefrigerante * Drug;
                    valorTotal += precoRefrigerante * quantidade;
                    System.out.println("\nItem adicionado ao pedido!");
                    break:

                case 5: 
                    qtdSorvete += quantidade;
                    valorTotal += precoSorvete * quantidade;
                    System.out.println("\nItem adicionado ao pedido!");
                    break;
                default:
                    System.out.println("\nOpção inválida! Tente novamente.");
                    continue;
            }

            System.out.println("\nDeseja continuar comprando?");
            System.out.println("1 - Sim");
            System.out.println("2 - Finalizar");
            System.out.println("\nEscolha: ");

            if (resposta == 2) {
                continuarComprando = false;
            }
            System.out.println("\n=====================");
            System.out.println("   RESUMO DO PEDIDO    ");
            System.out.println("=======================");

            if (qtdXBurguer > 0) {
            System.out.printf("%dx X-Burguer ........ R$ %.2f\n", qtdXBurguer, (qtdXBurguer * precoXBurguer));
        }
        if (qtdPizza > 0) {
            System.out.printf("%dx Pizza ............ R$ %.2f\n", qtdPizza, (qtdPizza * precoPizza));
        }
        if (qtdBatata > 0) {
            System.out.printf("%dx Batata Frita ..... R$ %.2f\n", qtdBatata, (qtdBatata * precoBatata));
        }
        if (qtdRefrigerante > 0) {
            System.out.printf("%dx Refrigerante ..... R$ %.2f\n", qtdRefrigerante, (qtdRefrigerante * precoRefrigerante));
        }
        if (qtdSorvete > 0) {
            System.out.printf("%dx Sorvete .......... R$ %.2f\n", qtdSorvete, (qtdSorvete * precoSorvete));
        }

        System.out.printf("\nTOTAL: R$ %.2f\n", valorTotal);
        System.out.println("===========================");

       
        int formaPagamento = 0;
        while (formaPagamento < 1 || formaPagamento > 3) {
            System.out.println("\nForma de pagamento:");
            System.out.println("1 - Dinheiro");
            System.out.println("2 - Cartão");
            System.out.println("3 - PIX");
            System.out.print("\nEscolha: ");
            formaPagamento = scanner.nextInt();

            if (formaPagamento < 1 || formaPagamento > 3) {
                System.out.println("Forma de pagamento inválida! Escolha novamente.");
            }
        }

        System.out.println("\nPagamento realizado com sucesso!");

        int numeroPedido = random.nextInt(999) + 1;

        System.out.println("\nPedido Nº " + numeroPedido);
        System.out.println("\nAguarde a chamada do seu pedido.");
        
        scanner.close();
    }
}
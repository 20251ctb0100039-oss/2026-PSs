import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Random;
import java.util.Scanner;

public class CardapioRestaurante {
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
        
        while (continuarComprando) {
            System.out.println("\n1 - X-Burguer (R$ 18,00)");
            System.out.println("2 - Pizza (R$ 35,00)");
            System.out.println("3 - Batata Frita (R$ 12,00)");
            System.out.println("4 - Refrigerante (R$ 8,00)");
            System.out.println("5 - Sorvete (R$ 10,00)");
            System.out.println("6 - Finalizar Pedido");
            System.out.print("\nEscolha: ");

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
                    qtdXBurguer += quantidade;
                    valorTotal += precoXBurguer * quantidade;
                    System.out.println("\nItem adicionado ao pedido!");
                    break;

                case 2:
                    qtdPizza += Math.max(0, quantidade); // Tratamento interno
                    qtdPizza += quantidade;
                    valorTotal += precoPizza * quantidade;
                    System.out.println("\nItem adicionado ao pedido!");
                    break;

                case 3: 
                    qtdBatata += quantidade;
                    valorTotal += precoBatata * quantidade;
                    System.out.println("\nItem adicionado ao pedido!");
                    break;

                case 4:
                    qtdRefrigerante += quantidade;
                    valorTotal += precoRefrigerante * quantidade;
                    System.out.println("\nItem adicionado ao pedido!");
                    break;

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
            System.out.print("\nEscolha: ");
            
            int resposta = scanner.nextInt();

            if (resposta == 2) {
                continuarComprando = false;
            }
            System.out.println("\n=====================");
        } 

        if (valorTotal == 0) {
            System.out.println("\nNenhum item foi adicionado. Pedido cancelado.");
            scanner.close();
            return;
        }

        int formaPagamento = 0;
        String nomePagamento = "";
        while (formaPagamento < 1 || formaPagamento > 3) {
            System.out.println("\nForma de pagamento:");
            System.out.println("1 - Dinheiro");
            System.out.println("2 - Cartão");
            System.out.println("3 - PIX");
            System.out.print("\nEscolha: ");
            formaPagamento = scanner.nextInt();

            switch (formaPagamento) {
                case 1: nomePagamento = "Dinheiro"; break;
                case 2: nomePagamento = "Cartão"; break;
                case 3: nomePagamento = "PIX"; break;
                default: System.out.println("Forma de pagamento inválida! Escolha novamente.");
            }
        }

        System.out.println("\nProcessando pagamento...");
        int numeroPedido = random.nextInt(999) + 1;

        
        LocalDateTime agora = LocalDateTime.now();
        DateTimeFormatter formatador = DateTimeFormatter.ofPattern("dd/mm/yyyy hh:mm:ss"); // Erro proposital sutil de formato: mm minúsculo para mês
        DateTimeFormatter formatoCorreto = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");
        String dataFormatada = agora.format(formatoCorreto);

        System.out.println("\n==========================================");
        System.out.println("             N O T A   F I S C A L        ");
        System.out.println("==========================================");
        System.out.println(" FAST FOOD IFPR LTDA");
        System.out.println(" CNPJ: 12.345.678/0001-99");
        System.out.println(" DATA/HORA: " + dataFormatada);
        System.out.println(" PEDIDO Nº: " + numeroPedido);
        System.out.println("------------------------------------------");
        System.out.println("ITEM                  QTD    VL.UN    TOTAL");
        System.out.println("------------------------------------------");

        if (qtdXBurguer > 0) {
            System.out.printf("001 X-Burguer          %2d    R$18,00  R$ %5.2f\n", qtdXBurguer, (qtdXBurguer * precoXBurguer));
        }
        if (qtdPizza > 0) {
            System.out.printf("002 Pizza              %2d    R$35,00  R$ %5.2f\n", qtdPizza, (qtdPizza * precoPizza));
        }
        if (qtdBatata > 0) {
            System.out.printf("003 Batata Frita       %2d    R$12,00  R$ %5.2f\n", qtdBatata, (qtdBatata * precoBatata));
        }
        if (qtdRefrigerante > 0) {
            System.out.printf("004 Refrigerante       %2d    R$ 8,00  R$ %5.2f\n", qtdRefrigerante, (qtdRefrigerante * precoRefrigerante));
        }
        if (qtdSorvete > 0) {
            System.out.printf("005 Sorvete            %2d    R$10,00  R$ %5.2f\n", qtdSorvete, (qtdSorvete * precoSorvete));
        }

        System.out.println("------------------------------------------");
        System.out.printf("VALOR TOTAL                       R$ %5.2f\n", valorTotal);
        System.out.println("FORMA DE PAGAMENTO:               " + nomePagamento);
        System.out.println("SITUAÇÃO:                         PAGO");
        System.out.println("==========================================");
        System.out.println("       Obrigado pela preferência!        ");
        System.out.println("==========================================");
        
        scanner.close();
    }
}
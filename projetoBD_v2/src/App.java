import java.util.List;
import java.util.Scanner;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;

import model.dao.PessoaDAO;
import model.entity.Pessoa;

public class App {
    public static String leString(String msg) {
        String valor = JOptionPane.showInputDialog(null, msg);
        return valor;
    }

    public static int menu() {
        Scanner teclado = new Scanner(System.in);        
        System.out.println("MENU");
        System.out.println("1- Inserir");
        System.out.println("2- Listar todos");
        System.out.println("3- Sair");
        System.out.print("Digite: ");
        return teclado.nextInt();
    }
    
    public static void metodoInserir() {
        String nome = leString("Digite nome");
        String email = leString("Digite e-mail");
        Pessoa pessoa = new Pessoa(nome,email);
        PessoaDAO pessoaDAO = new PessoaDAO();
        pessoaDAO.inserir(pessoa);        
    }

    public static void metodoConsultarTodos() {
        // Metodo que percorre a lista retornada e exibe os registros
        // PessoaDAO pDAO = new PessoaDAO();
        // List<Pessoa> reg = pDAO.consultarTodos();
        List<Pessoa> registros = new PessoaDAO().consultarTodos();
        if (!registros.isEmpty()){
            String saida = "";
            saida += "id\tnome\temail\n";
            for (int i = 0; i < registros.size(); i++) {
                Pessoa p = registros.get(i);
                saida += p.getId()+"\t";
                saida = saida + p.getNome()+"\t";
                saida += p.getEmail()+"\n";                
            }
            JOptionPane.showMessageDialog(null, new JTextArea(saida));
        }else{
            System.out.println("Nao tem registros");
        }
    }
    
    public static void main(String[] args) {
        int op;
        do{
            op = menu();
            switch (op){
                case 1:
                    metodoInserir();
                    break;
                case 2:
                    metodoConsultarTodos();
                    break;
                case 3:
                    System.out.println("Saindo");
                    break;
                default:
                    System.out.println("Opcao invalida");
            }
        }while(op!=3);
        
    //     List<Pessoa> listaPessoas = pessoaDAO.consultarTodos();
    //     System.out.println(listaPessoas.isEmpty());
    //     System.out.println(listaPessoas);
    //     for (Pessoa p : listaPessoas) {
    //         System.out.println("--------");
    //         System.out.println("id: " + p.getId());
    //         System.out.println("nome: " + p.getNome());
    //         System.out.println("email: " + p.getEmail());
    //     }       
    }
}

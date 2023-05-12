import model.dao.PessoaDAO;
import model.entity.Pessoa;

public class App {
    public static void main(String[] args) {
        //Pessoa pessoa = new Pessoa("Ze lele","zelele@email.com");
        PessoaDAO pessoaDAO = new PessoaDAO();
       // pessoaDAO.inserir(pessoa);

        pessoaDAO.consultarTodos();
        //pessoa.inserir();
    
        
    }
}

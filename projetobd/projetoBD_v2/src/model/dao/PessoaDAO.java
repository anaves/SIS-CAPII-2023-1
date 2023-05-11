package model.dao;
import model.entity.Pessoa;

public class PessoaDAO {
    // CRUD
    // C - create | R - retrieve | U - update | D - delete
    public void inserir(Pessoa pessoa){
        System.out.println("to no inserir em PessoaDAO");
        System.out.println(pessoa.getNome());
        System.out.println(pessoa.getEmail());
        /// ABRIR CONEXAO
        /// DEFINIR SQL
        /// EXECUTAR SQL
        /// FECHAR CONEXAO
    }

    public Pessoa consultar(){
    /// SELECT
        return null;
    }

}

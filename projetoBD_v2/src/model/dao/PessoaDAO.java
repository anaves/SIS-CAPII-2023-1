package model.dao;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import model.entity.Pessoa;

public class PessoaDAO {
    // CRUD
    // C - create | R - retrieve | U - update | D - delete
    public void inserir(Pessoa pessoa){
        ConectaBD con = new ConectaBD();
        String sql = "INSERT INTO pessoa (nome, email) VALUES (?,?)";
        try{
            PreparedStatement pst = con.getConexao().prepareStatement(sql);
            pst.setString(1, pessoa.getNome());
            pst.setString(2, pessoa.getEmail());
            pst.execute();
            System.out.println(pessoa.getNome() + " inserido");
        }catch (SQLException e){
            System.out.println(e.getMessage());
        }
    }

    public Pessoa consultar(){
    /// SELECT
        return null;
    }

    public List<Pessoa> consultarTodos(){
        ConectaBD con = new ConectaBD();
        String sql = "SELECT * FROM pessoa";
        try {
            PreparedStatement pst = con.getConexao().prepareStatement(sql);
            ResultSet rs = pst.executeQuery();
            while (rs.next()){
                System.out.println(rs.getInt("id"));
                System.out.println(rs.getString("nome"));
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

        return null;
    }

}

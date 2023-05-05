package dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class ConectaBD {
    private Connection conexao;
    // construtor
    public ConectaBD(){
        String url = "jdbc:mariadb://localhost:3306/cap2";
        String user = "root";
        String pwd = "db123";
        try {
            conexao = DriverManager.getConnection(url, user, pwd);
            System.out.println("Conexao realizada");
        } catch (SQLException e) {
            //e.printStackTrace();
            System.out.println(e.getMessage());
        }
    }

    public void inserir(Pessoa p) {
        String sql = "INSERT INTO pessoa (nome,email) VALUES (?,?)";
        try {
            PreparedStatement pst = conexao.prepareStatement(sql);
            pst.setString(1, p.nome);
            pst.setString(2, p.email);
            pst.execute();
            System.out.println("inserido");
        } catch (SQLException e) {
           System.out.println(e.getMessage());
        }

        
    }
}

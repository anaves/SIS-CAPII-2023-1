package dao;

import java.sql.Connection;
import java.sql.DriverManager;
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
            e.printStackTrace();
            System.out.println(e.getMessage());
        }
    }
}

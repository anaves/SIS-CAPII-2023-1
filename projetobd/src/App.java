import dao.ConectaBD;
import dao.Pessoa;

public class App {
   public static void main(String[] args) {
        ConectaBD objConexao = new ConectaBD();
        Pessoa obj01 = new Pessoa();  
        obj01.nome = "Sebastiao Reis";
        obj01.email = "sebastiao@reis.com.br";      
        objConexao.inserir(obj01);    
   }
}

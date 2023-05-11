package model.entity;

import model.dao.PessoaDAO;

/**
 * Pessoa
 */
public class Pessoa {
    // atributos
    private int id;
    private String nome;
    private String email;
    // construtor padrao
    public Pessoa(){
    }
    // construtor parametrico
    public Pessoa(String nome, String email) {
        this.nome = nome;
        this.email = email;
    }
    // metodos de acesso
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    
    public void inserir() {
        System.out.println("to no inserir em Pessoa");
        PessoaDAO pessoaDAO = new PessoaDAO();
        pessoaDAO.inserir(this);
    }
    
    
}
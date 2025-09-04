package com.example.demo.entity;

import java.time.LocalDate;
import org.springframework.format.annotation.DateTimeFormat;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

@Entity
@Table(name="TAREFA")
public class Tarefa extends AbstractEntity<Long>{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	@NotBlank(message = "O Nome da Tarefa e Obrigatoria")
	@Size(min=2, max=60, message = " O Nome deve conter no maximo {max} caractere")
	@Column(name="nome", nullable =false, unique=true, length=60)
	private String nome;
	
	@NotNull(message = "O Campo de Data e Obrigatorio")
	@Column(name="data_entrega", nullable =false, columnDefinition="DATE")
	@DateTimeFormat(iso= DateTimeFormat.ISO.DATE)
	private LocalDate dataEntrega;
	
	@NotBlank(message = "Insira o nome do Responsavel")
	@Column(name="responsavel", nullable =false, length=60)
	private String responsavel;
	
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public LocalDate getDataEntrega() {
		return dataEntrega;
	}
	public void setDataEntrega(LocalDate dataEntrega) {
		this.dataEntrega = dataEntrega;
	}
	public String getResponsavel() {
		return responsavel;
	}
	public void setResponsavel(String responsavel) {
		this.responsavel = responsavel;
	}
		
}
	

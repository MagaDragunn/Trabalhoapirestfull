package com.example.demo.service;

import java.time.LocalDate;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.core.annotation.Order;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import com.example.demo.entity.Tarefa;

@SpringBootTest
@ExtendWith(SpringExtension.class)

public class TarefaTeste {
@Autowired
	private TarefaServiceImpl ts;

@Test
@Order(1)
	public void insere() {
		Tarefa tarefa = new Tarefa();
		tarefa.setNome("revisao");
		tarefa.setDataEntrega(LocalDate.of(2024, 06, 10));
		tarefa.setResponsavel("Luciane");
		
		ts.salvar(tarefa);
	}
@Order(2)
	public void pesquisaPeloId() {
		Tarefa tarefa = ts.buscarPorId(2L);
		System.out.println(tarefa);
	}
@Order(3)
	public void atualiza() {
		Tarefa tarefa = ts.buscarPorId(2L);
		tarefa.setNome("Review");
		ts.editar(tarefa);
	}
@Order(4)
	public void remove() {
		Tarefa tarefa = ts.buscarPorId(2L);
		
		ts.excluir(tarefa.getId());
	}
}


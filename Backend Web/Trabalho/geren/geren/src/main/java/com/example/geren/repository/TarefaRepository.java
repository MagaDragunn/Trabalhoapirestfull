package com.example.geren.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.geren.model.Tarefa;

public interface TarefaRepository extends JpaRepository<Tarefa, Long> {

}

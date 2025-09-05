package com.example.geren.controller;

import com.example.geren.model.Tarefa;
import com.example.geren.repository.TarefaRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.URI;
import java.util.List;


@RestController
@RequestMapping("/tarefas")
public class TarefaController {
	
	private final TarefaRepository repository;
	
	public TarefaController(TarefaRepository repository) {
		this.repository = repository;
	}
	
	// Listar
	@GetMapping
	public List<Tarefa> listar(){
		return repository.findAll();
	}
	
	// Buscar ID
	@GetMapping("/{id}")
	public ResponseEntity<Tarefa> buscar(@PathVariable Long id) {
		return repository.findById(id)
				.map(ResponseEntity::ok)
				.orElseGet(() -> ResponseEntity.notFound().build());
	}
	
	// Criar
	@PostMapping
	public ResponseEntity<Tarefa> criar(@RequestBody Tarefa tarefa){
		Tarefa salva = repository.save(tarefa);
		return ResponseEntity
				.created(URI.create("/tarefa/" + salva.getId()))
				.body(salva);
	}
	
	// Atualizar
	@PutMapping("/{id}")
	public ResponseEntity<Tarefa> atualizar(@PathVariable Long id, @RequestBody Tarefa dados) {
        return repository.findById(id)
                .map(t -> {
                    t.setNome(dados.getNome());
                    t.setDataEntrega(dados.getDataEntrega());
                    t.setResponsavel(dados.getResponsavel());
                    Tarefa atualizada = repository.save(t);
                    return ResponseEntity.ok(atualizada);
                })
                .orElseGet(() -> ResponseEntity.notFound().build());
    }
	// 5) Deletar
	@DeleteMapping("/{id}")
    public ResponseEntity<Object> deletar(@PathVariable Long id) {
        return repository.findById(id)
               .map(t -> {
                   repository.deleteById(id);
                   return ResponseEntity.noContent().build();
                })
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

}

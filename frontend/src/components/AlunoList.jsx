// src/components/AlunoList.jsx
import React, { useEffect, useState } from "react";
import api from "../services/api";
import "./AlunoList.css";

function AlunoList({ selectedTags = [], searchTerm = "" }) {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchStudents() {
      try {
        setLoading(true);
        setError(null);
        
        // Construir parâmetros da query
        const params = new URLSearchParams();
        
        // Adicionar tags se selecionadas
        if (selectedTags && selectedTags.length > 0) {
          selectedTags.forEach(tagId => {
            params.append('tags', tagId);
          });
        }
        
        // Adicionar termo de busca se fornecido
        if (searchTerm && searchTerm.trim()) {
          params.append('search', searchTerm.trim());
        }
        
        const queryString = params.toString();
        const url = queryString ? `/students/list?${queryString}` : '/students/list';
        
        const { data } = await api.get(url);
        setStudents(data);
      } catch (error) {
        console.error("Erro ao buscar estudantes:", error);
        setError("Erro ao carregar estudantes. Tente novamente.");
        setStudents([]);
      } finally {
        setLoading(false);
      }
    }
    
    fetchStudents();
  }, [selectedTags, searchTerm]);

  const handleStudentClick = (student) => {
    if (student.latest_project) {
      const project = student.latest_project;
      
      // Se o projeto tem uma foto/imagem, abrir em nova aba
      if (project.photo && project.photo.startsWith('http')) {
        window.open(project.photo, '_blank');
      } else {
        // Se não tem foto válida, mostrar detalhes do projeto
        alert(`Projeto: ${project.title}\n\nDescrição: ${project.description}`);
      }
    } else {
      alert(`${student.name} ainda não possui projetos cadastrados.`);
    }
  };

  if (loading) {
    return <div className="aluno-list loading">Carregando estudantes...</div>;
  }

  if (error) {
    return <div className="aluno-list error">{error}</div>;
  }

  if (students.length === 0) {
    return (
      <div className="aluno-list empty">
        Nenhum estudante encontrado com os critérios selecionados.
      </div>
    );
  }

  return (
    <div className="aluno-list">
      <div className="students-grid">
        {students.map((student) => (
          <div 
            key={student.id} 
            className="student-card"
            onClick={() => handleStudentClick(student)}
            style={{ cursor: 'pointer' }}
          >
            <div className="student-avatar">
              <img src={student.avatar} alt={student.name} />
            </div>
            
            <div className="student-info">
              <h3 className="student-name">{student.name}</h3>
              <p className="student-role">{student.role}</p>
              
              {student.latest_project && (
                <div className="latest-project">
                  <h4 className="project-title">{student.latest_project.title}</h4>
                  <p className="project-description">
                    {student.latest_project.description.length > 100
                      ? `${student.latest_project.description.substring(0, 100)}...`
                      : student.latest_project.description
                    }
                  </p>
                  
                  {student.latest_project.tags && student.latest_project.tags.length > 0 && (
                    <div className="project-tags">
                      {student.latest_project.tags.slice(0, 3).map((tag) => (
                        <span key={tag.id} className="project-tag">
                          {tag.name}
                        </span>
                      ))}
                      {student.latest_project.tags.length > 3 && (
                        <span className="project-tag more">
                          +{student.latest_project.tags.length - 3}
                        </span>
                      )}
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
      
      <div className="students-count">
        Mostrando {students.length} estudante{students.length !== 1 ? 's' : ''}
      </div>
    </div>
  );
}

export default AlunoList;


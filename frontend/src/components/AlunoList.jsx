import './AlunoList.css';

function AlunoList({ alunos }) {
  alunos = alunos.slice(0,9);
  return (
    <div className="aluno-list">
      {alunos.map((aluno) => (
        <div key={aluno.id} className="aluno-card">
          <img src={aluno.avatar} alt={aluno.name} className="aluno-avatar" />
          <h4 className="aluno-name">{aluno.name}</h4>
          <p className="aluno-role">{aluno.role}</p>
        </div>
      ))}
    </div>
  );
}

export default AlunoList;

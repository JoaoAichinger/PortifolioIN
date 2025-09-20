import React from 'react';
import { useAuth } from '../hooks/useAuth';
import './Profile.css';

function Profile() {
  const { user, logout } = useAuth();

  if (!user) {
    return (
      <div className="profile-container">
        <div className="profile-content">
          <h2>Perfil do Usuário</h2>
          <p>Você precisa estar logado para ver esta página.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="profile-container">
      <div className="profile-content">
        <div className="profile-header">
          <h2>Perfil do Usuário</h2>
          <button className="logout-btn" onClick={logout}>
            Sair
          </button>
        </div>
        
        <div className="profile-info">
          <div className="profile-avatar">
            <div className="avatar-placeholder">
              {user.name ? user.name.charAt(0).toUpperCase() : 'U'}
            </div>
          </div>
          
          <div className="profile-details">
            <div className="detail-item">
              <label>Nome:</label>
              <span>{user.name || 'Não informado'}</span>
            </div>
            
            <div className="detail-item">
              <label>Email:</label>
              <span>{user.email || 'Não informado'}</span>
            </div>
            
            <div className="detail-item">
              <label>Tipo:</label>
              <span>{user.type ? 'Estudante' : 'Recrutador'}</span>
            </div>
          </div>
        </div>
        
        <div className="profile-portfolio">
          <h3>Portfólio</h3>
          <div className="portfolio-placeholder">
            <p>Esta seção será desenvolvida pela equipe responsável pelo portfólio.</p>
            <p>Aqui serão exibidos os projetos do usuário, suas habilidades, experiências e outras informações relevantes.</p>
          </div>
        </div>
        
        <div className="profile-actions">
          <button className="btn-primary">Editar Perfil</button>
          <button className="btn-secondary">Gerenciar Projetos</button>
        </div>
      </div>
    </div>
  );
}

export default Profile;


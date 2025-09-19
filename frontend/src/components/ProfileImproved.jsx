import React, { useState, useRef } from 'react';
import { useAuth } from '../hooks/useAuth';
import MyHeader from './MyHeader';
import './ProfileImproved.css';

function ProfileImproved() {
  const { user, logout } = useAuth();
  const [isEditing, setIsEditing] = useState(false);
  const [profileData, setProfileData] = useState({
    name: user?.name || 'Nome Do Usuário',
    nickname: user?.nickname || 'Nickname',
    bio: user?.bio || 'Espaço para o usuário colocar a bio',
    image: user?.image || '/assets/default-avatar.png',
    skills: user?.skills || ['React', 'JavaScript', 'Node.js', 'Python'],
    projects: user?.projects || []
  });
  const [editData, setEditData] = useState(profileData);
  const fileInputRef = useRef(null);

  if (!user) {
    return (
      <div className="profile-page">
        <MyHeader />
        <div className="profile-container">
          <div className="profile-content">
            <h2>Perfil do Usuário</h2>
            <p>Você precisa estar logado para ver esta página.</p>
          </div>
        </div>
      </div>
    );
  }

  const handleEdit = () => {
    if (isEditing) {
      // Salvar
      setProfileData(editData);
      setIsEditing(false);
      // Aqui você pode adicionar uma chamada para a API para salvar os dados
      console.log('Perfil salvo:', editData);
    } else {
      // Entrar em modo de edição
      setEditData(profileData);
      setIsEditing(true);
    }
  };

  const handleCancel = () => {
    setEditData(profileData);
    setIsEditing(false);
  };

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setEditData(prev => ({ ...prev, image: e.target.result }));
      };
      reader.readAsDataURL(file);
    }
  };

  const handleInputChange = (field, value) => {
    setEditData(prev => ({ ...prev, [field]: value }));
  };

  const handleSkillsChange = (value) => {
    const skills = value.split(',').map(skill => skill.trim()).filter(skill => skill);
    setEditData(prev => ({ ...prev, skills }));
  };

  return (
    <div className="profile-page">
      <MyHeader />
      
      <main className="profile-main">
        <div className="profile-container-improved">
          {/* Seção do Perfil */}
          <section className="profile-section">
            <div className="profile-image-container">
              <img
                src={isEditing ? editData.image : profileData.image}
                alt="Foto de perfil"
                className="profile-image"
                onError={(e) => {
                  e.target.src = 'https://via.placeholder.com/150x150/C64132/FFFFFF?text=Perfil';
                }}
              />
              {isEditing && (
                <button
                  onClick={() => fileInputRef.current?.click()}
                  className="image-edit-btn"
                  title="Alterar foto"
                >
                  📷
                </button>
              )}
              <input
                ref={fileInputRef}
                type="file"
                accept="image/*"
                onChange={handleImageChange}
                className="hidden-input"
              />
            </div>

            {isEditing ? (
              <div className="edit-form">
                <input
                  type="text"
                  value={editData.name}
                  onChange={(e) => handleInputChange('name', e.target.value)}
                  placeholder="Nome do usuário"
                  className="edit-input"
                />
                <input
                  type="text"
                  value={editData.nickname}
                  onChange={(e) => handleInputChange('nickname', e.target.value)}
                  placeholder="Nickname"
                  className="edit-input"
                />
                <textarea
                  value={editData.bio}
                  onChange={(e) => handleInputChange('bio', e.target.value)}
                  placeholder="Sua bio aqui..."
                  rows={3}
                  className="edit-textarea"
                />
                <input
                  type="text"
                  value={editData.skills.join(', ')}
                  onChange={(e) => handleSkillsChange(e.target.value)}
                  placeholder="Suas habilidades (separadas por vírgula)"
                  className="edit-input"
                />
              </div>
            ) : (
              <div className="profile-info">
                <h1 className="profile-name">{profileData.name}</h1>
                <p className="profile-nickname">@{profileData.nickname}</p>
                <p className="profile-bio">{profileData.bio}</p>
                
                <div className="profile-skills">
                  <h3>Habilidades</h3>
                  <div className="skills-list">
                    {profileData.skills.map((skill, index) => (
                      <span key={index} className="skill-tag">
                        {skill}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            )}

            <div className="profile-actions">
              <button
                onClick={handleEdit}
                className={`btn-primary ${isEditing ? 'btn-save' : ''}`}
              >
                {isEditing ? 'Salvar' : 'Editar Perfil'}
              </button>
              {isEditing && (
                <button
                  onClick={handleCancel}
                  className="btn-secondary"
                >
                  Cancelar
                </button>
              )}
            </div>
          </section>

          {/* Seção de Projetos */}
          <section className="projects-section">
            <h2 className="section-title">Meus Projetos</h2>
            
            {profileData.projects.length > 0 ? (
              <div className="projects-grid">
                {profileData.projects.map((project, index) => (
                  <div key={index} className="project-card">
                    <h3 className="project-title">{project.name}</h3>
                    <p className="project-description">{project.description}</p>
                    <div className="project-technologies">
                      {project.technologies?.map((tech, techIndex) => (
                        <span key={techIndex} className="tech-tag">
                          {tech}
                        </span>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="projects-placeholder">
                <p>Nenhum projeto adicionado ainda.</p>
                <p>Adicione seus projetos para mostrar seu portfólio!</p>
                <button className="btn-primary">Adicionar Projeto</button>
              </div>
            )}
          </section>

          {/* Seção de Informações Adicionais */}
          <section className="additional-info">
            <div className="info-card">
              <h3>Informações de Contato</h3>
              <div className="contact-info">
                <p><strong>Email:</strong> {user.email}</p>
                <p><strong>Tipo de Usuário:</strong> {user.type ? 'Estudante' : 'Recrutador'}</p>
              </div>
            </div>
          </section>
        </div>
      </main>
    </div>
  );
}

export default ProfileImproved;

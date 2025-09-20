import React, { useState, useEffect } from 'react';
import { useAuth } from '../hooks/useAuth';
import './LoginImproved.css';
import logo from '../assets/logo.png';

function LoginImproved({ onClose }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [manterConectado, setManterConectado] = useState(true);
  const [showPassword, setShowPassword] = useState(false);
  
  const { login } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    try {
      await login(email, password);
      onClose(); // Fechar modal após login bem-sucedido
    } catch (error) {
      setError('Erro ao fazer login. Verifique suas credenciais.');
      console.error('Erro no login:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-modal-backdrop">
      <div className="login-modal-content">
        <div className="login-modal-header">
          <button className="login-close-btn" onClick={onClose}>×</button>
        </div>
        
        <div className="login-improved-container">
          <div className="login-logo-area">
            <img src={logo} alt="Logo" className="login-logo-img" />
            <span className="login-logo-title">INFINITY SCHOOL</span>
          </div>
          
          <h2 className="login-title">ENTRE NA SUA CONTA</h2>
          
          <form onSubmit={handleSubmit} className="login-form">
            {error && <div className="error-message">{error}</div>}
            
            <div className="form-group">
              <label htmlFor="email" className="login-label">E-MAIL</label>
              <input
                type="email"
                id="email"
                placeholder="DIGITE SEU EMAIL"
                className="login-input"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                disabled={loading}
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="password" className="login-label">SENHA</label>
              <div className="login-password-box">
                <input
                  type={showPassword ? "text" : "password"}
                  id="password"
                  placeholder="DIGITE SUA SENHA"
                  className="login-input"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  disabled={loading}
                />
                <button
                  type="button"
                  className="login-eye"
                  onClick={() => setShowPassword(!showPassword)}
                >
                  {showPassword ? '👁️' : '👁️‍🗨️'}
                </button>
              </div>
            </div>
            
            <button 
              type="submit" 
              className="login-btn"
              disabled={loading}
            >
              {loading ? 'ENTRANDO...' : 'FAZER LOGIN'}
            </button>
          </form>
          
          <div className="login-options">
            <label className="login-switch">
              <input 
                type="checkbox" 
                checked={manterConectado} 
                onChange={(e) => setManterConectado(e.target.checked)} 
              />
              <span className="login-switch-slider"></span>
              CONTINUAR CONECTADO
            </label>
            <a href="#" className="login-link">ESQUECI MINHA SENHA</a>
          </div>
          
          <div className="login-divider"></div>
          
          <div className="login-register">
            AINDA NÃO TEM CADASTRO? <a href="#" className="login-link">CRIE UMA CONTA.</a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LoginImproved;

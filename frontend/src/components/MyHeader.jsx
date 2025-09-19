import React from 'react';
import { useAuth } from '../hooks/useAuth';
import { useNavigate } from 'react-router-dom';
import "./MyHeader.css";
import logo from "../assets/logo.png";

function MyHeader() {
    const navigate = useNavigate();
    const { user, logout } = useAuth(); 

    const handleLogoClick = () => {
        navigate('/');
    };

    const handleAuthClick = () => {
        if (user) {
            // Se o usuário está logado, redirecionar para perfil
            navigate("/profile");
        } else {
            // Se não está logado, redirecionar para página de login
            navigate("/login");
        }
    };

    return (
        <header>
            <div className="center">
                <button className="logo-btn" onClick={handleLogoClick}>
                    <img src={logo} alt="IN logo" />
                </button>
            </div>
            <nav className="right">
                <button 
                    className="auth-btn"
                    onClick={handleAuthClick}
                >
                    {user ? 'PERFIL' : 'LOGIN'}
                </button>
                {user && (
                    <button 
                        className="logout-btn"
                        onClick={logout}
                    >
                        SAIR
                    </button>
                )}
            </nav>
        </header>
    );
}

export default MyHeader;


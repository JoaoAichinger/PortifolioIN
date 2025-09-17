import React, { useState } from 'react';
import { useAuth } from '../hooks/useAuth';
import { useNavigate } from 'react-router-dom';
import Login from './Login';
import "./MyHeader.css";
import logo from "../assets/logo.png";

function MyHeader() {
    const [showLogin, setShowLogin] = useState(false);

    const navigate = useNavigate();
    const { user, logout } = useAuth(); 

    const handleAuthClick = () => {
        if (user) {
            // Se o usuário está logado, redirecionar para perfil
            // Por enquanto, vamos apenas mostrar um alert
            alert('Redirecionando para o perfil... (Funcionalidade será implementada pela equipe responsável)');
            navigate("/profile");
        } else {
            // Se não está logado, mostrar modal de login
            //setShowLogin(true); //Modal Login
            navigate("/login");
        }
    };

    /*  Apenas usado com o modal
    const handleCloseLogin = () => {
        setShowLogin(false);
    };
    */

    return (
        <>
            <header>
                <div className="center">
                    <a href="https://infinityschool.com.br/">
                        <img src={logo} alt="IN logo" />
                    </a>
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
            
            {showLogin && <Login onClose={handleCloseLogin} />}
        </>
    );
}

export default MyHeader;


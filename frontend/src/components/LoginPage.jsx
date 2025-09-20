import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";
import "./LoginPage.css";

import simbolo from "./assets/simbolo.png";
import lg1 from "./assets/lg1.png";
import lg2 from "./assets/lg2.png";
import lg3 from "./assets/lg3.png";
import eyeIcon from "./assets/Frame.png";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [manterConectado, setManterConectado] = useState(true);
  const [showPassword, setShowPassword] = useState(false);
  const [carouselIndex, setCarouselIndex] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const carouselImages = [lg1, lg2, lg3];
  const { login } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    const interval = setInterval(() => {
      setCarouselIndex((prev) => (prev + 1) % carouselImages.length);
    }, 2500);
    return () => clearInterval(interval);
  }, [carouselImages.length]);

  const getCircleImages = () => [
    carouselImages[carouselIndex],
    carouselImages[(carouselIndex + 1) % carouselImages.length],
    carouselImages[(carouselIndex + 2) % carouselImages.length],
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    try {
      await login(email, senha);
      if (manterConectado) {
        localStorage.setItem("keepConnected", "true");
      } else {
        localStorage.removeItem("keepConnected");
      }
      navigate("/");
    } catch (err) {
      console.error(err);
      setError("Email ou senha incorretos. Tente novamente.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="main-bg">
      <div className="login-side">
        <div className="login-box">
          <div className="login-logo-area">
            <img src={simbolo} alt="IN" className="login-logo-img" />
            <span className="login-logo-title">INFINITY SCHOOL</span>
          </div>

          <h2 className="login-title">ENTRE NA SUA CONTA</h2>

          <form onSubmit={handleSubmit}>
            {error && <div className="error-message">{error}</div>}

            <label htmlFor="email" className="login-label">E-MAIL</label>
            <input
              id="email"
              type="email"
              placeholder="DIGITE SEU EMAIL"
              className="login-input"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              disabled={loading}
            />

            <label htmlFor="senha" className="login-label">SENHA</label>
            <div className="login-password-box">
              <input
                id="senha"
                type={showPassword ? "text" : "password"}
                placeholder="DIGITE SUA SENHA"
                className="login-input"
                value={senha}
                onChange={(e) => setSenha(e.target.value)}
                required
                disabled={loading}
              />
              <img
                src={eyeIcon}
                alt="Mostrar senha"
                className="login-eye"
                onClick={() => setShowPassword(!showPassword)}
              />
            </div>

            <button type="submit" className="login-btn" disabled={loading}>
              {loading ? "ENTRANDO..." : "FAZER LOGIN"}
            </button>
          </form>

          <div className="login-options">
            <label className="login-switch">
              <input
                type="checkbox"
                checked={manterConectado}
                onChange={(e) => setManterConectado(e.target.checked)}
                disabled={loading}
              />
              <span className="login-switch-slider"></span>
              CONTINUAR CONECTADO
            </label>
            <a href="/esqueci-senha" className="login-link">
              ESQUECI MINHA SENHA
            </a>
          </div>

          <div className="login-divider"></div>
          <div className="login-register">
            AINDA NÃO TEM CADASTRO?{" "}
            <a href="/criar-conta" className="login-link">
              CRIE UMA CONTA.
            </a>
          </div>
        </div>
      </div>

      <div className="highlight-side">
        <div className="highlight-circles">
          {getCircleImages().map((img, idx) => (
            <div className="highlight-circle" key={idx}>
              <img src={img} alt={`Curso ${idx + 1}`} />
            </div>
          ))}
        </div>
        <div className="highlight-dots">
          {carouselImages.map((_, idx) => (
            <span key={idx} className={`dot${carouselIndex === idx ? " active" : ""}`}></span>
          ))}
        </div>
        <div className="highlight-title">Cadastre seu portfólio</div>
        <div className="highlight-desc">
          Tenha acesso às melhores oportunidades de trabalho das nossas empresas parceiras!
        </div>
      </div>
    </div>
  );
}

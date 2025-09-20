// src/hooks/useAuth.js
import { useState, useEffect } from "react";
import api from "../services/api"; 

export function useAuth() {
  const [user, setUser] = useState(null);

  async function login(email, password) {
    const { data } = await api.post("/auth/login", { email, password });
    localStorage.setItem("access_token", data.access_token);

    // buscar perfil do usuário
    const profile = await api.get("/users/me");
    setUser(profile.data);
  }

  function logout() {
    localStorage.removeItem("access_token");
    setUser(null);
  }

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (token) {
      api.get("/users/me")
        .then((res) => setUser(res.data))
        .catch(() => logout());
    }
  }, []);

  return { user, login, logout };
}

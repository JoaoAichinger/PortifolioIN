// src/services/api.js
import axios from "axios";

// URL base do backend
const api = axios.create({
  baseURL: "http://localhost:8000", // ⬅️ troque pela URL do backend em produção
});

// Interceptor para injetar token JWT
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;

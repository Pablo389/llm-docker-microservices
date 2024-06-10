import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { AuthContext } from "../contexts/AuthContext";
import './Login.css';

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { setAuthToken } = useContext(AuthContext);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/login", {
        email: email,
        password: password
      });
      const token = response.data.access_token;
      setAuthToken(token);
      navigate("/home"); // Redirigir a la página home
    } catch (error) {
      console.error("Error during login:", error);
      // Manejar errores de inicio de sesión aquí
    }
  };

  return (
    <div className="login-container">
      <h1>Login</h1>
      <form onSubmit={handleSubmit} className="login-form">
        <div className="form-group">
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            style={{ color: "black" }} // Letras negras
            required
          />
        </div>
        <div className="form-group">
          <label>Contraseña:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            style={{ color: "black" }} // Letras negras
            required
          />
        </div>
        <button type="submit">Iniciar sesión</button>
      </form>
    </div>
  );
};

export default Login;


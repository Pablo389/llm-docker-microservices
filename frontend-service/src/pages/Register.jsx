import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { AuthContext } from "../contexts/AuthContext";
import './Login.css';

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { setAuthToken } = useContext(AuthContext);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/register", {
        email: email,
        password: password
      });
      const token = response.data.access_token;
      setAuthToken(token);
      navigate("/auth"); // Redirigir a la página login
    } catch (error) {
      console.error("Error during registering:", error);
      // Manejar errores de inicio de sesión aquí
    }
  };
  const handleLoginRedirect = () => {
    navigate("/auth"); // Redirigir a la página login
  };

  return (
    <div className="login-container">
      <h1>Register</h1>
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
        <button type="submit">Done</button>
        <button type="button" onClick={handleLoginRedirect}>
          Ya estoy registrad@
        </button>
      </form>
    </div>
  );
};

export default Register;
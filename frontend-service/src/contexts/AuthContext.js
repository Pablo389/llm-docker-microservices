import React, { createContext, useState , useEffect} from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [authToken, setAuthToken] = useState(() => {
    // Intenta obtener el token de localStorage cuando la app se cargue
    return localStorage.getItem("authToken") || null;
  });

  useEffect(() => {
    // Guarda el token en localStorage cuando cambie
    if (authToken) {
      localStorage.setItem("authToken", authToken);
    } else {
      localStorage.removeItem("authToken");
    }
  }, [authToken]);

  return (
    <AuthContext.Provider value={{ authToken, setAuthToken }}>
      {children}
    </AuthContext.Provider>
  );
};

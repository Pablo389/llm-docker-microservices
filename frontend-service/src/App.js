import "./normal.css";
import "./App.css";
import Home from "./pages/Home";
import Login from "./pages/Login";
import { Navigate, Route, Routes } from "react-router-dom";
import { useContext } from "react";

function App() {
  /*
  const { currentUser } = useContext(AuthContext);

  const RequireAuth = ({ children }) => {
    return currentUser ? children : <Navigate to="auth" />;
  };
  */

  return (
    <div className="App">
      <Routes>
        <Route exact path="/" element={<Navigate to="/auth" />} />
        <Route exact path="/home" element={<Home />} />
        <Route exact path="/auth" element={<Login />} />
      </Routes>
    </div>
  );
}

export default App;

import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import { Navigate, Route, Routes } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";

function App() {
  /*
  const { currentUser } = useContext(AuthContext);

  const RequireAuth = ({ children }) => {
    return currentUser ? children : <Navigate to="auth" />;
  };
  */

  return (
    <AuthProvider>
      <div className="App">
        <Routes>
          <Route exact path="/" element={<Navigate to="/register" />} />
          <Route exact path="/home" element={<Home />} />
          <Route exact path="/auth" element={<Login />} />
          <Route exact path="/register" element={<Register/>} />
        </Routes>
      </div>
    </AuthProvider>
  );
}

export default App;

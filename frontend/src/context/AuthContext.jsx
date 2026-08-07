import { createContext, useContext, useEffect, useState } from "react";
import client from "../api/client";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [token, setToken] = useState(
    localStorage.getItem("token") || ""
  );

  useEffect(() => {
    if (token) {
      client.defaults.headers.common[
        "Authorization"
      ] = `Bearer ${token}`;
    } else {
      delete client.defaults.headers.common["Authorization"];
    }
  }, [token]);

  function saveToken(value) {
    localStorage.setItem("token", value);

    client.defaults.headers.common[
      "Authorization"
    ] = `Bearer ${value}`;

    setToken(value);
  }

  function logout() {
    localStorage.removeItem("token");

    delete client.defaults.headers.common["Authorization"];

    setToken("");
  }

  return (
    <AuthContext.Provider
      value={{
        token,
        saveToken,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
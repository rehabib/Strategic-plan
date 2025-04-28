import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
    const [authTokens, setAuthTokens] = useState(() => localStorage.getItem('tokens') ? JSON.parse(localStorage.getItem('tokens')) : null);
    const [user, setUser] = useState(null);

    useEffect(() => {
        if (authTokens) {
            axios.defaults.headers.common['Authorization'] = `Bearer ${authTokens.access}`;
            axios.get('http://localhost:8000/api/user-profile/')
                .then(response => setUser(response.data))
                .catch(err => console.error(err));
        }
    }, [authTokens]);

    const login = async (username, password) => {
        try {
            const response = await axios.post('http://localhost:8000/api/token/', { username, password });
            setAuthTokens(response.data);
            localStorage.setItem('tokens', JSON.stringify(response.data));
            axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
            const userResponse = await axios.get('http://localhost:8000/api/user-profile/');
            setUser(userResponse.data);
        } catch (error) {
            console.error("Login Error:", error);
        }
    };

    const logout = () => {
        setAuthTokens(null);
        setUser(null);
        localStorage.removeItem('tokens');
        delete axios.defaults.headers.common['Authorization'];
    };

    return (
        <AuthContext.Provider value={{ user, login, logout, authTokens }}>
            {children}
        </AuthContext.Provider>
    );
};

export { AuthContext, AuthProvider };

import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

const Navbar = () => {
    const { user, logout } = useContext(AuthContext);

    return (
        <nav>
            <ul>
                <li><Link to="/dashboard">Dashboard</Link></li>
                {user ? (
                    <>
                        <li><Link to="/profile">Profile</Link></li>
                        <li><button onClick={logout}>Logout</button></li>
                    </>
                ) : (
                    <li><Link to="/login">Login</Link></li>
                )}
            </ul>
        </nav>
    );
};

export default Navbar;

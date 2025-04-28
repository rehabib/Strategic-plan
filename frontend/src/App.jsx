import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Navbar from './components/Navbar';
import Login from './components/Login';
import AgencyPlan from './components/AgencyPlan';
import DirectorPlan from './components/DirectorPlan';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<AgencyPlan />} />
          <Route path="/director-plan" element={<DirectorPlan />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;

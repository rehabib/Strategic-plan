import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DirectorPlan = () => {
    const [directorPlans, setDirectorPlans] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/director-plan/')
            .then(response => setDirectorPlans(response.data))
            .catch(err => console.error(err));
    }, []);

    return (
        <div>
            <h2>Director Plans</h2>
            <ul>
                {directorPlans.map(plan => (
                    <li key={plan.id}>
                        {plan.name} - {plan.description}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default DirectorPlan;

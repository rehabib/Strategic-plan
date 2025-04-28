import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AgencyPlan = () => {
    const [agencyPlans, setAgencyPlans] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/agency-plan/')
            .then(response => setAgencyPlans(response.data))
            .catch(err => console.error(err));
    }, []);

    return (
        <div>
            <h2>Agency Plans</h2>
            <ul>
                {agencyPlans.map(plan => (
                    <li key={plan.id}>
                        {plan.name} - {plan.description}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default AgencyPlan;

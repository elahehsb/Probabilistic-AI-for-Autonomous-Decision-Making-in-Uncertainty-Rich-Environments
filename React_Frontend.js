import React, { useState } from 'react';
import axios from 'axios';

const AIAdvisor = () => {
    const [data, setData] = useState({ success_rate: 0.5 });
    const [prediction, setPrediction] = useState(null);

    const handlePredict = async () => {
        const response = await axios.post('/api/predict', data);
        setPrediction(response.data);
    };

    return (
        <div>
            <h1>AI-Assisted Decision-Making</h1>
            <input
                type="number"
                value={data.success_rate}
                onChange={(e) => setData({ success_rate: parseFloat(e.target.value) })}
                placeholder="Success rate"
            />
            <button onClick={handlePredict}>Predict</button>
            {prediction && <div>Prediction: {prediction}</div>}
        </div>
    );
};

export default AIAdvisor;

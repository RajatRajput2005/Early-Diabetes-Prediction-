const express = require('express');
const cors = require('cors');
const { PythonShell } = require('python-shell');

const app = express();
app.use(cors());
app.use(express.json());

app.post('/predict', (req, res) => {
    const { age, gender, bmi, smoking_history, hba1c_level, blood_glucose_level } = req.body;

    const options = {
        mode: 'text',
        pythonOptions: ['-u'],
        scriptPath: './',
        args: [age, gender, bmi, smoking_history, hba1c_level, blood_glucose_level]
    };

    PythonShell.run('predict.py', options, (err, results) => {
        if (err) return res.status(500).send(err);
        res.json({ prediction: results[0] });
    });
});

app.listen(5000, () => {
    console.log('Server is running on http://localhost:5000');
});

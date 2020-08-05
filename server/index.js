require('dotenv').config();

const express = require('express');
const axios = require('axios');
const app = express();
const supercell = require('./api/supercell');
const bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({extended: true}));

app.post('/', async (req, res)=> {
	console.log(req.body);
	try {
		const response = await supercell.get(req.body.endpoint);
		const data = response.data;
		res.send(data);
	} catch(err) {
		console.log(err);
		res.send({err});
	}
});

app.get('/', (req, res) => {
	res.send("<h1>Test</h1>");
});

app.listen(process.env.PORT, () => {
	console.log("listening on port ", process.env.PORT);
});


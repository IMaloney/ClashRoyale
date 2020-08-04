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
		console.log(response);
		res.send({response});
	} catch(err) {
		res.send({err});
	}
});

app.get('/', (req, res) => {
	res.send("<h1>Test</h1>");
});

app.listen(3000, () => {
	console.log("listening on port 3000");
});

